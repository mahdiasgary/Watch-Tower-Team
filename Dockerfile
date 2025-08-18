FROM python:3.11-slim

# نصب ابزارهای سیستم
RUN apt-get update && apt-get install -y \
    build-essential \
    crunch \
    libssl-dev \
    libffi-dev \
    python3-dev \
    git \
    curl \
    wget \
    unzip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# نصب Go
ENV GO_VERSION 1.24.1
RUN wget https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz && \
    rm go${GO_VERSION}.linux-amd64.tar.gz
ENV GOPATH=/root/go
ENV PATH="/usr/local/go/bin:$GOPATH/bin:$PATH"

# نصب ابزارهای Go
RUN go install github.com/tomnomnom/waybackurls@latest && \
    go install github.com/projectdiscovery/httpx/cmd/httpx@latest && \
    go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest && \
    go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && \
    go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest && \
    go install github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest && \
    go install github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest && \
    go install github.com/ImAyrix/fallparams@latest && \
    go install github.com/iangcarroll/cookiemonster/cmd/cookiemonster@latest && \
    go install github.com/tomnomnom/anew@latest && \
    go install github.com/ffuf/ffuf/v2@latest && \
    go install github.com/ImAyrix/cut-cdn@latest && \
    go install github.com/lc/gau/v2/cmd/gau@latest && \
    go install github.com/tomnomnom/unfurl@latest && \
    go install github.com/projectdiscovery/notify/cmd/notify@latest

# نصب massdns
RUN git clone https://github.com/blechschmidt/massdns.git /opt/massdns && \
    make -C /opt/massdns && \
    cp /opt/massdns/bin/massdns /usr/local/bin/

# نصب dnsgen
RUN pip install --no-cache-dir dnsgen

# اضافه کردن پروژه
WORKDIR /app
COPY . /app

# نصب کتابخانه‌های پایتون
RUN pip install --no-cache-dir -r requirements.txt
