
import tempfile
import os
import json
from utils import run_command_in_zsh


class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"


def httpx(subdomains, domain):
    responses = []

    # ساخت فایل موقت برای subdomainها
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp_file:
        for sub in subdomains:
            temp_file.write(f"{sub}\n")
        subdomains_file = temp_file.name

    # دستور httpx (فقط فلگ‌های معمول که تو همه نسخه‌ها هستن)
    command = f"httpx -l {subdomains_file} -silent -json -favicon -fhr -tech-detect -irh -include-chain -timeout 3 -retries 1 -threads 5 -rate-limit 4 -ports 443 -extract-fqdn -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0' -H 'Referer: https://{domain}'"

    print(f"{Colors.GRAY}Executing command: {command}{Colors.RESET}")

    try:
        result = run_command_in_zsh(command, read_line=False)

        for r in result.splitlines():
            if not r.strip():
                continue  # پرش از خطوط خالی
            try:
                responses.append(json.loads(r))
            except json.JSONDecodeError:
                print(f"{Colors.GRAY}[!] Skipped invalid JSON line: {r}{Colors.RESET}")
                continue

    finally:
        # پاک کردن فایل موقت حتی اگر خطا بخوره
        if os.path.exists(subdomains_file):
            os.remove(subdomains_file)

    return responses
