import requests
from config import config
from utils import current_time
import time

"""
State: 
    HTTP:
    1. Change Title -> http_title
    2. Change Status code -> http_status_code
    1. Change Favicon -> http_favicon

    Live: 
    1. Fresh -> live_fresh

    nuclei: nuclei_result
"""

import subprocess

def run_command_in_zsh(command, read_line=True):
    try:
        result = subprocess.run(["bash", "-c", command], capture_output=True, text=True)
        time.sleep(1)
        if result.returncode != 0:
            print("Error occurred:", result.stderr)
            return False
        if read_line:
            return result.stdout.splitlines()
        return result.stdout
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)

def send_discord_message(subdomain, program, state, args):

    if state == "http_title":
        message = f"""
😯 {program}
🌐 {subdomain}
💬 HTTP Title, From `{str(args[0])}` To `{str(args[1])}`
⏰ {current_time()}"""
    
    if state == "http_status_code":
        message = f"""
😵 {program}
🌐 {subdomain}
💬 HTTP Status Code, From `{args[0]}` To `{args[1]}`
⏰ {current_time()}"""

    if state == "http_favicon":
        message = f"""
🥴 {program}
🌐 {subdomain}
💬 HTTP Favicon, From `{args[0]}` To `{args[1]}`
⏰ {current_time()}"""

    if state == "http_fresh":
        message = f"""
🤩 {program}
🌐 {subdomain}
💬 HTTP Fresh Asset With Status Code `{args}`.
⏰ {current_time()}"""

    if state == "live_fresh":
        message = f"""
🤑 {program}
🌐 {subdomain}
💬 Live Fresh Asset Added.
⏰ {current_time()}"""
    
    if state == "nuclei_result":
        message = f"""
🆕 Title: Nuclei Result:
{args}
⏰ {current_time()}"""


    if state == "ip_http_title":
        message = f"""
🆕 Title: Change IP Http Title
😯 {program}
🌐 url: {args[2]}
💬 HTTP Title, From `{str(args[0])}` To `{str(args[1])}`
⏰ {current_time()}"""
    
    if state == "ip_http_status_code":
        message = f"""
🆕 Title: Change IP Http Status Code
😯 {program}
🌐 url: {args[2]}
💬 HTTP Status Code, From `{args[0]}` To `{args[1]}`
⏰ {current_time()}"""

    if state == "ip_http_favicon":
        message = f"""
🆕 Title: Change IP Http Favicon
😯 {program}
🌐 url: {args[2]}
💬 HTTP Favicon, From `{args[0]}` To `{args[1]}`
⏰ {current_time()}"""

    if state == "ip_http_webserver":
        message = f"""
🆕 Title: Change IP Http Web Server
😯 {program}
🌐 url: {args[2]}
💬 HTTP Web Server, From `{args[0]}` To `{args[1]}`
⏰ {current_time()}"""

    if state == "ip_http_fresh":
        message = f"""
🆕 Title: IP Http Fresh Asset
😯 {program}
🌐 url: {args[1]}
💬 IP HTTP Fresh Asset With Status Code `{args[0]}` Added.
⏰ {current_time()}"""

    command = f"echo subdomain.com | notify -mf '{message}'"
    time.sleep(1)

    run_command_in_zsh(command)
