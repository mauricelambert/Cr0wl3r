#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module implements a crawler to find all links and resources
on the target web site.

~# python3 Cr0wl3r.py https://github.com/mauricelambert
form action https://github.com/settings/blocked_users
a href https://docs.github.com/en/articles/blocking-a-user-from-your-personal-account
a href https://docs.github.com/en/articles/reporting-abuse-or-spam
a href https://github.com/contact/report-abuse?report=mauricelambert+%28user%29
a href https://github.com/mauricelambert/WebScripts
a href https://github.com/mauricelambert/WebScripts/stargazers
a href https://github.com/mauricelambert/WebScripts/forks
a href https://github.com/mauricelambert/SpyWare
a href https://github.com/mauricelambert/SpyWare/stargazers
a href https://github.com/mauricelambert/SpyWare/forks
a href https://github.com/mauricelambert/CVE-2022-21907
a href https://github.com/mauricelambert/CVE-2022-21907/stargazers
a href https://github.com/mauricelambert/CVE-2022-21907/forks
a href https://github.com/mauricelambert/Vulnerability1-XSS-title
a href https://github.com/mauricelambert/CLEF
a href https://github.com/mauricelambert/FastRC4
a href https://docs.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile
a href https://github.com/mauricelambert?tab=overview&from=2023-05-01&to=2023-05-19
a href https://github.com/mauricelambert?tab=overview&from=2022-12-01&to=2022-12-31
a href https://github.com/mauricelambert?tab=overview&from=2021-12-01&to=2021-12-31
a href https://github.com/mauricelambert?tab=overview&from=2020-12-01&to=2020-12-31
a href https://github.com/mauricelambert?tab=overview&from=2019-12-01&to=2019-12-31
a href https://github.com/mauricelambert/FastRC4/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/mauricelambert.github.io
a href https://github.com/mauricelambert/mauricelambert.github.io/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/EicarSpam
a href https://github.com/mauricelambert/EicarSpam/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/SIDAnalyzer
a href https://github.com/mauricelambert/SIDAnalyzer/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/ProgramExecutableAnalyzer
a href https://github.com/mauricelambert/ProgramExecutableAnalyzer/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/ReverseShell
a href https://github.com/mauricelambert/ReverseShell/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/p0dalirius/pyLAPS
a href https://github.com/p0dalirius/pyLAPS/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/PythonToolsKit
a href https://github.com/mauricelambert/PythonToolsKit/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/NetworkScanner
a href https://github.com/mauricelambert/NetworkScanner/commits?author=mauricelambert&since=2023-05-01&until=2023-05-20
a href https://github.com/mauricelambert/pyLAPS
a href https://github.com/mauricelambert?tab=overview&from=2023-05-01&to=2023-05-31
a href https://github.com/p0dalirius/pyLAPS/pull/1
a href https://github.com/mauricelambert/ReverseShell/issues/8
a href https://github.com/mauricelambert/ReverseShell/issues/7
a href https://github.com/mauricelambert/ReverseShell/issues/6
a href https://github.com/mauricelambert/ReverseShell/issues/5
a href https://github.com/mauricelambert/ReverseShell/issues/4
a href https://github.com/mauricelambert/ReverseShell/issues/3
a href https://github.com/mauricelambert/ReverseShell/issues/2
a href https://github.com/mauricelambert/ReverseShell/issues/1
... (160 lines)
~# python3 Cr0wl3r.py -F test.json -l DEBUG -f test.log -R -S -d -c "test=test" -H "User-Agent:Chrome" -m 3 -t p -r https://github.com/mauricelambert
link href https://github.githubassets.com
link href https://avatars.githubusercontent.com
link href https://github-cloud.s3.amazonaws.com
link href https://user-images.githubusercontent.com/
link href https://github.githubassets.com/assets/light-0946cdc16f15.css
link href https://github.githubassets.com/assets/dark-3946c959759a.css
link href https://github.githubassets.com/assets/primer-primitives-fb1d51d1ef66.css
link href https://github.githubassets.com/assets/primer-57c312e484b2.css
link href https://github.githubassets.com/assets/global-0d04dfcdc794.css
link href https://github.githubassets.com/assets/github-c7a3a0ac71d4.css
link href https://github.githubassets.com/assets/profile-39867166a585.css
script src https://github.githubassets.com/assets/wp-runtime-377d421cc9f7.js
script src https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-ae93d3fba59c.js
script src https://github.githubassets.com/assets/ui_packages_failbot_failbot_ts-e38c93eab86e.js
script src https://github.githubassets.com/assets/environment-de3997b81651.js
... (385 lines)
~# 
"""

###################
#    This module implements a crawler to find all links and resources
#    on the target web site.
#    Copyright (C) 2023  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This module implements a crawler to find all links and resources
on the target web site.
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/Cr0wl3r"

copyright = """
Cr0wl3r  Copyright (C) 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["_Crawler", "CrawlerPrinter", "main", "CriticalUrllibError", "ContentTypeError"]

