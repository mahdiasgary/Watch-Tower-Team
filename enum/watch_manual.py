#!/usr/bin/env python3
import sys
import re
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.services import upsert_subdomain
from database.selectors import get_program_by_scope

from utils import current_time

def parse_args():
    parser = argparse.ArgumentParser(description="Subfinder Automation Script")
    parser.add_argument('-p', '--provider', required=True, help="Specify the provider")
    parser.add_argument('-subs', '--subs', required=True, help="File containing subdomains")
    parser.add_argument('-d', '--domain', required=True, help="Target domain")
    return parser.parse_args()

def process_subfinder(domain, provider, subs_file):
    program = get_program_by_scope(domain)

    if program:
        print(f"[{current_time()}] running {provider} module for '{domain}'")
        with open(subs_file, 'r') as file:
            subs = file.readlines()

        for sub in subs:
            sub = sub.strip()
            if re.search(r"\.\s*" + re.escape(domain), sub, re.IGNORECASE):
                upsert_subdomain(program.program_name, sub,provider )
    else:
        print(f"[{current_time()}] scope for '{domain}' does not exist in watchtower")

if __name__ == "__main__":
    args = parse_args()

    domain = args.domain
    provider = args.provider
    subs_file = args.subs

    if not domain or not provider or not subs_file:
        print(f"Usage: python3 app.py -p <provider> -subs <subdomain file> -d <domain>")
        sys.exit(1)

    process_subfinder(domain, provider, subs_file)
