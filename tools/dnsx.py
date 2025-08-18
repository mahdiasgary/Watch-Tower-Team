#!/usr/bin/env python3
import tempfile
import os

from utils import run_command_in_zsh


class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"


def dnsx(subdomains_array, domain):
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as temp_file:
        for sub in subdomains_array:
            temp_file.write(f"{sub}\n")
    subdomains_file = temp_file.name

    command = (
        f"dnsx -l {subdomains_file} -silent  -resp -json "
        f"-rl 30 -t 10 -r 8.8.4.4,129.250.35.251,208.67.222.222"
    )
    print(f"{Colors.GRAY}Executing command: {command}{Colors.RESET}")

    try:
        results = run_command_in_zsh(command)
    finally:
        os.remove(subdomains_file)

    import json
    results_json = [json.loads(line) for line in results if line.strip()]
    return results_json