print(copyright)

from logging import basicConfig, debug, info, warning, error, critical
from typing import Union, Set, List, Dict, Tuple, TypeVar
from http.client import HTTPResponse, IncompleteRead
from argparse import ArgumentParser, Namespace
from urllib.parse import urlparse, ParseResult
from urllib.error import URLError, HTTPError
from collections import defaultdict, Counter
from urllib.request import urlopen, Request
from xml.etree.ElementTree import parse
from abc import ABC, abstractmethod
from html.parser import HTMLParser
from dataclasses import dataclass
from datetime import datetime
from sys import exit, stderr
from functools import cache
from time import sleep
from json import dump
import logging

try:
    from selenium.webdriver import Chrome, ChromeOptions
except ImportError:
    selenium = False
else:
    selenium = True
    if __name__ == "__main__":
        driver = None
    else:
        driver = Chrome()

_Crawler = TypeVar("_Crawler")

# https://www.w3.org/TR/REC-html40/index/attributes.html
# https://stackoverflow.com/questions/2725156/complete-list-of-html-tag-attributes-which-have-a-url-value
# https://html.spec.whatwg.org/multipage/indices.html#attributes-1

url_attributes: List[str] = [
    "src",
    "icon",
    "href",
    "cite",
    "code",
    "data",
    "action",
    "usemap",
    "poster",
    "srcset",
    "itemid",
    "srcdoc",
    "profile",
    "archive",
    "codebase",
    "longdesc",
    "manifest",
    "formaction",
]

interaction_tags: Dict[str, int] = {
    "textarea": 3,
    "select": 2,
    "button": 1,
    "script": 1,
    "input": 1,
    "form": 5,
}

input_types: Dict[str, int] = {
    "datetime-local": 1,
    "password": 1,
    "hidden": 1,
    "search": 2,
    "number": 1,
    "email": 1,
    "radio": 1,
    "color": 1,
    "month": 1,
    "week": 1,
    "date": 1,
    "file": 2,
    "text": 2,
    "url": 1,
    "tel": 1,
}

counters: Dict[str, Dict[str, int]] = defaultdict(Counter)


@dataclass
class HttpResponse:

    """
    This class is used with selenium to have same api as HTTPResponse.
    """

    code: int
    url: str
    headers: List[Tuple[str, str]]
    response: bytes
    readed: bool = False

    def read(self) -> bytes:
        return self.response

    def getcode(self) -> int:
        if self.readed:
            return None
        return self.code

    def getheader(self, header: str, default: str = None) -> str:
        try:
            return [
                x for y, x in self.headers if y.casefold() == header.casefold()
            ][0]
        except IndexError:
            return default

    def getheaders(self) -> List[Tuple[str, str]]:
        return self.headers


class ContentTypeError(ValueError):

    """
    Exception raised when the Content-Type
    is not valid for web page.
    """

    pass


class CriticalUrllibError(Exception):

    """
    Exception raised after urllib exception
    when is critical.
    """

    pass


class UrlGetter(HTMLParser):

    """
    This class analyzes HTML web page to found URLs.
    """

    def __init__(self, crawler: _Crawler):
        super().__init__()
        self.crawler = crawler

    def handle_starttag(
        self, tag: str, attributes: List[Tuple[str, str]]
    ) -> None:
        """
        This function get URLs attributes and values.
        """

        debug("Start new tag: " + tag)
        if tag in interaction_tags:
            info("Get a new interactive tag: " + tag)
            counters[self.crawler.current_url][tag] += interaction_tags[tag]
            type_ = tuple(x for x, _ in attributes if x == "type")
            if tag == "input" and type_ and type_ in input_types:
                counters[self.crawler.current_url][tag] += input_types[type_]

        for attribute, url in attributes:
            debug("Get new attribute: " + attribute + " = " + str(url))
            if (
                url
                and not url.strip().startswith("data:")
                and not url.strip().startswith("javascript:")
                and attribute in url_attributes
            ):
                info("Get new URL: " + url)
                url = self.crawler.get_complete_url(urlparse(url))
                self.crawler._handle(url, tag, attribute)
                self.crawler.add(urlparse(url))


