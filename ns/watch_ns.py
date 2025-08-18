#!/usr/bin/env python3
import sys
import json
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.services import upsert_lives
from database.selectors import get_subdomains

from tools import dnsx

from utils import current_time, get_ip_tag


if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else False

    if not domain:
        print("Usage: watch_ns <domain>")
        sys.exit()

    obj_subs = get_subdomains(scope=domain)

    if not obj_subs:
        print(f"[{current_time()}] Domain '{domain}' does not exist in watchtower")
        sys.exit()

    print(f"[{current_time()}] Running Dnsx module for '{domain}'")
    subdomains = [obj_sub.subdomain for obj_sub in obj_subs]
    print(f"\033[32m length: {len(subdomains)} \033[0m")

    results = dnsx(subdomains, domain)

    for result in results:
        # اگر نتیجه هنوز str است، JSON کنیم
        obj = result if isinstance(result, dict) else json.loads(result)

        if not obj.get("a"):
            print(f"Invalid 'a' field in result: {obj}")
            continue

        tag = get_ip_tag(obj.get("a"))

        # پیدا کردن providers
        idx = next((i for i, sub_info in enumerate(obj_subs) if sub_info.subdomain == obj.get("host")), -1)
        providers = obj_subs[idx].providers if idx != -1 else []

        upsert_lives(
            domain=domain,
            subdomain=obj.get("host"),
            ips=obj.get("a"),
            tag=tag,
            providers=providers
        )
