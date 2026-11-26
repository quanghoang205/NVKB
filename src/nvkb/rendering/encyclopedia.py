"""Learner navigation built from authored groups, separate from provenance notes."""

from collections import defaultdict


def add_encyclopedia_navigation(items, note, links):
    cves = [x for x in items if x["entity_type"] == "Vulnerability"]
    curated = [x for x in cves if x.get("curation_version") == "1.3.0"]
    if not curated:
        return
    ids = {x["id"] for x in items}
    groups = defaultdict(list)
    for item in cves:
        groups[item.get("research_group", "Chưa biên tập v1.3")].append(item)
    body = "Tra cứu theo cơ chế và kiến thức nền. Maturity là trạng thái biên tập; đọc evidence ở từng bài để biết mức hỗ trợ. Không suy fault location từ liên kết học tập.\n\n"
    for group, members in sorted(groups.items()):
        body += (
            "## "
            + group
            + "\n\n"
            + "\n".join(
                "- "
                + links([x["id"]])
                + " — "
                + x["title"]
                + " — **"
                + x.get("editorial_maturity", "METADATA_ONLY")
                + "**"
                for x in members
            )
            + "\n\n"
        )
    note("00-Home/MOC-CVE-Encyclopedia.md", "CVE Encyclopedia", body)
    note(
        "00-Home/MOC-CVE-by-Publication-Year.md",
        "CVE by Publication Year",
        "Năm công bố thực tế, không suy từ CVE ID.\n\n"
        + " · ".join("[[MOC-CVE-" + str(y) + "]]" for y in sorted({x["publication_year"] for x in cves})),
    )
    topics = {
        "NGINX-Architecture": (
            [
                "DEPLOYMENT:REVERSE-PROXY",
                "COMPONENT:MASTER-PROCESS",
                "COMPONENT:EVENT-DRIVEN",
                "COMPONENT:CONNECTION-LIFECYCLE",
                "COMPONENT:MEMORY-POOL",
            ],
            set(groups),
        ),
        "Memory-Safety": (
            [
                "COMPONENT:MEMORY-POOL",
                "WEAKNESS:CWE-787",
                "WEAKNESS:CWE-125",
                "WEAKNESS:CWE-122",
                "WEAKNESS:CWE-416",
                "CONTROL:RESOURCE-BOUNDS",
            ],
            {"media", "http", "resolver", "multiplexing"},
        ),
        "Protocol-Security": (
            ["PROTOCOL:TLS", "PROTOCOL:HTTP-2", "PROTOCOL:HTTP-3", "PROTOCOL:QUIC", "PROTOCOL:DNS"],
            {"tls", "quic", "multiplexing", "mail", "resolver"},
        ),
        "HTTP-Processing": (
            [
                "COMPONENT:CONNECTION-LIFECYCLE",
                "COMPONENT:REQUEST-PARSING",
                "COMPONENT:REWRITE-ENGINE",
                "COMPONENT:UPSTREAM-COMMUNICATION",
                "MODULE:NGX-HTTP-CHARSET-MODULE",
            ],
            {"http", "proxy", "multiplexing"},
        ),
        "Media-Processing": (["MODULE:NGX-HTTP-MP4-MODULE", "COMPONENT:MEMORY-POOL"], {"media"}),
        "Defensive-Engineering": (
            ["CONTROL:RESOURCE-BOUNDS", "CONTROL:LEAST-PRIVILEGE", "CONTROL:PATCH-VERIFICATION"],
            set(groups),
        ),
        "Patch-Management": (
            ["CONCEPT:ADVISORY", "CONCEPT:BACKPORT", "CONTROL:PATCH-VERIFICATION", "CONCEPT:CVE"],
            set(groups),
        ),
    }
    for name, (knowledge, selected) in topics.items():
        content = "Kiến thức nền theo thứ tự gợi ý:\n\n" + links([k for k in knowledge if k in ids])
        content += "\n\n## CVE nghiên cứu liên quan\n\n" + "\n".join(
            "- " + links([x["id"]]) + " — " + x.get("editorial_maturity", "METADATA_ONLY")
            for x in curated
            if x["research_group"] in selected
        )
        content += "\n\n[[MOC-CVE-Encyclopedia|Encyclopedia]] · [[Learning-Library|Lộ trình học]]"
        note("00-Home/MOC-" + name + ".md", name.replace("-", " "), content)
    note(
        "00-Home/MOC-Research-Review-Queue.md",
        "Research Review Queue",
        "Không bài nào được tự cấp HUMAN_APPROVED. Review kỹ thuật độc lập và learner testing còn chờ.\n\n"
        + "\n".join(
            "- "
            + links([x["id"]])
            + " — "
            + x.get("editorial_maturity", "METADATA_ONLY")
            + ": "
            + x.get("editorial_review_note", "Chưa có review v1.3")
            for x in cves
        )
        + "\n\n[[Research-Library|Claim/Evidence và lịch sử]] · [[MOC-CVE-Encyclopedia|Quay lại bài học]]",
    )