class _Crawler(ABC):

    """
    This class crawls a web page to get URLs and resources paths.
    """

    def __init__(
        self,
        url: str,
        recursive: bool = True,
        max_request: int = None,
        only_domain: bool = True,
        headers: Dict[str, str] = {},
        robots: bool = True,
        sitemap: bool = True,
    ):
        self.counter = 1
        self.robots = robots
        self.sitemap = sitemap
        self.headers = headers
        self.html: bytes = None
        self.recursive = recursive
        self.current_url: str = None
        self.max_request = max_request
        self.only_domain = only_domain
        self.urls_parsed: List[str] = []
        urls_to_parse = self.urls_to_parse = {url}
        self.master_url: ParseResult = urlparse(url)
        self.html_parser: UrlGetter = UrlGetter(self)
        self.urls_getted: Set[str] = urls_to_parse.copy()

    def add(self, url: ParseResult) -> None:
        """
        This method adds an URL if not already added.
        """

        if self.only_domain and self.master_url.netloc not in url.netloc:
            self.urls_getted.add(url.geturl())
            return None

        url = url.geturl()
        if url not in self.urls_getted:
            self.urls_getted.add(url)
            self.urls_to_parse.add(url)

    def decode(self, data: bytes) -> str:
        """
        This method try to decode data using utf-8 and latin-1.
        """

        try:
            return data.decode()
        except UnicodeDecodeError:
            return data.decode("latin-1")

    @abstractmethod
    def handle(self, url: str, *sources: str) -> None:
        pass

    @cache
    def _handle(self, url: str, *sources: str) -> None:
        """
        This method calls handle method.
        """

        self.handle(url, *sources)

    def reader(self, response: HTTPResponse) -> bytes:
        """
        This method excepts the IncompleteRead error.
        """

        try:
            return response.read()
        except IncompleteRead as e:
            warning(
                "IncompleteRead exception: "
                + e.__class__.__name__
                + " "
                + str(e)
            )
            return e.partial

    @cache
    def ask_sitemap(self, url: ParseResult) -> None:
        """
        This method send request for robots.txt.
        """

        url = ParseResult(
            url.scheme,
            url.netloc,
            (url.path + "sitemap.xml")
            if url.path and url.path[-1] == "/"
            else (url.path + "/sitemap.xml"),
            url.params,
            url.query,
            url.fragment,
        )
        response = self.get_data(url)

        if not response or (
            "text/plain" not in response.getheader("Content-Type")
            and "text/xml" not in response.getheader("Content-Type")
        ):
            return None

        info("Get a new sitemap.xml")
        self._handle(url.geturl(), "sitemap")
        self.parse_sitemap(response)

    def parse_sitemap(self, data: Union[HTTPResponse, str]) -> None:
        """
        This method requests a sitemap URL and/or parse it.
        """

        if isinstance(data, str):
            data = self.get_data(data)
            if data is None:
                return None

        debug("Parse a new sitemap.")
        if "text/xml" in data.getheader("Content-Type", ""):
            root = parse(data).getroot()
            for element_ in root:
                for element in element_:
                    if element.tag == "loc":
                        url = self.get_complete_url(urlparse(element.text))
                        info("Get an URL in sitemap: " + url)
                        self._handle(url, "sitemap.xml", "sitemap")
                        if element_.tag == "sitemap":
                            info("Get a sitemap in sitemap.xml")
                            self.parse_sitemap(url)
        elif "text/plain" in data.getheader("Content-Type"):
            levels = {}
            for line in data:
                url = self.decode(line).strip()
                level = len(line) - len(url)
                levels[level] = url
                url = self.get_complete_url(
                    urlparse(
                        "".join(levels[x] for x in levels if x < level) + url
                    )
                )
                info("Get an URL in sitemap.txt: " + url)
                self._handle(url, "sitemap.txt")

    @cache
    def ask_robots(self, url: ParseResult) -> None:
        """
        This method send request for robots.txt.
        """

        url = ParseResult(
            url.scheme,
            url.netloc,
            (url.path + "robots.txt")
            if url.path and url.path[-1] == "/"
            else (url.path + "/robots.txt"),
            url.params,
            url.query,
            url.fragment,
        )
        response = self.get_data(url)

        if not response or "text/plain" not in response.getheader(
            "Content-Type"
        ):
            return None

        info("Get a new robots.txt")
        lines = self.reader(response).splitlines()
        self._handle(url.geturl(), "robots.txt")

        for line in lines:
            line = self.decode(line)
            startswith = line.strip().casefold().startswith
            if startswith("#") or startswith("user-agent"):
                debug("Get a new comment in robots.txt")
                continue
            if startswith("allow") or startswith("disallow"):
                if ":" in line:
                    info("Get a URL in robots.txt")
                    url = line.split(":", 1)[1].strip()
                    url = self.get_complete_url(urlparse(url))
                    self.add(urlparse(url))
                    self._handle(url, "robots.txt")
                    continue
            if startswith("sitemap"):
                if ":" in line:
                    info("Get a sitemap in robots.txt")
                    url = line.split(":", 1)[1].strip()
                    url = self.get_complete_url(urlparse(url))
                    self._handle(url, "robots.txt", "sitemap")
                    if self.sitemap:
                        self.parse_sitemap(url)
                    continue

            warning("Invalid line in robots.txt: " + line)

    def crawl(self) -> None:
        """
        This function starts crawler.
        """

        first = True
        urls = self.urls_to_parse
        urls_done = self.urls_parsed

        while urls:
            url = urls.pop()
            urls_done.append(url)

            parsed_url = urlparse(url)
            response = self.get_data(parsed_url)
            if response is None and not first:
                warning(
                    "An error occurs on the request, URL is probably wrong: "
                    + url
                )
                continue
            elif response is None and first:
                message = (
                    "An error occurs on the first request, "
                    "URL is probably wrong: " + url
                )
                critical(message)
                raise CriticalUrllibError(message)

            is_html = "text/html" in response.getheader("Content-Type")
            data = self.reader(response)

            if is_html:
                self.html_parser.feed(self.decode(data))
                first = False
            elif first and not is_html:
                message = (
                    f"Response for {url} cannot be parsed and "
                    "is not valid in this context."
                )
                critical(message)
                raise ContentTypeError(message)

            if not self.recursive:
                return None

            if self.robots:
                self.ask_robots(parsed_url)

            if self.sitemap:
                self.ask_sitemap(parsed_url)

    def add_domain_new_url(self, url: str) -> None:
        """
        This function add new url to parse.
        """

        url_parsed = urlparse(url)

        if (
            (
                url_parsed.netloc == self.master_url.netloc
                or url_parsed.netloc == ""
            )
            and url_parsed.path not in self.urls_to_parse
            and url_parsed.path not in self.urls_parsed
        ):
            self.urls_to_parse.append(url_parsed.path)

    def get_complete_url(self, url: ParseResult) -> str:
        """
        This function build a complete url.
        """

        if url.scheme:
            return url.geturl()

        if url.path and url.path[0] == "/":
            return ParseResult(
                self.master_url.scheme,
                self.master_url.netloc,
                url.path,
                url.params,
                url.query,
                url.fragment,
            ).geturl()

        return ParseResult(
            self.master_url.scheme,
            self.master_url.netloc,
            (self.master_url.path + url.path)
            if self.master_url.path and self.master_url.path[-1] == "/"
            else (self.master_url.path + "/" + url.path),
            url.params,
            url.query,
            url.fragment,
        ).geturl()

    @cache
    def get_data(self, url: ParseResult) -> HTTPResponse:
        """
        This function sends the HTTP request
        and returns the HTTP response.
        """

        if self.max_request and self.max_request < self.counter:
            return None

        self.counter += 1

        url: str = self.get_complete_url(url)
        self.current_url = url
        counters[url]

        try:
            response = urlopen(Request(url, headers=self.headers))
        except (URLError, HTTPError) as error_:
            if getattr(error_, "code", None):
                warning(f"HTTP {error_.code} error." + url)
                return error_
            else:
                error("Could not request: " + str(error_) + " " + url)
                return None

        info("Get ressources from this URL: " + url)
        return response


