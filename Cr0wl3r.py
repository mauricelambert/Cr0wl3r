#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

__version__ = "1.0.0"
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

__all__ = [
    "_Crawler",
    "CrawlerRawPrinter",
    "CrawlerRawUrlOnlyPrinter",
    "CrawlerColoredPrinter",
    "main",
    "CriticalUrllibError",
    "ContentTypeError",
]

print(copyright)

from ssl import create_default_context, _create_unverified_context, SSLContext
from logging import basicConfig, debug, info, warning, error, critical
from typing import Union, Set, List, Dict, Tuple, TypeVar, FrozenSet
from os.path import dirname, basename, normpath, join, exists
from urllib.parse import urlparse, ParseResult, quote
from http.client import HTTPResponse, IncompleteRead
from argparse import ArgumentParser, Namespace
from urllib.error import URLError, HTTPError
from collections import defaultdict, Counter
from urllib.request import urlopen, Request
from xml.etree.ElementTree import parse
from os import name, getcwd, makedirs
from abc import ABC, abstractmethod
from html.parser import HTMLParser
from dataclasses import dataclass
from shutil import copyfileobj
from datetime import datetime
from sys import exit, stderr
from time import sleep, time
from io import BytesIO
from json import dump
import logging

try:
    filename = (
        "TerminalMessages.dll" if name == "nt" else "libTerminalMessages.so"
    )
    with open(filename, "wb") as file:
        copyfileobj(
            urlopen(
                "https://github.com/mauricelambert/Terminal"
                "Messages/releases/download/v0.0.2/" + filename
            ),
            file,
        )
    with open("TerminalMessagesInterface.py", "wb") as file:
        copyfileobj(
            urlopen(
                "https://raw.githubusercontent.com/mauricelambert/Terminal"
                "Messages/main/TerminalMessagesInterface.py"
            ),
            file,
        )
    from TerminalMessagesInterface import messagef

    format_output: bool = True
except Exception as e:
    raise e
    format_output: bool = False

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
CWD = getcwd()

# https://www.w3.org/TR/REC-html40/index/attributes.html
# https://stackoverflow.com/questions/2725156/complete-list-of-html-tag-attributes-which-have-a-url-value
# https://html.spec.whatwg.org/multipage/indices.html#attributes-1

url_attributes: FrozenSet[str] = frozenset(
    (
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
    )
)

extensions: FrozenSet[str] = {
    ".csv",
    ".doc",
    ".docm",
    ".docx",
    ".dot",
    ".dotx",
    ".exe",
    ".gif",
    ".iso",
    ".jar",
    ".mp3",
    ".jpg",
    ".jpeg",
    ".mp4",
    ".msi",
    ".pdf",
    ".png",
    ".pot",
    ".potm",
    ".potx",
    ".ppam",
    ".pps",
    ".ppsm",
    ".ppsx",
    ".ppt",
    ".pptm",
    ".pptx",
    ".rar",
    ".rtf",
    ".sldx",
    ".txt",
    ".wav",
    ".vsd",
    ".vsdm",
    ".vsdx",
    ".vss",
    ".vssm",
    ".vst",
    ".vstm",
    ".vstx",
    ".xla",
    ".xlam",
    ".xll",
    ".xlm",
    ".xls",
    ".xlsm",
    ".xlsx",
    ".xlt",
    ".xltm",
    ".xltx",
    ".xps",
    ".xml",
    ".zip",
    ".tar",
    ".bz2",
    ".gz",
    ".lz",
    ".lz4",
    ".lzma",
    ".7z",
    ".s7z",
    ".apk",
    ".tgz",
    ".tbz2",
    ".txz",
    ".tar.Z",
    ".tar.zst",
    ".txz",
    ".zipx",
    ".pkg",
    ".dmg",
    ".asc",
    ".sigstore",
    ".xz",
}

static_url_tags_attributes: FrozenSet[Tuple[str]] = frozenset(
    (
        ("script", "src"),
        ("link", "href"),
    )
)

