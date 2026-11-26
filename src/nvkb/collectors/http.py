"""Small requests adapter: immutable snapshots, conditional GET, bounded retry."""

from __future__ import annotations

import hashlib
import json
import time
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests
from pyvulnerabilitylookup import PyVulnerabilityLookup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from nvkb.config import Config, utcnow
from nvkb.storage.canonical import atomic_write, json_text


class SourceError(RuntimeError):
    pass


class Fetcher:
    def __init__(self, config: Config, offline=False, refresh=False, session=None):
        self.config, self.offline, self.refresh = config, offline, refresh
        options = config.settings["http"]
        self.timeout = options["timeout"]
        self.interval = options.get("minimum_interval", 0.35)
        self.ttl = options.get("cache_ttl_hours", 24) * 3600
        self.session = session or requests.Session()
        retries = Retry(
            total=options["retries"],
            backoff_factor=options["backoff_factor"],
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD"],
            respect_retry_after_header=True,
            backoff_max=30,
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))
        self.session.headers.update(
            {"User-Agent": "NVKB/1.0 (local scholarly library; public advisory lookups)"}
        )
        self.last_request = 0.0
        self.host_last = {}
        self.failures: list[dict] = []
        self.sdk = PyVulnerabilityLookup(root_url=config.sources["vulnerability_lookup"]["url"])
        self.sdk.session.close()
        self.sdk.session = self.session

    def fetch(self, url: str, category: str, *, sdk_id: str | None = None, expect_json=False) -> dict:
        key = hashlib.sha256(url.encode()).hexdigest()
        pointer = self.config.path(f"data/raw/{category}/{key}.meta.json")
        old = json.loads(pointer.read_text()) if pointer.exists() else None
        if old and (
            self.offline
            or (
                not self.refresh
                and (
                    datetime.now(timezone.utc)
                    - datetime.fromisoformat(old.get("checked_at", old["retrieved_at"]))
                ).total_seconds()
                < self.ttl
            )
        ):
            return self._cached(old)
        if self.offline:
            raise SourceError(f"Offline cache miss: {url}")
        try:
            host = urlparse(url).netloc
            interval = self.config.settings["http"].get("host_intervals", {}).get(host, self.interval)
            time.sleep(max(0.0, interval - (time.monotonic() - self.host_last.get(host, 0.0))))
            headers = {}
            if old:
                if old.get("etag"):
                    headers["If-None-Match"] = old["etag"]
                if old.get("last_modified"):
                    headers["If-Modified-Since"] = old["last_modified"]
            if sdk_id:
                # SDK 4.5.0 does not expose timeout/response metadata. Adapt only its GET call.
                original_get = self.session.get
                response_box = []

                def sdk_get(target, **kwargs):
                    response = original_get(target, timeout=self.timeout, **kwargs)
                    response.raise_for_status()
                    response_box.append(response)
                    return response

                self.session.get = sdk_get
                try:
                    self.sdk.get_vulnerability(sdk_id)
                    response = response_box[0]
                finally:
                    self.session.get = original_get
            else:
                response = self.session.get(url, timeout=self.timeout, headers=headers)
            self.last_request = time.monotonic()
            self.host_last[host] = self.last_request
            if response.status_code == 304 and old:
                old["checked_at"] = utcnow()
                atomic_write(pointer, json_text(old))
                return self._cached(old)
            response.raise_for_status()
            if not response.content:
                raise ValueError("Empty response")
            if expect_json or sdk_id:
                value = response.json()
                if not isinstance(value, (dict, list)) or not value:
                    raise ValueError("Missing JSON object or list")
            body = response.content
            digest = hashlib.sha256(body).hexdigest()
            extension = "json" if expect_json or sdk_id else "html"
            relative = f"data/raw/{category}/snapshots/{digest}.{extension}"
            atomic_write(self.config.path(relative), body)
            meta = dict(
                source_url=url,
                retrieved_at=old["retrieved_at"] if old and old["content_hash"] == digest else utcnow(),
                checked_at=utcnow(),
                content_hash=digest,
                local_snapshot_path=relative,
                etag=response.headers.get("ETag"),
                last_modified=response.headers.get("Last-Modified"),
                content_type=response.headers.get("Content-Type", ""),
            )
            atomic_write(pointer, json_text(meta))
            return {**meta, "text": body.decode("utf-8", errors="replace")}
        except (requests.RequestException, ValueError, KeyError, IndexError) as exc:
            self.failures.append(dict(url=url, error=str(exc), at=utcnow()))
            raise SourceError(f"{url}: {exc}") from exc

    def _cached(self, meta):
        path = self.config.path(meta["local_snapshot_path"])
        if not path.exists():
            raise SourceError(f"Missing snapshot: {path}")
        body = path.read_bytes()
        if hashlib.sha256(body).hexdigest() != meta["content_hash"]:
            raise SourceError(f"Snapshot hash mismatch: {path}")
        return {**meta, "text": body.decode("utf-8", errors="replace")}

    def close(self):
        self.session.close()