class CrawlerPrinter(_Crawler):
    def handle(self, url: str, *sources: str) -> None:
        """
        This method prints the URL found.
        """

        print(*sources, url)


if selenium:

    class CrawlerPrinter(CrawlerPrinter):
        @cache
        def get_data(self, url: ParseResult) -> HttpResponse:
            response = super().get_data(url)
            if not response:
                return response

            url = response.geturl()

            driver.get(url)
            precedent_length = len(driver.page_source)
            sleep(0.5)

            while len(driver.page_source) != precedent_length:
                precedent_length = len(driver.page_source)
                sleep(0.5)

            if script := getattr(self, "script", None):
                driver.execute_script(script)

            return HttpResponse(
                response.getcode(),
                url,
                response.getheaders(),
                driver.page_source.encode(),
            )


def parse_args() -> Namespace:
    """
    This function parses the command line arguments.
    """

    parser = ArgumentParser(
        description="This script crawls web site and prints URLs."
    )
    add = parser.add_argument
    add(
        "url",
        help="First URL to crawl.",
    )
    add(
        "--recursive",
        "-r",
        action="store_true",
        help="Crawl URLs recursively.",
    )
    add(
        "--do-not-request-robots",
        "--no-robots",
        "-R",
        default=False,
        action="store_true",
        help="Don't search, request and parse robots.txt",
    )
    add(
        "--do-not-request-sitemap",
        "--no-sitemap",
        "-S",
        default=False,
        action="store_true",
        help="Don't search, request and parse sitemap.xml",
    )
    add(
        "--not-only-domain",
        "-d",
        default=False,
        action="store_true",
        help=(
            "Do not request only the base URL" " domain (request all domains)."
        ),
    )
    add(
        "--max-request",
        "-m",
        type=int,
        help="Maximum request to perform.",
    )
    add(
        "--cookie",
        "-c",
        help="Add a cookie.",
    )
    add(
        "--headers",
        "-H",
        help="Add headers.",
        action="extend",
        nargs="+",
    )
    add(
        "--tags-counter",
        "--tags",
        "-t",
        help="Add a tag counter for scoring.",
        action="extend",
        nargs="+",
    )
    add(
        "--report-filename",
        "--report",
        "-F",
        default="CrawlerReport_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".json",
        help="The JSON report filename.",
    )
    add(
        "--loglevel",
        "-l",
        help="WebSiteCloner logs level.",
        default="WARNING",
        choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"},
    )
    add(
        "--logfile",
        "-f",
        help="WebCrawler logs file.",
    )

    if selenium:
        add(
            "--no-gui",
            "-g",
            action="store_true",
            help=(
                "Don't use GUI for selenium, sometime"
                " Web Page doesn't respond correctly."
            ),
        )
        add(
            "--script",
            "-s",
            help=(
                "A javascript script you want to run on the page, to "
                "wait a specific element created by javascript."
            ),
        )

    return parser.parse_args()


