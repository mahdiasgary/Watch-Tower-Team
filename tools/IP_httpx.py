import tempfile
import os
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

class Colors:
    GRAY = "\033[90m"
    RESET = "\033[0m"

def run_command_in_zsh(command):
    try:
        result = subprocess.run(["bash", "-c", command], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"{Colors.GRAY}Error: {result.stderr}{Colors.RESET}")
        return result.stdout
    except Exception as e:
        print(f"Exception occurred: {e}")
        return ""

def split_ips_arr_full(file_path, chunk_size=100):
    with open(file_path, 'r') as file:
        ip_list = [line.strip() for line in file if line.strip()]
    print(f"{Colors.GRAY}Number of all IPs: {len(ip_list)}{Colors.RESET}")
    batches_of_100 = [ip_list[i:i + chunk_size] for i in range(0, len(ip_list), chunk_size)]
    return [[batch[i:i + 10] for i in range(0, len(batch), 10)] for batch in batches_of_100]

def run_httpx(batch):
    results = []
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write("\n".join(batch).encode())
        temp_file_path = temp_file.name

    command = [
        "httpx",
        "-l", temp_file_path,
        "-silent",
        "-json",
        "-favicon",
        "-fhr",
        "-tech-detect",
        "-irh",
        "-include-chain",
        "-timeout", "3",
        "-retries", "1",
        "-threads", "20",  # تعداد کنترل شده
        "-rate-limit", "4",
        "-ports", "80,443",
        "-extract-fqdn",
        "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0"
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if stderr:
        print(f"{Colors.GRAY}[httpx error]: {stderr.decode()}{Colors.RESET}")

    os.remove(temp_file_path)

    for line in stdout.decode().splitlines():
        try:
            results.append(json.loads(line))
        except json.JSONDecodeError:
            print(f"{Colors.GRAY}[Invalid JSON skipped]: {line}{Colors.RESET}")

    return results

def multi_httpx(ips_list_arr, max_workers=5):
    all_results = []
    counter = 0
    for ips_list in ips_list_arr:
        print(f"{Colors.GRAY}Processing IPs {counter} to {counter + 100}{Colors.RESET}")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(run_httpx, batch) for batch in ips_list]
            for future in as_completed(futures):
                all_results.extend(future.result())
                print(all_results)
        counter += 100
    return all_results

def IP_httpx(asns):
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp_file:
        ips_file = tmp_file.name

    print(f"{Colors.GRAY}Processing ASN List...{Colors.RESET}")

    for asn in asns:
        command_asn_to_ip = (
            f"curl -s 'https://api.bgpview.io/asn/{asn}/prefixes' "
            f"-H 'user-agent:Mozilla/5.0' | "
            f"jq -r '.data.ipv4_prefixes[]?.prefix' | mapcidr -silent >> {ips_file}"
        )
        run_command_in_zsh(command_asn_to_ip)

    ips_list_arr = split_ips_arr_full(ips_file)
    all_results = multi_httpx(ips_list_arr)
    os.remove(ips_file)

    print(f"{Colors.GRAY}httpx processing finished and tmp file deleted{Colors.RESET}")
    return all_results