html_url_tags_attributes: FrozenSet[Tuple[str]] = frozenset(
    (
        ("frame", "src"),
        ("iframe", "src"),
        ("a", "href"),
        ("area", "href"),
        ("blockquote", "cite"),
        ("q", "cite"),
        ("del", "cite"),
        ("ins", "cite"),
        ("form", "action"),
        ("head", "profile"),
    )
)

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


class UrlReport:
    """
    This class implements all attributes to generate an URL report.
    """

    def __init__(self, path: str = None, requested: bool = True, status: int = 200):
        self.filepath: str = path
        self.requested: bool = requested
        self.status: int = status
        self.time: float = time()
        self.urls: Counter = Counter()
        self.tags: Counter = Counter()
        self.dynamics: Counter = Counter()
        self.tags_attributes: Counter = Counter()

    def to_dict(
        self,
    ) -> Dict[str, Union[str, None, int, float, Dict[str, int]]]:
        """
        This method convert this report to dict for JSON report.
        """

        return {
            "filepath": self.filepath,
            "requested": self.requested,
            "status": self.status,
            "time": self.time,
            "urls": self.urls,
            "dynamics": self.dynamics,
            "tags": self.tags,
            "tags_attributes": self.tags_attributes,
        }


reports: Dict[str, UrlReport] = defaultdict(UrlReport)


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

    def __init__(self, url: str, report: UrlReport, crawler: _Crawler):
        super().__init__()
        self.url = url
        self.report = report
        self.crawler = crawler

    def add_interactive_tag(
        self, tag: str, attributes: List[Tuple[str, str]]
    ) -> None:
        """
        This method adds the tag dynamic score to dynamic counter.
        """

        info("Get a new interactive tag: " + tag)
        dynamics = self.report.dynamics
        dynamics[tag] += interaction_tags[tag]

        type_ = tuple(x for x, _ in attributes if x == "type")
        if tag == "input" and type_ and type_[0] in input_types:
            dynamics[tag] += input_types[type_]

    def get_add_url(self, tag: str, attribute: str, value: str) -> None:
        """
        This method adds the value if it's URL attribute.
        """

        attribute = attribute.casefold()
        self.report.tags_attributes[tag + "<" + attribute + ">"] += 1
        debug("Get new attribute: " + attribute + " = " + str(value))

        if (
            value
            and attribute in url_attributes
            and not value.strip().startswith("data:")
            and not value.strip().startswith("javascript:")
        ):
            info("Get new URL: " + value)
            url, parsed_url = self.crawler.get_complete_url(urlparse(value))

            self.crawler._handle(
                self.url,
                parsed_url,
                url,
                tag,
                attribute,
                self.get_url_type((tag, attribute)),
            )

    def get_url_type(self, tag_attribute: Tuple[str, str]) -> str:
        """
        This method returns the URL type from tag and attribute.
        """

        if tag_attribute in html_url_tags_attributes:
            return "html"
        elif tag_attribute in static_url_tags_attributes:
            return "static"
        return "resource"

    def handle_starttag(
        self, tag: str, attributes: List[Tuple[str, str]]
    ) -> None:
        """
        This function gets URLs attributes and values.
        """

        tag = tag.casefold()
        self.report.tags[tag] += 1
        debug("Start new tag: " + tag)
        if tag in interaction_tags:
            self.add_interactive_tag(tag, attributes)

        for attribute, value in attributes:
            self.get_add_url(tag, attribute, value)


