import requests

class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"

def crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    print(f"{Colors.GRAY}Executing HTTP Request: {url}{Colors.RESET}")
    res = requests.get(url)
    if res.status_code != 200:
        return []

    data = res.json()
    subdomains = set()
    for entry in data:
        name = entry["name_value"]
        for n in name.split("\n"):
            if "*" not in n:
                subdomains.add(n.lower())

    return list(subdomains)

