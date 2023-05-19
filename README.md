![Cr0wl3r logo](https://mauricelambert.github.io/info/python/security/Cr0wl3r_small.png "Cr0wl3r logo")

# Cr0wl3r

## Description

This package implements a web crawler to find all visible URLs in the page and sort URL by dynamic content (useful for pentest and hacking).

## Requirements

This package require: 
 - python3
 - python3 Standard Library

Optional:
 - Selenium

## Installation

```bash
pip install Cr0wl3r 
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
Cr0wl3r -F report.json -l DEBUG -f logs.log -R -S -d -c "cookie=foobar" -H "User-Agent:Chrome" -m 3 -t p -r https://github.com/mauricelambert
```

### Python3

```python
from Cr0wl3r import CrawlerPrinter
from logging import basicConfig

basicConfig(level=1)

cr0wl3r = CrawlerPrinter(
    "https://github.com/mauricelambert",
    recursive = False,
    max_request = None,
    only_domain = True,
    headers = {},
    robots = True,
    sitemap = True,
)
cr0wl3r.crawl()
```

```python
from Cr0wl3r import _Crawler

class CustomCr0wl3r(_Crawler):
    def handle(self, url: str, *sources: str) -> None:
        print("[+] New url:", url, "from", *sources)
        print("[*] Getted in", self.urls_parsed[-1])
        print("[*] There are still", len(self.urls_to_parse), "requests to send.")

cr0wl3r = CustomCr0wl3r("https://github.com/mauricelambert", recursive=False)
cr0wl3r.crawl()
with open("urls.txt", 'w') as report:
    [report.write(url + '\n') for url in cr0wl3r.urls_getted]
```

## Links

 - [Github Page](https://github.com/mauricelambert/Cr0wl3r)
 - [Pypi](https://pypi.org/project/Cr0wl3r/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/Cr0wl3r.html)
 - [Executable](https://mauricelambert.github.io/info/python/security/Cr0wl3r.pyz)

## Help

```text
~# python3 Cr0wl3r.py -h
usage: Cr0wl3r.py [-h] [--recursive] [--do-not-request-robots] [--do-not-request-sitemap] [--not-only-domain] [--max-request MAX_REQUEST]
                  [--cookie COOKIE] [--headers HEADERS [HEADERS ...]] [--tags-counter TAGS_COUNTER [TAGS_COUNTER ...]] [--report-filename REPORT_FILENAME]
                  [--loglevel {DEBUG,ERROR,CRITICAL,WARNING,INFO}] [--logfile LOGFILE] [--no-gui] [--script SCRIPT]
                  url

This script crawls web site and prints URLs.

positional arguments:
  url                   First URL to crawl.

options:
  -h, --help            show this help message and exit
  --recursive, -r       Crawl URLs recursively.
  --do-not-request-robots, --no-robots, -R
                        Don't search, request and parse robots.txt
  --do-not-request-sitemap, --no-sitemap, -S
                        Don't search, request and parse sitemap.xml
  --not-only-domain, -d
                        Do not request only the base URL domain (request all domains).
  --max-request MAX_REQUEST, -m MAX_REQUEST
                        Maximum request to perform.
  --cookie COOKIE, -c COOKIE
                        Add a cookie.
  --headers HEADERS [HEADERS ...], -H HEADERS [HEADERS ...]
                        Add headers.
  --tags-counter TAGS_COUNTER [TAGS_COUNTER ...], --tags TAGS_COUNTER [TAGS_COUNTER ...], -t TAGS_COUNTER [TAGS_COUNTER ...]
                        Add a tag counter for scoring.
  --report-filename REPORT_FILENAME, --report REPORT_FILENAME, -F REPORT_FILENAME
                        The JSON report filename.
  --loglevel {DEBUG,ERROR,CRITICAL,WARNING,INFO}, -l {DEBUG,ERROR,CRITICAL,WARNING,INFO}
                        WebSiteCloner logs level.
  --logfile LOGFILE, -f LOGFILE
                        WebCrawler logs file.
  --no-gui, -g          Don't use GUI for selenium, sometime Web Page doesn't respond correctly.
  --script SCRIPT, -s SCRIPT
                        A javascript script you want to run on the page, to wait a specific element created by javascript.
~# 
```

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
