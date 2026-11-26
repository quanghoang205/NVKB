"""Conservative patch comparison for supplied inventories; no remote probes."""

from __future__ import annotations

import re

from debian.debian_support import Version as DebianVersion
from packaging.version import Version
from rpm_vercmp import vercmp

from nvkb.collectors.sources import PRODUCTS, classify_product


def upstream(value: str) -> Version:
    if not re.fullmatch(r"\d+\.\d+\.\d+", value):
        raise ValueError(f"Unsupported upstream release: {value!r}; use a distribution package comparator")
    return Version(value)


def compare(a: str, b: str, ecosystem="upstream") -> int:
    if ecosystem in {"debian", "ubuntu"}:
        x, y = DebianVersion(a), DebianVersion(b)
        return (x > y) - (x < y)
    if ecosystem == "rpm":
        if "^" in a or "^" in b:
            raise ValueError(
                "rpm-vercmp 0.1.2 does not implement modern caret ordering; manual review required"
            )

        def evr(value):
            epoch, _, rest = value.partition(":")
            if not rest:
                epoch, rest = "0", epoch
            version, separator, release = rest.rpartition("-")
            if not separator:
                version, release = rest, ""
            return int(epoch), version, release

        x, y = evr(a), evr(b)
        return ((x[0] > y[0]) - (x[0] < y[0])) or vercmp(x[1], y[1]) or vercmp(x[2], y[2])
    if ecosystem != "upstream":
        raise ValueError(f"Unsupported ecosystem: {ecosystem}")
    x, y = upstream(a), upstream(b)
    return (x > y) - (x < y)


def parse_ranges(expression: str) -> list[dict]:
    ranges = []
    for fragment in expression.split(","):
        fragment = fragment.strip()
        if not fragment:
            continue
        match = re.fullmatch(r"(\d+\.\d+\.\d+)(?:-(\d+\.\d+\.\d+))?", fragment)
        if not match:
            raise ValueError(f"Unparsed vendor version expression: {fragment}")
        lower, upper = match.group(1), match.group(2) or match.group(1)
        if compare(lower, upper) > 0:
            raise ValueError(f"Reversed version range: {fragment}")
        ranges.append(
            dict(
                lower=lower,
                upper=upper,
                lower_inclusive=True,
                upper_inclusive=True,
                exclusions=[],
                ecosystem="upstream",
                raw_expression=fragment,
            )
        )
    return ranges


def in_range(version: str, interval: dict) -> bool:
    ecosystem = interval.get("ecosystem", "upstream")
    if version in interval.get("exclusions", []):
        return False
    for bound, inclusive, direction in [("lower", "lower_inclusive", 1), ("upper", "upper_inclusive", -1)]:
        if interval.get(bound):
            sign = compare(version, interval[bound], ecosystem) * direction
            if sign < 0 or (sign == 0 and not interval.get(inclusive, True)):
                return False
    return True


def release_is_fixed(version: str, fixes: list[str]) -> bool:
    current = upstream(version)
    releases = [upstream(v) for v in fixes]
    if not releases:
        return False
    branch = current.release[:2]
    return any(branch == f.release[:2] and current >= f for f in releases) or branch > max(
        f.release[:2] for f in releases
    )


