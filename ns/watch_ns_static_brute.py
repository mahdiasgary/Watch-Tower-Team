#!/usr/bin/env python3
import sys, re, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.services import upsert_subdomain
from database.selectors import get_program_by_scope

from tools import static_brute
from config import config

from utils import current_time,run_command_in_zsh


if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else False
    ns_path = config().get("WATCH__DIR") + "ns"

    if not domain:
        print(f"Usage: watch_ns_brute domain")
        sys.exit()

    program = get_program_by_scope(domain)

    if program:
        print(f"[{current_time()}] running ns_brute module for '{domain}'")
        try:
            subs = static_brute(domain) or []
        except Exception as e:
            print(f"[{current_time()}] Error in dynamic_brute: {e}")
            subs = []

        for sub in subs:
            # فقط زیر دامنه‌هایی که واقعاً متعلق به دامنه هستند ذخیره شوند
            if sub.lower().endswith("." + domain.lower()):
                upsert_subdomain(program.program_name, sub, "dynamic_brute")
                print(f"[{current_time()}] found {sub}")

    else:
        print(f"[{current_time()}] scope for '{domain}' does not exist in watchtower")
