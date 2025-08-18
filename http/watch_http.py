#!/usr/bin/env python3
import sys, os, json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.selectors import get_lives
from database.services import upsert_http
from utils import current_time
from tools import httpx


if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else False

    if domain is False:
        print(f"Usage: watch_http domain")
        sys.exit()

    obj_lives = get_lives(scope=domain)

    if obj_lives:
        print(f"[{current_time()}] running HTTPx module for '{domain}'")
        subdomains = [obj.subdomain for obj in obj_lives]
        print(f"\033[32m length: {len(subdomains)} \033[0m")
        result = httpx(subdomains, domain)

        for obj in result:
            http = {
                "subdomain": obj.get("input"),
                "scope": domain,
                "providers": obj_lives[next((i for i, sub_info in enumerate(obj_lives) if sub_info['subdomain'] == obj.get("input")), -1)].providers,
                "ips": obj.get("a", ""),
                "tech": obj.get("tech", []),
                "title": obj.get("title", ""),
                "status_code": str(obj.get("status_code", "")),
                "headers": obj.get("header", {}),
                "url": obj.get("url", ""),
                "final_url": obj.get("final_url", ""),
                "favicon": obj.get("favicon", ""),
            }
            upsert_http(**http)
