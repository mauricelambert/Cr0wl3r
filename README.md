![Cr0wl3r logo](https://mauricelambert.github.io/info/python/security/Cr0wl3r_small.png "Cr0wl3r logo")

# Cr0wl3r

## Description

This package implements a web discreet crawler to find all visible URLs on a website, this crawler can store pages (and reuse them for next crawl), scan web content for dynamic content (useful for pentest, red teaming and hacking), create a full JSON report and database to reuse the analysis, try to identify web pages, static content and assets to request only what is useful.

> The name *Cr0wl3r* is a pun with *Crawler* and *Growler* because this tool in not offensive but it's the first step to attack a web server.

## Requirements

This package require:

 - python3
 - python3 Standard Library

Optional:

 - Selenium

## Installation

### Pip

```bash
pip install Cr0wl3r 
```

### Git

```bash
git clone "https://github.com/mauricelambert/Cr0wl3r.git"
cd "Cr0wl3r"
python3 -m pip install .
```

### Wget

```bash
wget https://github.com/mauricelambert/Cr0wl3r/archive/refs/heads/main.zip
unzip main.zip
cd Cr0wl3r-main
python3 -m pip install .
```

### cURL

```bash
curl -O https://github.com/mauricelambert/Cr0wl3r/archive/refs/heads/main.zip
unzip main.zip
cd Cr0wl3r-main
python3 -m pip install .
```

## Usages

### Command lines

```bash
# Python executable
python3 Cr0wl3r.pyz -h
# or
chmod u+x Cr0wl3r.pyz
./Cr0wl3r.pyz --help

# Python module
python3 -m Cr0wl3r https://github.com/mauricelambert

# Entry point (console)
Cr0wl3r -F report.json -L DEBUG -l logs.log -R -S -d -c "mycookie=foobar" -H "User-Agent:Chrome" -m 3 -t "p" -r https://github.com/mauricelambert
Cr0wl3r -R -S -C -d -u -i -F report.json -L DEBUG -l logs.log -c "mycookie=foobar" "session=abc" -c "counter=5" -H "User-Agent:Chrome" "Api-Key:myapikey" -H "Authorization:Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==" -m 5 -t "p" "img" -t "link" -I 3.5 -f "raw-url-only" -D4 "text/html" -q -r https://github.com/mauricelambert
```

### Python script

```python
from Cr0wl3r import CrawlerRawPrinter

CrawlerRawPrinter(
    "https://github.com/mauricelambert",
    recursive=False,
).crawl()
```

```python
from ssl import _create_unverified_context
from Cr0wl3r import _Crawler, reports
from logging import basicConfig
from typing import Union

basicConfig(level=1)

class CustomCr0wl3r(_Crawler):
    def handle_web_page(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:

        print("[+] New web page:", url, "from", from_url, f"{tag}<{attribute}>")
        print("[*] There are still", len(self.urls_to_parse), "requests to send.")

    def handle_static(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:

        print("[+] New static:", url, "from", from_url, f"{tag}<{attribute}>")
        print("[*] There are still", len(self.urls_to_parse), "requests to send.")

    def handle_resource(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:

        print("[+] New assets:", url, "from", from_url, f"{tag}<{attribute}>")
        print("[*] There are still", len(self.urls_to_parse), "requests to send.")

cr0wl3r = CustomCr0wl3r(
    "https://github.com/mauricelambert",
    recursive=True,
    update=True,
    max_request=10,
    only_domain=False,
    headers={"User-Agent": "Chrome", "Cookie": "mycookie=abc"},
    robots=False,
    sitemap=False,
    crossdomain=False,
    context=_create_unverified_context(),
    interval=3.5,
    download_policy="do not download",
    no_query_page=False,
)
cr0wl3r.crawl()

with open("urls.txt", 'w') as report:
    [report.write(url + '\n') for url in reports]
```

## Links

 - [Github Page](https://github.com/mauricelambert/Cr0wl3r)
 - [Pypi](https://pypi.org/project/Cr0wl3r/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/Cr0wl3r.html)
 - [Python Executable](https://mauricelambert.github.io/info/python/security/Cr0wl3r.pyz)
 - [Windows Python Executable](https://mauricelambert.github.io/info/python/security/Cr0wl3r.exe)

## Help

```text
~# Cr0wl3r --help
usage: Cr0wl3r [-h] [--recursive] [--update] [--insecure] [--do-not-request-robots] [--do-not-request-sitemap] [--do-not-request-crossdomain] [--not-only-domain] [--max-request MAX_REQUEST] [--cookies COOKIES [COOKIES ...]]
               [--headers HEADERS [HEADERS ...]] [--dynamic-tags-counter DYNAMIC_TAGS_COUNTER [DYNAMIC_TAGS_COUNTER ...]] [--report-filename REPORT_FILENAME] [--loglevel {DEBUG,INFO,REQUEST,WARNING,ERROR,CRITICAL}] [--logfile LOGFILE]
               [--interval-request INTERVAL_REQUEST] [--output-format {raw-url-only,colored,raw}] [--no-query-page]
               [--download-all | --download-html | --download-static | --download-resources | --download-by-content-type DOWNLOAD_BY_CONTENT_TYPE | --download-requested | --do-not-download]
               url

This script crawls web site and prints URLs.

positional arguments:
  url                   First URL to crawl.

options:
  -h, --help            show this help message and exit
  --recursive, -r       Crawl URLs recursively.
  --update, -u          Re-downloads and overwrites responses from requests made during previous crawls.
  --insecure, -i        Use insecure SSL (support selenium and urllib)
  --do-not-request-robots, --no-robots, -R
                        Don't search, request and parse robots.txt
  --do-not-request-sitemap, --no-sitemap, -S
                        Don't search, request and parse sitemap.xml
  --do-not-request-crossdomain, --no-crossdomain, -C
                        Don't search, request and parse crossdomain.xml
  --not-only-domain, -d
                        Do not request only the base URL domain (request all domains).
  --max-request MAX_REQUEST, -m MAX_REQUEST
                        Maximum request to perform.
  --cookies COOKIES [COOKIES ...], -c COOKIES [COOKIES ...]
                        Add a cookie.
  --headers HEADERS [HEADERS ...], -H HEADERS [HEADERS ...]
                        Add headers.
  --dynamic-tags-counter DYNAMIC_TAGS_COUNTER [DYNAMIC_TAGS_COUNTER ...], --tags-counter DYNAMIC_TAGS_COUNTER [DYNAMIC_TAGS_COUNTER ...], --tags DYNAMIC_TAGS_COUNTER [DYNAMIC_TAGS_COUNTER ...], -t DYNAMIC_TAGS_COUNTER [DYNAMIC_TAGS_COUNTER ...]
                        Add a tag counter for scoring.
  --report-filename REPORT_FILENAME, --report REPORT_FILENAME, -F REPORT_FILENAME
                        The JSON report filename.
  --loglevel {DEBUG,INFO,REQUEST,WARNING,ERROR,CRITICAL}, -L {DEBUG,INFO,REQUEST,WARNING,ERROR,CRITICAL}
                        WebCrawler logs level.
  --logfile LOGFILE, -l LOGFILE
                        WebCrawler logs file.
  --interval-request INTERVAL_REQUEST, --interval INTERVAL_REQUEST, -I INTERVAL_REQUEST
                        Interval between each requests by domain.
  --output-format {raw-url-only,colored,raw}, --format {raw-url-only,colored,raw}, -f {raw-url-only,colored,raw}
                        Output format.
  --no-query-page, --no-query, -q
                        Request only when path is different, without this option the same path will be requested for each differents queries.
  --download-all, --download, -D, -D0
                        Download (store) all responses
  --download-html, --dh, -D1
                        Download (store) only HTML responses
  --download-static, --ds, -D2
                        Download (store) only static files (HTML, CSS, JavaScript)
  --download-resources, --dr, -D3
                        Download (store) only resources files (images, documents, icon...)
  --download-by-content-type DOWNLOAD_BY_CONTENT_TYPE, --dct DOWNLOAD_BY_CONTENT_TYPE, -D4 DOWNLOAD_BY_CONTENT_TYPE
                        Download (store) only responses with Content-Type that contains this value
  --download-requested, --dR, -D5
                        Download all requests responses and try to requests only Web page
  --do-not-download, --dN, -D6
                        Try to requests only Web page and do not download

~# 
```

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
