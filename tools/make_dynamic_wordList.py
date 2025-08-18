import os
import tempfile
from utils import run_command_in_zsh
from config import config

from database.selectors import get_subdomains


class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"

WATCH__DIR = config().get("WATCH__DIR")
def make_dynamic_wordList(domain):
    with tempfile.TemporaryDirectory() as temp_dir:
        dns_subs = os.path.join(temp_dir, "dns_subs.txt")
        
        # Step 2: Get subdomains for dynamic brute
        subdomains = get_subdomains(scope=domain)
        subs =[obj_sub.subdomain for obj_sub in subdomains]
        with open(dns_subs, 'w') as file:
            for sub in subs:
                print(sub)
                file.write(f"{sub}\n")  # Write each subdomain on a new line


        dns_txt_path = os.path.expanduser("~/Watch-Tower-Team/utils/dns.txt")
        output_file = os.path.join("wordlist", f"{domain}_dynamic_wordlist.txt")

        command = f"dnsgen -w {dns_txt_path} {dns_subs} | sort -u > {output_file}"
        run_command_in_zsh(command)


