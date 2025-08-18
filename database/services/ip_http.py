from database.models import Programs, ip_http
from utils import current_time, send_discord_message
from datetime import datetime


def upsert_ip_http(program_name, ip, port, scheme, webserver, tech, title, status_code, headers, url, favicon):

    # program = Programs.objects(scopes=scope).first()
    # program.program_name

    # already existed http service
    existing = ip_http.objects(ip=ip, port=port).first()
    if existing:

        if existing.title != title:
            # send_discord_message(f"```'{subdomain}' title has been changed from '{existing.title}' to '{title}'```")
            send_discord_message('', program_name, "ip_http_title", [str(existing.title), str(title), f"{scheme}://{ip}:{port}"])
            print(f"[{current_time()}] changes title for ip: {ip}")
            existing.title = title

        if existing.status_code != status_code:
            # send_discord_message(f"```'{subdomain}' status code has been changed from '{existing.status_code}' to '{status_code}'```")
            send_discord_message('', program_name, "ip_http_status_code", [existing.status_code, status_code, f"{scheme}://{ip}:{port}"])
            print(f"[{current_time()}] changes status code for ip: {ip}")
            existing.status_code = status_code

        
        if existing.favicon != favicon:
            # send_discord_message(f"```'{subdomain}' favhash has been changed from '{existing.favicon}' to '{favicon}'```")
            send_discord_message('', program_name, "ip_http_favicon", [existing.favicon, favicon, f"{scheme}://{ip}:{port}"])
            print(f"[{current_time()}] changes favhash for ip: {ip}")
            existing.favicon = favicon
        
        if existing.webserver != webserver:
            # send_discord_message(f"```'{subdomain}' favhash has been changed from '{existing.favicon}' to '{favicon}'```")
            send_discord_message('', program_name, "ip_http_webserver", [existing.webserver, webserver, f"{scheme}://{ip}:{port}"])
            print(f"[{current_time()}] changes Web Server for ip: {ip}")
            existing.webserver = webserver
        
        existing.ip = ip
        existing.scheme = scheme
        existing.tech = tech
        existing.headers = headers
        existing.url = url
        existing.last_update = datetime.now()
        existing.save()

    else:
        new_ip_http = ip_http(
            program_name = program_name,
            ip = ip,
            port = port,
            scheme = scheme,
            webserver = webserver,
            tech = tech,
            title = title,
            status_code = status_code,
            headers = headers,
            url = url,
            favicon = favicon,
            created_date = datetime.now(),
            last_update = datetime.now()
        )
        new_ip_http.save()

        #send_discord_message(f"```'{subdomain}' (fresh http) has been added to '{program.program_name}' program```")
        send_discord_message('', program_name, "ip_http_fresh", [status_code, f"{scheme}://{ip}:{port}"])
        print(f"[{current_time()}] Inserted new IP HTTP service: {ip}:{port}")
        
    return True