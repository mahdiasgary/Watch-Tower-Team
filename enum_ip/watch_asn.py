#!/usr/bin/env python3
import sys, os, json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.selectors import get_all_programs, get_program_by_program_name
from database.services import upsert_ip_http
from utils import current_time
from tools import IP_httpx


if __name__ == "__main__":
    
    program_name = sys.argv[1] if len(sys.argv) > 1 else False

    if program_name is False:
        print(f"Usage: watch_http \"program_name\"")
        sys.exit()
    
    program = get_program_by_program_name(program_name)
    
    if isinstance(program, str):
        print("Program name not found!!!")
        print(program)
        sys.exit()

    obj_program = program

    if obj_program:
        print(f"[{current_time()}] running HTTPx module for {obj_program.program_name} ASN's ")

        all_result = IP_httpx(obj_program.asns)
        
        print(f"[{current_time()}] get result from HTTPx module was successfully")
        
        for items in all_result:
            if len(items) > 0:
                for item in items:
                    ip_http = {
                        "program_name": obj_program.program_name,
                        "ip": item['host'] if 'host' in item else '',
                        "port": item['port'] if 'port' in item else '',
                        "scheme": item['scheme'] if 'scheme' in item else '',
                        "webserver": item['webserver'] if 'webserver' in item else '',
                        "tech": item['tech'] if 'tech' in item else [],
                        "title": item['title'] if 'title' in item else '',
                        "status_code": str(item['status_code'] if 'status_code' in item else ''),
                        "headers": item['header'] if 'header' in item else {},
                        "url": item['url'] if 'url' in item else '',
                        "favicon": item['favicon'] if 'favicon' in item else '',
                    }  
                    upsert_ip_http(**ip_http)