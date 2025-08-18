#!/usr/bin/env python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.services import upsert_subdomain
from database.selectors import get_program_by_scope
from tools import dynamic_brute
from utils import current_time

if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else None

    if not domain:
        print("Usage: watch_ns_brute domain")
        sys.exit(1)

    program = get_program_by_scope(domain)

    if not program:
        print(f"[{current_time()}] scope for '{domain}' does not exist in watchtower")
        sys.exit(1)

    print(f"[{current_time()}] running ns_brute module for '{domain}'")

    # دریافت زیر دامنه‌ها و جایگزینی None با لیست خالی
    try:
        subs = dynamic_brute(domain) or []
    except Exception as e:
        print(f"[{current_time()}] Error in dynamic_brute: {e}")
        subs = []

    for sub in subs:
        # فقط زیر دامنه‌هایی که واقعاً متعلق به دامنه هستند ذخیره شوند
        if sub.lower().endswith("." + domain.lower()):
            upsert_subdomain(program.program_name, sub, "dynamic_brute")
            print(f"[{current_time()}] found {sub}")

    print(f"[{current_time()}] ns_brute module finished for '{domain}'")