class _Crawler(ABC):

    """
    This class crawls a web page to get URLs and resources paths.
    """

    def __init__(
        self,
        url: str,
        recursive: bool = True,
        update: bool = False,
        max_request: int = None,
        only_domain: bool = True,
        headers: Dict[str, str] = {},
        robots: bool = True,
        sitemap: bool = True,
        crossdomain: bool = True,
        context: SSLContext = create_default_context(),
        interval: float = 0,
        download_policy: str = None,
    ):
        self.counter = 0
        self.robots = robots
        self.update = update
        self.context = context
        self.sitemap = sitemap
        self.headers = headers
        self.html: bytes = None
        self.interval = interval
        self.recursive = recursive
        self.max_request = max_request
        self.crossdomain = crossdomain
        self.only_domain = only_domain
        self.urls_parsed: List[str] = []
        self.download_policy = download_policy
        urls_to_parse = self.urls_to_parse = {url}
        self.master_url: ParseResult = urlparse(url)
        self.urls_getted: Set[str] = urls_to_parse.copy()
        self.store = download_policy != "do not download"

    def add(self, parsed_url: ParseResult, url: str, request: bool) -> None:
        """
        This method adds an URL if not already added.
        """

        if (
            self.only_domain
            and self.master_url.netloc not in parsed_url.netloc
        ):
            self.urls_getted.add(url)
            return None

        if request and url not in self.urls_getted:
            self.urls_to_parse.add(url)

        self.urls_getted.add(url)

    def decode(self, data: bytes) -> str:
        """
        This method try to decode data using utf-8 and latin-1.
        """

        try:
            return data.decode()
        except UnicodeDecodeError:
            return data.decode("latin-1")

    @abstractmethod
    def handle_web_page(
        self, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        pass

    @abstractmethod
    def handle_static(
        self, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        pass

    @abstractmethod
    def handle_resource(
        self, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        pass

    def _handle(
        self,
        from_url: str,
        parsed_url: ParseResult,
        url: str,
        tag: str,
        attribute: str,
        type_: str,
    ) -> Union[bool, None]:
        """
        This method calls handle method.
        """

        if type_ == "resource" or any(parsed_url.path.endswith(x) for x in extensions):
            handle = self.handle_resource
            request = self.download_policy == "resources"
        elif type_ == "html":
            handle = self.handle_web_page
            request = (
                self.download_policy is None
                or self.download_policy == "text/html"
                or self.download_policy == "requested"
                or self.download_policy == "do not download"
            )
        elif type_ == "static":
            handle = self.handle_static
            request = self.download_policy == "static"
        elif type_ == "sitemap" or type_ == "robots.txt":
            self.urls_getted.add(url)
            handle = self.handle_resource
            request = False
            if type_ == "sitemap" and self.sitemap:
                self.parse_sitemap(url)

        reports[from_url].urls[url] += 1
        request = not handle(from_url, url, tag, attribute) and (
            self.download_policy == "all" or request
        )

        self.add(parsed_url, url, request)

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

    def ask_sitemap(self, url: ParseResult) -> None:
        """
        This method send request for robots.txt.
        """

        url_parsed = ParseResult(
            url.scheme, url.netloc, "/sitemap.xml", "", "", ""
        )
        url = url_parsed.geturl()
        url not in self.urls_getted and self.parse_sitemap(
            url
        ) and self._handle(url, url_parsed, url, "sitemap", "", "sitemap")

    def parse_sitemap_xml(self, data: HTTPResponse) -> None:
        """
        This method parses XML sitemaps.
        """

        from_url = data.geturl()
        root = parse(BytesIO(data.data)).getroot()
        for element_ in root:
            for element in element_:
                if not element.tag.casefold().endswith("loc"):
                    continue

                url, parsed_url = self.get_complete_url(urlparse(element.text))
                info("Get an URL in sitemap: " + url)
                if element_.tag.casefold() == "sitemap":
                    info("Get a sitemap from sitemap.xml")
                    self._handle(
                        from_url,
                        parsed_url,
                        url,
                        "sitemap.xml",
                        "sitemap",
                        "sitemap",
                    )
                else:
                    info("Get an URL from sitemap.xml")
                    self._handle(
                        from_url, parsed_url, url, "sitemap.xml", "URL", "html"
                    )

    def parse_sitemap_text(self, data: HTTPResponse) -> None:
        """
        This method parses TEXT sitemaps.
        """

        from_url = data.geturl()
        levels = {}
        for line in data:
            url = self.decode(line).strip()
            level = len(line) - len(url)
            levels[level] = url
            url, parsed_url = self.get_complete_url(
                urlparse("".join(levels[x] for x in levels if x < level) + url)
            )
            info("Get an URL in sitemap.txt: " + url)
            self._handle(
                from_url, parsed_url, url, "sitemap.txt", "URL", "html"
            )

    def parse_sitemap(self, url: Union[str, ParseResult]) -> bool:
        """
        This method requests a sitemap URL and/or parse it.
        """

        data, _ = self.get_data(
            urlparse(url) if isinstance(url, str) else url, False
        )
        if data is None or data.status != 200:
            return False

        if "xml" in data.getheader("Content-Type", ""):
            self.parse_sitemap_xml(data)
            return True
        elif "text/plain" in data.getheader("Content-Type", ""):
            self.parse_sitemap_text(data)
            return True

        return False

    def parse_robots_line(self, from_url: str, line: str, type_: str) -> None:
        """
        This method parses a robots.txt line.
        """

        url = line.split(":", 1)[1].strip()
        url, parsed_url = self.get_complete_url(urlparse(url))
        self._handle(
            from_url,
            parsed_url,
            url,
            "robots.txt",
            type_ if type_ != "html" else "URL",
            type_,
        )

    def ask_crossdomain(self, url: ParseResult) -> None:
        """
        This method send request for crossdomain.xml
        """

        parsed_url = ParseResult(
            url.scheme, url.netloc, "/crossdomain.xml", "", "", ""
        )
        url = parsed_url.geturl()

        if url in self.urls_getted:
            return None

        response, url = self.get_data(parsed_url, False)

        if (
            response is None
            or response.status != 200
            or "xml" not in response.getheader("Content-Type", "")
        ):
            return None

        info("Get /crossdomain.xml")
        cross_domain_policy = parse(response).getroot()
        self._handle(
            url, parsed_url, url, "crossdomain.xml", "", "crossdomain.xml"
        )

        for element in cross_domain_policy:
            domain = element.get("domain")
            if domain is None:
                continue
            parsed_url = ParseResult("https", domain, "/", "", "", "")
            self._handle(
                url,
                parsed_url,
                parsed_url.geturl(),
                "crossdomain.xml",
                "domain",
                "html",
            )

    def ask_robots(self, url: ParseResult) -> None:
        """
        This method send request for robots.txt.
        """

        parsed_url = ParseResult(
            url.scheme, url.netloc, "/robots.txt", "", "", ""
        )
        response, url = self.get_data(parsed_url, False)

        if (
            response is None
            or response.status != 200
            or "text/plain" not in response.getheader("Content-Type", "")
        ):
            return None

        info("Get /robots.txt")
        lines = response.data.splitlines()
        self._handle(url, parsed_url, url, "robots.txt", "", "robots.txt")

        for line in lines:
            line = self.decode(line)
            startswith = line.strip().casefold().startswith

            if startswith("#") or startswith("user-agent"):
                debug("Read a new comment from robots.txt")
            elif (
                startswith("allow") or startswith("disallow")
            ) and ":" in line:
                info("Get an URL page from robots.txt")
                self.parse_robots_line(url, line, "html")
            elif startswith("sitemap") and ":" in line:
                info("Get a sitemap from robots.txt")
                self.parse_robots_line(url, line, "sitemap")
            else:
                info("Invalid line in robots.txt: " + line)

    def get_url_and_data(
        self, urls: List[str], urls_done: Set[str], first: bool
    ) -> Tuple[HTTPResponse, ParseResult, str]:
        """
        This method gets url, parses it and gets data from it.
        """

        url = urls.pop()
        urls_done.append(url)

        parsed_url = urlparse(url)
        response, url_ = self.get_data(parsed_url, first)
        if response is None or response.status != 200 and not first:
            if url_ == "break":
                return None, None, None

            warning(
                "An error occurs on the request, URL is probably wrong: "
                + (url_ or url)
            )
        elif response is None and first:
            message = (
                "An error occurs on the first request, "
                "URL is probably wrong: " + url
            )
            critical(message)
            raise CriticalUrllibError(message)

        return response, parsed_url, url_ or url

    def read_and_parse(
        self, response: HTTPResponse, url: str, first: bool
    ) -> None:
        """
        This method reads the response and parses it.
        """

        is_html = response and "text/html" in response.getheader(
            "Content-Type", ""
        )

        if is_html:
            UrlGetter(url, response.report, self).feed(
                self.decode(response.data)
            )
            first = False
        elif first and not is_html:
            message = (
                f"Response for {url} cannot be parsed and "
                "is not valid in this context."
            )
            critical(message)
            raise ContentTypeError(message)

    def get_parse_html(
        self,
        urls: List[str],
        urls_done: Set[str],
        first: bool,
    ) -> ParseResult:
        """
        This function gets HTML data and parses it.
        """

        response, parsed_url, url = self.get_url_and_data(
            urls, urls_done, first
        )

        self.read_and_parse(response, url, False)

        return parsed_url

    def crawl(self) -> None:
        """
        This function starts crawler.
        """

        urls, urls_done, recursive = (
            self.urls_to_parse,
            self.urls_parsed,
            self.recursive,
        )

        parsed_url = self.get_parse_html(urls, urls_done, True)

        if self.robots:
            self.ask_robots(parsed_url)

        if self.sitemap:
            self.ask_sitemap(parsed_url)

        if self.crossdomain:
            self.ask_crossdomain(parsed_url)

        while recursive and urls and parsed_url:
            parsed_url = self.get_parse_html(urls, urls_done, False)

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

    def get_complete_url(self, url: ParseResult) -> Tuple[str, ParseResult]:
        """
        This function build a complete url.
        """

        if url.netloc:
            if not url.scheme:
                url = ParseResult(
                    self.master_url.scheme,
                    url.netloc,
                    url.path,
                    url.params,
                    url.query,
                    url.fragment,
                )
            return url.geturl(), url

        if url.path and url.path[0] == "/":
            url = ParseResult(
                self.master_url.scheme,
                self.master_url.netloc,
                url.path,
                url.params,
                url.query,
                url.fragment,
            )
            return url.geturl(), url

        url = ParseResult(
            self.master_url.scheme,
            self.master_url.netloc,
            (self.master_url.path + url.path)
            if self.master_url.path and self.master_url.path[-1] == "/"
            else (self.master_url.path + "/" + url.path),
            url.params,
            url.query,
            url.fragment,
        )
        return url.geturl(), url

    def get_local_filepath(self, url: ParseResult) -> str:
        """
        This method returns the local file path to store the response content.
        """

        directory = dirname(url.path[1:]).replace("_", "__").replace("%", "_")
        filename = basename(url.path[1:]).replace("_", "__").replace("%", "_")
        return join(
            CWD,
            url.scheme,
            url.netloc.replace("_", "__").replace(":", "_"),
            normpath(directory),
            quote(
                filename
                + ";"
                + url.params
                + "?"
                + url.query
                # + "#"
                # + url.fragment
            )
            .replace("_", "__")
            .replace("%", "_")[:255],
        )

    def write_response(
        self, url: ParseResult, response: HTTPResponse, report: UrlReport
    ) -> Union[HTTPResponse, None]:
        """
        This method writes the response content for a URL.
        """

        response.report = report
        data = self.reader(response)
        response.data = data

        if not self.store:
            return response, False

        path = self.get_local_filepath(url)
        report.filepath = path

        if not report.requested:
            return response, False

        makedirs(dirname(path), exist_ok=True)

        with open(path, "wb") as file:
            file.write(data)

        return response, True

    def write_error(
        self, url: ParseResult, error: HTTPResponse, report: UrlReport
    ) -> None:
        """
        This method writes the response content on HTTP error.
        """

        error, writed = self.write_response(url, error, report)
        report.status = error.status

        if writed:
            return None

        path = join(
            CWD, url.scheme, url.netloc.replace("_", "__").replace(":", "_")
        )
        path = join(path, str(error.code) + ".html")

        with open(path, "wb") as file:
            file.write(error.data)

    def prepare_request(
        self, url_parsed: ParseResult
    ) -> Tuple[UrlReport, str, bool]:
        """
        This method prepares the request and response parsing.
        """

        url, url_parsed = self.get_complete_url(url_parsed)
        filepath = self.get_local_filepath(url_parsed)
        report = UrlReport(filepath)

        if not self.update and exists(filepath):
            info("Do not request " + url + " response is write by previous crawls")
            report.requested = False
            url = filepath
        else:
            self.counter += 1

        reports[url] = report
        return report, url, report.requested

    def get_data(
        self, url_parsed: ParseResult, first: bool
    ) -> Tuple[HttpResponse, str]:
        """
        This function sends the HTTP request
        and returns the HTTP response.
        """

        if self.max_request and self.max_request <= self.counter:
            return None, "break"

        report, url, request = self.prepare_request(url_parsed)
        if not request:
            response = open(url, "rb")
            response.code = 200
            response.status = 200
            response.getheader = lambda x, y: "text/html"
            response.geturl = lambda: url
        else:
            if not first:
                sleep(self.interval)
    
            try:
                response = urlopen(Request(url, headers=self.headers))
            except (URLError, HTTPError) as error_:
                if getattr(error_, "code", None):
                    warning(f"HTTP {error_.code} error in " + url)
                    self.write_error(url_parsed, error_, report)
                    return error_, None
                error("Could not request: " + str(error_) + " " + url)
                return None, None

        self.write_response(url_parsed, response, report)
        info("Get resources from this URL: " + url)
        return response, url

    if selenium:
        _get_data = get_data

        def get_data(
            self, url: ParseResult, first: bool
        ) -> Tuple[HttpResponse, str]:
            """
            This method gets the Web page content after javascript execution
            using selenium.
            """

            response = self._get_data(url, first)
            url, _ = self.get_complete_url(url)

            driver.get(url)
            precedent_length = len(driver.page_source)
            sleep(0.5)

            while len(driver.page_source) != precedent_length:
                precedent_length = len(driver.page_source)
                sleep(0.5)

            if script := getattr(self, "script", None):
                driver.execute_script(script)

            return (
                HttpResponse(
                    response.getcode(),
                    url,
                    response.getheaders(),
                    driver.page_source.encode(),
                ),
                url,
            )


if format_output:

    class CrawlerColoredPrinter(_Crawler):
        """
        This class prints all URLs.
        """

        def get_pourcent(self):
            """
            This function returns the pourcents of URL requested.
            """

            pourcent = round(
                self.counter
                / (self.max_request or len(self.urls_to_parse))
                * 100
            )
            if pourcent == 100:
                return 99
            return pourcent

        def handle_web_page(
            self, from_url: str, url: str, tag: str, attribute: str
        ) -> Union[bool, None]:
            """
            This method prints the URL found.
            """

            messagef(f"[{tag}<{attribute}>] {url}", "OK", self.get_pourcent())

        def handle_static(
            self, from_url: str, url: str, tag: str, attribute: str
        ) -> Union[bool, None]:
            """
            This method prints the URL found.
            """

            messagef(
                f"[{tag}<{attribute}>] {url}", "INFO", self.get_pourcent()
            )

        def handle_resource(
            self, from_url: str, url: str, tag: str, attribute: str
        ) -> Union[bool, None]:
            """
            This method prints the URL found.
            """

            messagef(
                f"[{tag}<{attribute}>] {url}", "TODO", self.get_pourcent()
            )


class CrawlerRawPrinter(_Crawler):
    """
    This class prints all URLs.
    """

    def handle_web_page(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        print("[+]", tag, attribute, url)

    def handle_static(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        print("[*]", tag, attribute, url)

    def handle_resource(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        print("[#]", tag, attribute, url)


class CrawlerRawUrlOnlyPrinter(_Crawler):
    """
    This class prints all URLs.
    """

    def handle_web_page(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        print(url)

    def handle_static(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        print(url)

    def handle_resource(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        print(url)


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
        default=False,
        action="store_true",
        help="Crawl URLs recursively.",
    )
    add(
        "--update",
        "-u",
        default=False,
        action="store_true",
        help=(
            "Re-downloads and overwrites responses from"
            " requests made during previous crawls."
        ),
    )
    add(
        "--insecure",
        "-i",
        default=False,
        action="store_true",
        help="Use insecure SSL (support selenium and urllib)",
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
        "--do-not-request-crossdomain",
        "--no-crossdomain",
        "-C",
        default=False,
        action="store_true",
        help="Don't search, request and parse crossdomain.xml",
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
        "--cookies",
        "-c",
        nargs="+",
        action="extend",
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
        "--dynamic-tags-counter",
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
        "-L",
        help="WebSiteCloner logs level.",
        default="WARNING",
        choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"},
    )
    add(
        "--logfile",
        "-l",
        help="WebCrawler logs file.",
    )
    add(
        "--interval-request",
        "--interval",
        "-I",
        default=0,
        type=float,
        help="Interval between each requests by domain.",
    )
    add(
        "--output-format",
        "--format",
        "-f",
        default="colored" if format_output else "raw",
        choices={"raw", "raw-url-only", "colored"}
        if format_output
        else {"raw", "raw-url-only", "colored"},
        help="Output format.",
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

    group_download = parser.add_mutually_exclusive_group()
    add = group_download.add_argument

    add(
        "--download-all",
        "--download",
        "-D",
        "-D0",
        action="store_true",
        default=False,
        help="Download (store) all responses",
    )
    add(
        "--download-html",
        "--dh",
        "-D1",
        action="store_true",
        default=False,
        help="Download (store) only HTML responses",
    )
    add(
        "--download-static",
        "--ds",
        "-D2",
        action="store_true",
        default=False,
        help="Download (store) only static files (HTML, CSS, JavaScript)",
    )
    add(
        "--download-resources",
        "--dr",
        "-D3",
        action="store_true",
        default=False,
        help=(
            "Download (store) only resources files "
            "(images, documents, icon...)"
        ),
    )
    add(
        "--download-by-content-type",
        "--dct",
        "-D4",
        help=(
            "Download (store) only responses with "
            "Content-Type that contains this value"
        ),
    )
    add(
        "--download-requested",
        "--dR",
        "-D5",
        action="store_true",
        default=False,
        help=(
            "Download all requests responses and try to requests only Web page"
        ),
    )
    add(
        "--do-not-download",
        "--dN",
        "-D6",
        action="store_true",
        default=False,
        help=("Try to requests only Web page and do not download"),
    )

    return parser.parse_args()


def get_download_policy(arguments: Namespace) -> Union[str, None]:
    """
    This function returns the download policy.
    """

    if arguments.download_all:
        return "all"
    elif arguments.download_html:
        return "text/html"
    elif arguments.download_static:
        return "static"
    elif arguments.download_resources:
        return "resources"
    elif arguments.download_requested:
        return "requested"
    elif arguments.do_not_download:
        return "do not download"

    return arguments.download_by_content_type


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

    if arguments.dynamic_tags_counter:
        interaction_tags.update({x: 1 for x in arguments.dynamic_tags_counter})

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

    if arguments.cookies:
        cookies = headers.get("Cookie", "")
        if cookies:
            cookies += ";"
        cookies += ";".join(arguments.cookies)

    context = create_default_context()
    if selenium:
        global driver
        options = ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if arguments.no_gui:
            options.add_argument("--headless=new")
        if arguments.insecure:
            options.add_argument("ignore-certificate-errors")
        driver = Chrome(options=options)
    elif arguments.insecure:
        context = _create_unverified_context()

    copy: _Crawler = globals()[
        "Crawler"
        + arguments.output_format.title().replace("-", "")
        + "Printer"
    ](
        arguments.url,
        headers=headers,
        recursive=arguments.recursive,
        update=arguments.update,
        max_request=arguments.max_request,
        only_domain=not arguments.not_only_domain,
        robots=not arguments.do_not_request_robots,
        sitemap=not arguments.do_not_request_sitemap,
        crossdomain=not arguments.do_not_request_crossdomain,
        context=context,
        interval=arguments.interval_request,
        download_policy=get_download_policy(arguments),
    )

    try:
        copy.crawl()
    except (ContentTypeError, CriticalUrllibError):
        print(
            "Critical exception on the first request"
            ", there is nothing to cr0wl....",
            file=stderr,
        )
        critical("Critical exception on the first request.")
        return 2

    if selenium:
        driver.quit()

    dump(
        {k: v.to_dict() for k, v in reports.items()},
        open(arguments.report_filename, "w"),
    )

    return 0


if __name__ == "__main__":
    exit(main())
