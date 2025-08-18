from utils import run_command_in_zsh


class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"


def abuseipdb(domain):
    command = (
    f'curl -s "https://www.abuseipdb.com/whois/{domain}" '
    '-H "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" '
    f'-b "abuseipdb_session=eyJpdiI6IkNQU2EzYkFLMjlHVGJvM3cwR1pjaGc9PSIsInZhbHVlIjoiZGtJMkZEWXhNNUtxRVBQN2cwbmNQOWVneGF2WThIWlBiMTJIZlRnUTZSQ0NYaXZsWmx0dDB3K09jeThwWWxBb1I4NE5Dbjgzeis5SFNRZ3BWVFNhNGtlQ3EvNUtGMXViL05CZ1RlWUJiZ0dtWVRTVmN3QlJ2NlR2MER4QUREODUiLCJtYWMiOiIwYjJmMThiMWVlMjQ5YTI1MDZlMDg1Nzc0YmM4ODc5MTJjYzZmOGM2YWIxMzY1Njk3M2RjZDM5YWUwYTM1ODllIiwidGFnIjoiIn0%3D" | '
    f'grep -oP "<li>.*?{domain}.*?</li>" | sed -E "s/<\\/?li>//g"'
)



    print(f"{Colors.GRAY}Executing commands: {command}{Colors.RESET}")
    res = run_command_in_zsh(command)

    res_num = len(res) if res else 0
    print(f"{Colors.GRAY}done for {domain}, results: {res_num}{Colors.RESET}")

    return res