def _assess_versions(asset: dict, vulnerability: dict, entities: dict[str, dict]) -> dict:
    result = dict(
        asset_id=asset["asset_id"],
        relevant_advisory=vulnerability["cve_id"],
        remediation_status="UNKNOWN",
        required_manual_review=True,
        vendor_source=[
            entities[x]["source_url"]
            for x in vulnerability["source_refs"]
            if entities[x]["publisher"] == "NGINX / F5"
        ],
        patch_recommendation="Đối chiếu advisory và bản vá đúng sản phẩm/nhánh.",
        assessment_limitations="Đối chiếu bản vá từ inventory; chưa xác nhận cấu hình, tính năng hay khả năng khai thác.",
    )
    supplied_product = asset.get("product", "")
    if not isinstance(supplied_product, str):
        result["remediation_status"] = "NEEDS_REVIEW"
        return result
    product = (
        supplied_product
        if supplied_product in {"PRODUCT:" + key for key in PRODUCTS}
        else classify_product(supplied_product)
    )
    if product is None:
        result["remediation_status"] = "NEEDS_REVIEW"
        return result
    if product != "PRODUCT:NGINX-OSS":
        result.update(remediation_status="NOT_APPLICABLE", required_manual_review=False)
        return result
    if vulnerability["verification_status"] in {"CONFLICTED", "UNVERIFIED", "UNKNOWN", "REJECTED"}:
        result["remediation_status"] = "NEEDS_REVIEW"
        return result
    distribution = asset.get("distribution")
    try:
        if distribution:
            candidates = [
                entities[x]
                for x in vulnerability.get("distribution_status", [])
                if entities[x]["distribution"].lower() == distribution.lower()
                and entities[x].get("release") == asset.get("release")
                and entities[x].get("package_name") == asset.get("package_name", "nginx")
                and entities[x]["verification_status"] == "VERIFIED"
            ]
            if len(candidates) != 1 or not asset.get("package_version"):
                result["remediation_status"] = "NEEDS_REVIEW"
                return result
            package = candidates[0]
            result["distribution_source"] = [entities[r]["source_url"] for r in package["source_refs"]]
            if package.get("patch_status") == "not-affected":
                status = "NOT_APPLICABLE"
            elif package.get("fixed_version"):
                status = (
                    "PATCHED"
                    if compare(asset["package_version"], package["fixed_version"], package["ecosystem"]) >= 0
                    else "UPDATE_REQUIRED"
                )
            else:
                status = "NEEDS_REVIEW"
            result["assessment_limitations"] += (
                " Dùng tracker đúng distribution/release; không so sánh SemVer."
            )
        else:
            if asset.get("package_version"):
                result["remediation_status"] = "NEEDS_REVIEW"
                return result
            version = asset.get("installed_version", "")
            current = upstream(version)
            observed = [
                upstream(item["version"])
                for item in entities.values()
                if item.get("entity_type") == "Version"
                and item.get("product_id") == "PRODUCT:NGINX-OSS"
                and item.get("verification_status") == "VERIFIED"
            ]
            if not observed or current > max(observed):
                result["remediation_status"] = "NEEDS_REVIEW"
                return result
            fixes = [entities[x]["version"] for x in vulnerability.get("fixed_versions", [])]
            ranges = [entities[x] for x in vulnerability.get("affected_version_ranges", [])]
            if release_is_fixed(version, fixes):
                status = "PATCHED" if current in observed else "NEEDS_REVIEW"
            elif any(in_range(version, r) for r in ranges):
                status = "UPDATE_REQUIRED"
            elif ranges and (
                all(r.get("lower") and compare(version, r["lower"]) < 0 for r in ranges)
                or any(version in r.get("exclusions", []) for r in ranges)
            ):
                status = "NOT_APPLICABLE"
            else:
                status = "UNKNOWN"
            result["patch_recommendation"] = "Bản upstream đã sửa: " + (", ".join(fixes) or "chưa biết")
        result.update(remediation_status=status, required_manual_review=status in {"UNKNOWN", "NEEDS_REVIEW"})
    except (ValueError, TypeError, KeyError):
        result["remediation_status"] = "NEEDS_REVIEW"
    return result


def assess(asset: dict, vulnerability: dict, entities: dict[str, dict]) -> dict:
    """Keep the legacy comparison result while separating operational claims."""
    result = _assess_versions(asset, vulnerability, entities)
    result.update(
        advisory_patch_status="DOCUMENTED_FIX" if vulnerability.get("fixed_versions") else "UNKNOWN",
        distribution_package_status=result["remediation_status"]
        if asset.get("distribution")
        else "NOT_EVALUATED",
        product_support_lifecycle=vulnerability.get("lifecycle_status", "UNKNOWN"),
        kev_catalogue_membership=vulnerability.get("kev_status", "UNKNOWN"),
        kev_snapshot_membership=vulnerability.get("kev_snapshot_status", "UNKNOWN"),
        kev_catalogue_version=vulnerability.get("kev_catalogue_version", "UNKNOWN"),
        runtime_verification_status="ADMINISTRATOR_REPORTED" if asset.get("runtime_evidence") else "UNKNOWN",
        inventory_provenance=asset.get("inventory_provenance", "NOT_SUPPLIED"),
        package_origin=asset.get("package_origin", "UNKNOWN"),
        comparison_meaning="remediation_status is a legacy version comparison, not running-binary attestation.",
    )
    if result["remediation_status"] == "PATCHED":
        result["required_manual_review"] = True
        result["assessment_limitations"] += (
            " Runtime/build/restart provenance requires review; administrator evidence is not independent attestation."
        )
    if asset.get("custom_build") or asset.get("package_origin") in {"custom", "unknown", "untrusted"}:
        result.update(remediation_status="NEEDS_REVIEW", required_manual_review=True)
    return result