def main() -> int:
    """
    This function starts the script from the command line.
    """

    arguments = parse_args()

    basicConfig(
        format="[%(asctime)s] %(levelname)s (%(levelno)d): %(message)s",
        datefmt="%Y-%d-%m %H:%M:%S",
        level=getattr(logging, arguments.loglevel),
        filename=arguments.logfile,
    )

    if arguments.tags_counter:
        interaction_tags.update({x: 1 for x in arguments.tags_counter})

    if arguments.headers:
        try:
            headers = dict((x.split(":", 1) for x in arguments.headers))
        except ValueError:
            error(
                "Value error in headers, headers must be in this format:"
                " Header-Name:Value"
            )
    else:
        headers = {}

    if arguments.cookie:
        cookies = headers.get("Cookie", "")
        if cookies:
            cookies += ";"
        cookies += ";".join(arguments.cookie)

    if selenium:
        global driver
        options = ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if arguments.no_gui:
            options.add_argument("--headless=new")
        driver = Chrome(options=options)

    copy: CrawlerPrinter = CrawlerPrinter(
        arguments.url,
        headers=headers,
        recursive=arguments.recursive,
        max_request=arguments.max_request,
        only_domain=not arguments.not_only_domain,
        robots=not arguments.do_not_request_robots,
        sitemap=not arguments.do_not_request_sitemap,
    )

    try:
        copy.crawl()
    except (ContentTypeError, CriticalUrllibError):
        print(
            "Critical exception on the first request"
            ", there is nothing to cr0wl....",
            file=stderr
        )
        critical("Critical exception on the first request.")
        return 2

    if selenium:
        driver.quit()

    dump(
        {
            k: v
            for k, v in reversed(
                sorted(counters.items(), key=lambda x: x[1].total())
            )
        },
        open(arguments.report_filename, "w"),
    )

    return 0


if __name__ == "__main__":
    exit(main())
