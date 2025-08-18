# Watchtower
welcome to my watchtower :)

## Setup The Watch
1. inside the database folder run `docker compose up -d`
2. modify the config/.env file
3. install requirements
```bash
pip3 install -r requirements.txt
```
if you get error for not having virtualenv you can install them one by one with
```bash
sudo apt update
sudo apt install libpq-dev
pip install psycopg2-binary
sudo apt install zsh
sudo apt install unzip
sudo apt install jq
pip insatll fastapi
pip install uvicorn
sudo apt-get install crunch
```
4. configure zsh alias variables
## Install Tools
1. install go `https://go.dev/doc/install`
2. install subfinder 
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
3. install dnsx 
```bash
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```
4. install gau
```bash
go install github.com/lc/gau/v2/cmd/gau@latest
```
5. install httpx 
```bash 
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```
6. install nuclei 
```bash
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```
7. install waybackurls 
```bash
go install github.com/tomnomnom/waybackurls@latest
```
8. install cut-cdn 
```bash
go install github.com/ImAyrix/cut-cdn@latest
```
9. install unfurl 
```bash
go install github.com/tomnomnom/unfurl@latest
```
10. install notify 
```bash
go install -v github.com/projectdiscovery/notify/cmd/notify@latest
```
11. install mapcidr
```bash
go install -v github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest
```
12. install massdns
```bash
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
cd bin
sudo cp massdns /bin
```
13. install dnsgen
```bash
python3 -m pip install dnsgen
```
14. install unfurl
```bash
go install github.com/tomnomnom/unfurl@latest
```

## Zshrc Configurations
1. add following lines to your `~/.zshrc` file:
  ```bash
  export WATCH="~/watch_narutow"
  alias watch_sync_programs="$WATCH/programs/watch_sync_programs.py"
  alias watch_sync_chaos="$WATCH/chaos/watch_sync_chaos.py"
  alias watch_subfinder="$WATCH/enum/watch_subfinder.py"
  alias watch_crtsh="$WATCH/enum/watch_crtsh.py"
  alias watch_abuseipdb="$WATCH/enum/watch_abuseipdb.py"
  alias watch_chaos="$WATCH/enum/watch_chaos.py"
  alias watch_wayback="$WATCH/enum/watch_wayback.py"
  alias watch_gau="$WATCH/enum/watch_gau.py"
  alias watch_enum_all="$WATCH/enum/watch_enum_all.py"
  alias watch_ns="$WATCH/ns/watch_ns.py"
  alias watch_ns_static_brute="$WATCH/ns/watch_ns_static_brute.py"
  alias watch_ns_dynamic_brute="$WATCH/ns/watch_ns_dynamic_brute.py"
  alias watch_ns_all="$WATCH/ns/watch_ns_all.py"
  alias watch_http="$WATCH/http/watch_http.py"
  alias watch_http_all="$WATCH/http/watch_http_all.py"
  alias watch_nuclei="$WATCH/nuclei/watch_nuclei.py"
  alias watch_nuclei_all="$WATCH/nuclei/watch_nuclei_all.py"
  ```
2. add the following function to zshrc:
  ```bash
  asn_prefixes (){
      input=""
      while read line
      do
          curl -s https://api.bgpview.io/asn/AS$line/prefixes | jq -r ".data.ipv4_prefixes.[].prefix"
      done < "${1:-/dev/stdin}"
  }
  ```

5. you need to add your resolvers in  ~/.resolvers

6. do the following commands for start:
```bash
watch_sync_programs
watch_sync_chaos
watch_enum_all
watch_ns_all
watch_http_all
watch_nuclei_all
```
7. run with this command:
```bash
python3 app.py
```
8. put watch.sh in cronjob
