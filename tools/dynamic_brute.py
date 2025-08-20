import os
import shutil
from utils import run_command_in_zsh

class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"

def dynamic_brute(domain):
    # ساخت پوشه wordlist اگر وجود نداشت
    os.makedirs("wordlist", exist_ok=True)

    wordListPath = os.path.join("wordlist", f"{domain}_dynamic_wordlist.txt")
    resolvers_path = os.path.expanduser("~/.resolvers")

    # بررسی وجود فایل wordlist
    if not os.path.isfile(wordListPath):
        raise FileNotFoundError(f"Wordlist file does not exist: {wordListPath}")
    # بررسی خالی نبودن فایل
    if os.path.getsize(wordListPath) == 0:
        raise ValueError(f"Wordlist file is empty: {wordListPath}")

    # بررسی نصب بودن massdns
    if not shutil.which("massdns"):
        raise RuntimeError("massdns not found in PATH")

    shuffledns_command = (
        f"shuffledns -list {wordListPath} -d {domain} -r {resolvers_path} "
        f"-m $(which massdns) -mode resolve -t 100"
    )
    print(f"{Colors.GRAY}Executing command: {shuffledns_command}{Colors.RESET}")
    result = run_command_in_zsh(shuffledns_command)

    return result
