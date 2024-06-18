#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This module implements a crawler to find all links and resources
#    on the target web site.
#    Copyright (C) 2023, 2024  Maurice Lambert

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
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github-cloud.s3.amazonaws.com
[*] [link<href>] https://user-images.githubusercontent.com/
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github.githubassets.com/assets/light-b92e9647318f.css
[*] [link<href>] https://github.githubassets.com/assets/dark-5d486a4ede8e.css
[*] [link<href>] https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css
[*] [link<href>] https://github.githubassets.com/assets/primer-d6dcdf72e61d.css
[*] [link<href>] https://github.githubassets.com/assets/global-faa25eb56e2e.css
[*] [link<href>] https://github.githubassets.com/assets/github-933ef5369a60.css
[*] [link<href>] https://github.githubassets.com/assets/profile-9b93f5908234.css
[*] [script<src>] https://github.githubassets.com/assets/wp-runtime-e49d85e88ee7.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js
[*] [script<src>] https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js
[*] [script<src>] https://github.githubassets.com/assets/environment-fc6543d75794.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js
[*] [script<src>] https://github.githubassets.com/assets/github-elements-3485f2997bc6.js
[*] [script<src>] https://github.githubassets.com/assets/element-registry-981cc2eaa259.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js
[*] [script<src>] https://github.githubassets.com/assets/behaviors-464f50283c96.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js
[*] [script<src>] https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_primer_behaviors_dist_esm_-f047dc-5af6fdc6ba3e.js
[*] [script<src>] https://github.githubassets.com/assets/profile-96509d82fe08.js
[*] [link<href>] https://github.githubassets.com/
[#] [link<href>] https://github.com/opensearch.xml
[#] [link<href>] https://github.com/fluidicon.png
[*] [link<href>] https://github.githubassets.com/pinned-octocat.svg
[#] [link<href>] https://github.githubassets.com/favicons/favicon.png
[*] [link<href>] https://github.githubassets.com/favicons/favicon.svg
[*] [link<href>] https://github.com/manifest.json
[+] [a<href>] https://github.com/mauricelambert/#start-of-content
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-8311888324b2.js
[*] [script<src>] https://github.githubassets.com/assets/sessions-04ec2c51e991.js
[+] [a<href>] https://github.com/
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E&source=header
[+] [a<href>] https://github.com/features/actions
[+] [a<href>] https://github.com/features/packages
[+] [a<href>] https://github.com/features/security
[+] [a<href>] https://github.com/features/codespaces
[+] [a<href>] https://github.com/features/copilot
[+] [a<href>] https://github.com/features/code-review
[+] [a<href>] https://github.com/features/issues
[+] [a<href>] https://github.com/features/discussions
[+] [a<href>] https://github.com/features
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://skills.github.com/
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/enterprise
[+] [a<href>] https://github.com/team
[+] [a<href>] https://github.com/enterprise/startups
[+] [a<href>] https://education.github.com
[+] [a<href>] https://github.com/solutions/ci-cd/
[+] [a<href>] https://resources.github.com/devops/
[+] [a<href>] https://resources.github.com/devops/fundamentals/devsecops/
[+] [a<href>] https://resources.github.com/learn/pathways/
[+] [a<href>] https://resources.github.com/
[+] [a<href>] https://github.com/customer-stories
[+] [a<href>] https://partner.github.com/
[+] [a<href>] https://github.com/sponsors
[+] [a<href>] https://github.com/readme
[+] [a<href>] https://github.com/topics
[+] [a<href>] https://github.com/trending
[+] [a<href>] https://github.com/collections
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [form<action>] https://github.com/search/feedback
[+] [form<action>] https://github.com/search/custom_scopes
[#] [auto-check<src>] https://github.com/search/custom_scopes/check_name
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E&source=header
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?s=64&v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?s=64&v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://avatars.githubusercontent.com/u/50479118?v=4
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=followers
[+] [a<href>] https://github.com/mauricelambert?tab=following
[+] [a<href>] https://github.com/mauricelambert?tab=achievements
[+] [a<href>] https://github.com/mauricelambert?achievement=quickdraw&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/quickdraw-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=starstruck&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/starstruck-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=pull-shark&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/pull-shark-default.png
[+] [a<href>] https://github.com/orgs/community/discussions/categories/profile
[+] [a<href>] https://github.com/mauricelambert?tab=achievements
[+] [a<href>] https://github.com/mauricelambert?achievement=quickdraw&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/quickdraw-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=starstruck&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/starstruck-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=pull-shark&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/pull-shark-default.png
[+] [a<href>] https://github.com/orgs/community/discussions/categories/profile
[+] [form<action>] https://github.com/settings/blocked_users
[+] [a<href>] https://docs.github.com/en/articles/blocking-a-user-from-your-personal-account
[+] [a<href>] https://docs.github.com/en/articles/reporting-abuse-or-spam
[+] [a<href>] https://github.com/contact/report-abuse?report=mauricelambert+%28user%29
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert/WebScripts
[+] [a<href>] https://github.com/mauricelambert/WebScripts/stargazers
[+] [a<href>] https://github.com/mauricelambert/WebScripts/forks
[+] [a<href>] https://github.com/mauricelambert/SpyWare
[+] [a<href>] https://github.com/mauricelambert/SpyWare/stargazers
[+] [a<href>] https://github.com/mauricelambert/SpyWare/forks
[+] [a<href>] https://github.com/mauricelambert/CVE-2022-21907
[+] [a<href>] https://github.com/mauricelambert/CVE-2022-21907/stargazers
[+] [a<href>] https://github.com/mauricelambert/CVE-2022-21907/forks
[+] [a<href>] https://github.com/mauricelambert/Vulnerability1-XSS-title
[+] [a<href>] https://github.com/mauricelambert/CLEF
[+] [a<href>] https://github.com/mauricelambert/FastRC4
[+] [a<href>] https://github.com/mauricelambert/FastRC4/stargazers
[+] [a<href>] https://docs.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2023-10-01&to=2023-10-15
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2022-12-01&to=2022-12-31
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2021-12-01&to=2021-12-31
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2020-12-01&to=2020-12-31
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2019-12-01&to=2019-12-31
[+] [a<href>] https://github.com/mauricelambert/TerminalMessages
[+] [a<href>] https://github.com/mauricelambert/TerminalMessages/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/mauricelambert.github.io
[+] [a<href>] https://github.com/mauricelambert/mauricelambert.github.io/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/MaliciousFileDetector
[+] [a<href>] https://github.com/mauricelambert/MaliciousFileDetector/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/AsyncPortScanner
[+] [a<href>] https://github.com/mauricelambert/AsyncPortScanner/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/MalwareAnalysis
[+] [a<href>] https://github.com/mauricelambert/MalwareAnalysis/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/Cr0wl3r
[+] [a<href>] https://github.com/mauricelambert/Cr0wl3r/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/MaliciousFileDetector
[+] [form<action>] https://github.com/mauricelambert?tab=overview&from=2023-09-01&to=2023-09-30&include_header=no
[+] [a<href>] https://docs.github.com/categories/setting-up-and-managing-your-github-profile
[+] [a<href>] https://github.com
[+] [a<href>] https://docs.github.com/site-policy/github-terms/github-terms-of-service
[+] [a<href>] https://docs.github.com/site-policy/privacy-policies/github-privacy-statement
[+] [a<href>] https://github.com/security
[+] [a<href>] https://www.githubstatus.com/
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://support.github.com?tags=dotcom-footer
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://services.github.com
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/about
[#] [robots.txt<>] https://github.com/robots.txt
[+] [robots.txt<URL>] https://github.com/*/pulse
[+] [robots.txt<URL>] https://github.com/*/tree/
[+] [robots.txt<URL>] https://github.com/gist/
[+] [robots.txt<URL>] https://github.com/*/forks
[+] [robots.txt<URL>] https://github.com/*/stars
[+] [robots.txt<URL>] https://github.com/*/download
[+] [robots.txt<URL>] https://github.com/*/revisions
[+] [robots.txt<URL>] https://github.com/*/issues/new
[+] [robots.txt<URL>] https://github.com/*/issues/search
[+] [robots.txt<URL>] https://github.com/*/commits/
[+] [robots.txt<URL>] https://github.com/*/commits/*?author
[+] [robots.txt<URL>] https://github.com/*/commits/*?path
[+] [robots.txt<URL>] https://github.com/*/branches
[+] [robots.txt<URL>] https://github.com/*/tags
[+] [robots.txt<URL>] https://github.com/*/contributors
[+] [robots.txt<URL>] https://github.com/*/comments
[+] [robots.txt<URL>] https://github.com/*/stargazers
[+] [robots.txt<URL>] https://github.com/*/archive/
[+] [robots.txt<URL>] https://github.com/*/blame/
[+] [robots.txt<URL>] https://github.com/*/watchers
[+] [robots.txt<URL>] https://github.com/*/network
[+] [robots.txt<URL>] https://github.com/*/graphs
[+] [robots.txt<URL>] https://github.com/*/raw/
[+] [robots.txt<URL>] https://github.com/*/compare/
[+] [robots.txt<URL>] https://github.com/*/cache/
[+] [robots.txt<URL>] https://github.com/.git/
[+] [robots.txt<URL>] https://github.com/mauricelambert/*/.git/
[+] [robots.txt<URL>] https://github.com/*.git$
[+] [robots.txt<URL>] https://github.com/search/advanced
[+] [robots.txt<URL>] https://github.com/search
[+] [robots.txt<URL>] https://github.com/mauricelambert/*/search
[+] [robots.txt<URL>] https://github.com/*q=
[+] [robots.txt<URL>] https://github.com/*.atom$
[+] [robots.txt<URL>] https://github.com/ekansa/Open-Context-Data
[+] [robots.txt<URL>] https://github.com/ekansa/opencontext-*
[+] [robots.txt<URL>] https://github.com/mauricelambert/*/tarball/
[+] [robots.txt<URL>] https://github.com/mauricelambert/*/zipball/
[+] [robots.txt<URL>] https://github.com/*source=*
[+] [robots.txt<URL>] https://github.com/*ref_cta=*
[+] [robots.txt<URL>] https://github.com/*plan=*
[+] [robots.txt<URL>] https://github.com/*return_to=*
[+] [robots.txt<URL>] https://github.com/*ref_loc=*
[+] [robots.txt<URL>] https://github.com/*setup_organization=*
[+] [robots.txt<URL>] https://github.com/*source_repo=*
[+] [robots.txt<URL>] https://github.com/*ref_page=*
[+] [robots.txt<URL>] https://github.com/*source=*
[+] [robots.txt<URL>] https://github.com/*referrer=*
[+] [robots.txt<URL>] https://github.com/*report=*
[+] [robots.txt<URL>] https://github.com/*author=*
[+] [robots.txt<URL>] https://github.com/*since=*
[+] [robots.txt<URL>] https://github.com/*until=*
[+] [robots.txt<URL>] https://github.com/*commits?author=*
[+] [robots.txt<URL>] https://github.com/*report-abuse?report=*
[+] [robots.txt<URL>] https://github.com/*tab=*
[+] [robots.txt<URL>] https://github.com/*?tab=achievements&achievement=*
[+] [robots.txt<URL>] https://github.com/account-login
[+] [robots.txt<URL>] https://github.com/Explodingstuff/
[2023-15-10 09:29:52] WARNING (30): HTTP 406 error in https://github.com/sitemap.xml
[#] [crossdomain.xml<>] https://github.com/crossdomain.xml
[#]  3% |█                   |
~# python3 Cr0wl3r.py -F test.json -l DEBUG -f test.log -R -S -d -c "test=test" -H "User-Agent:Chrome" -m 3 -t p -r https://github.com/mauricelambert
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github-cloud.s3.amazonaws.com
[*] [link<href>] https://user-images.githubusercontent.com/
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github.githubassets.com/assets/light-b92e9647318f.css
[*] [link<href>] https://github.githubassets.com/assets/dark-5d486a4ede8e.css
[*] [link<href>] https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css
[*] [link<href>] https://github.githubassets.com/assets/primer-d6dcdf72e61d.css
[*] [link<href>] https://github.githubassets.com/assets/global-faa25eb56e2e.css
[*] [link<href>] https://github.githubassets.com/assets/github-933ef5369a60.css
[*] [link<href>] https://github.githubassets.com/assets/profile-9b93f5908234.css
[*] [script<src>] https://github.githubassets.com/assets/wp-runtime-e49d85e88ee7.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js
[*] [script<src>] https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js
[*] [script<src>] https://github.githubassets.com/assets/environment-fc6543d75794.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js
[*] [script<src>] https://github.githubassets.com/assets/github-elements-3485f2997bc6.js
[*] [script<src>] https://github.githubassets.com/assets/element-registry-981cc2eaa259.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js
[*] [script<src>] https://github.githubassets.com/assets/behaviors-464f50283c96.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js
[*] [script<src>] https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_primer_behaviors_dist_esm_-f047dc-5af6fdc6ba3e.js
[*] [script<src>] https://github.githubassets.com/assets/profile-96509d82fe08.js
[*] [link<href>] https://github.githubassets.com/
[#] [link<href>] https://github.com/opensearch.xml
[#] [link<href>] https://github.com/fluidicon.png
[*] [link<href>] https://github.githubassets.com/pinned-octocat.svg
[#] [link<href>] https://github.githubassets.com/favicons/favicon.png
[*] [link<href>] https://github.githubassets.com/favicons/favicon.svg
[*] [link<href>] https://github.com/manifest.json
[+] [a<href>] https://github.com/mauricelambert/#start-of-content
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-8311888324b2.js
[*] [script<src>] https://github.githubassets.com/assets/sessions-04ec2c51e991.js
[+] [a<href>] https://github.com/
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E&source=header
[+] [a<href>] https://github.com/features/actions
[+] [a<href>] https://github.com/features/packages
[+] [a<href>] https://github.com/features/security
[+] [a<href>] https://github.com/features/codespaces
[+] [a<href>] https://github.com/features/copilot
[+] [a<href>] https://github.com/features/code-review
[+] [a<href>] https://github.com/features/issues
[+] [a<href>] https://github.com/features/discussions
[+] [a<href>] https://github.com/features
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://skills.github.com/
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/enterprise
[+] [a<href>] https://github.com/team
[+] [a<href>] https://github.com/enterprise/startups
[+] [a<href>] https://education.github.com
[+] [a<href>] https://github.com/solutions/ci-cd/
[+] [a<href>] https://resources.github.com/devops/
[+] [a<href>] https://resources.github.com/devops/fundamentals/devsecops/
[+] [a<href>] https://resources.github.com/learn/pathways/
[+] [a<href>] https://resources.github.com/
[+] [a<href>] https://github.com/customer-stories
[+] [a<href>] https://partner.github.com/
[+] [a<href>] https://github.com/sponsors
[+] [a<href>] https://github.com/readme
[+] [a<href>] https://github.com/topics
[+] [a<href>] https://github.com/trending
[+] [a<href>] https://github.com/collections
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [form<action>] https://github.com/search/feedback
[+] [form<action>] https://github.com/search/custom_scopes
[#] [auto-check<src>] https://github.com/search/custom_scopes/check_name
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E&source=header
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?s=64&v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?s=64&v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://avatars.githubusercontent.com/u/50479118?v=4
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=followers
[+] [a<href>] https://github.com/mauricelambert?tab=following
[+] [a<href>] https://github.com/mauricelambert?tab=achievements
[+] [a<href>] https://github.com/mauricelambert?achievement=quickdraw&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/quickdraw-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=starstruck&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/starstruck-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=pull-shark&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/pull-shark-default.png
[+] [a<href>] https://github.com/orgs/community/discussions/categories/profile
[+] [a<href>] https://github.com/mauricelambert?tab=achievements
[+] [a<href>] https://github.com/mauricelambert?achievement=quickdraw&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/quickdraw-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=starstruck&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/starstruck-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=pull-shark&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/pull-shark-default.png
[+] [a<href>] https://github.com/orgs/community/discussions/categories/profile
[+] [form<action>] https://github.com/settings/blocked_users
[+] [a<href>] https://docs.github.com/en/articles/blocking-a-user-from-your-personal-account
[+] [a<href>] https://docs.github.com/en/articles/reporting-abuse-or-spam
[+] [a<href>] https://github.com/contact/report-abuse?report=mauricelambert+%28user%29
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert/WebScripts
[+] [a<href>] https://github.com/mauricelambert/WebScripts/stargazers
[+] [a<href>] https://github.com/mauricelambert/WebScripts/forks
[+] [a<href>] https://github.com/mauricelambert/SpyWare
[+] [a<href>] https://github.com/mauricelambert/SpyWare/stargazers
[+] [a<href>] https://github.com/mauricelambert/SpyWare/forks
[+] [a<href>] https://github.com/mauricelambert/CVE-2022-21907
[+] [a<href>] https://github.com/mauricelambert/CVE-2022-21907/stargazers
[+] [a<href>] https://github.com/mauricelambert/CVE-2022-21907/forks
[+] [a<href>] https://github.com/mauricelambert/Vulnerability1-XSS-title
[+] [a<href>] https://github.com/mauricelambert/CLEF
[+] [a<href>] https://github.com/mauricelambert/FastRC4
[+] [a<href>] https://github.com/mauricelambert/FastRC4/stargazers
[+] [a<href>] https://docs.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2023-10-01&to=2023-10-15
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2022-12-01&to=2022-12-31
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2021-12-01&to=2021-12-31
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2020-12-01&to=2020-12-31
[+] [a<href>] https://github.com/mauricelambert?tab=overview&from=2019-12-01&to=2019-12-31
[+] [a<href>] https://github.com/mauricelambert/TerminalMessages
[+] [a<href>] https://github.com/mauricelambert/TerminalMessages/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/mauricelambert.github.io
[+] [a<href>] https://github.com/mauricelambert/mauricelambert.github.io/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/MaliciousFileDetector
[+] [a<href>] https://github.com/mauricelambert/MaliciousFileDetector/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/AsyncPortScanner
[+] [a<href>] https://github.com/mauricelambert/AsyncPortScanner/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/MalwareAnalysis
[+] [a<href>] https://github.com/mauricelambert/MalwareAnalysis/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/Cr0wl3r
[+] [a<href>] https://github.com/mauricelambert/Cr0wl3r/commits?author=mauricelambert&since=2023-10-01&until=2023-10-16
[+] [a<href>] https://github.com/mauricelambert/MaliciousFileDetector
[+] [form<action>] https://github.com/mauricelambert?tab=overview&from=2023-09-01&to=2023-09-30&include_header=no
[+] [a<href>] https://docs.github.com/categories/setting-up-and-managing-your-github-profile
[+] [a<href>] https://github.com
[+] [a<href>] https://docs.github.com/site-policy/github-terms/github-terms-of-service
[+] [a<href>] https://docs.github.com/site-policy/privacy-policies/github-privacy-statement
[+] [a<href>] https://github.com/security
[+] [a<href>] https://www.githubstatus.com/
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://support.github.com?tags=dotcom-footer
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://services.github.com
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/about
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github-cloud.s3.amazonaws.com
[*] [link<href>] https://user-images.githubusercontent.com/
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github.githubassets.com/assets/light-b92e9647318f.css
[*] [link<href>] https://github.githubassets.com/assets/dark-5d486a4ede8e.css
[*] [link<href>] https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css
[*] [link<href>] https://github.githubassets.com/assets/primer-d6dcdf72e61d.css
[*] [link<href>] https://github.githubassets.com/assets/global-faa25eb56e2e.css
[*] [link<href>] https://github.githubassets.com/assets/github-933ef5369a60.css
[*] [link<href>] https://github.githubassets.com/assets/profile-9b93f5908234.css
[*] [link<href>] https://github.githubassets.com/assets/projects-ad534a3151e8.css
[*] [script<src>] https://github.githubassets.com/assets/wp-runtime-e49d85e88ee7.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js
[*] [script<src>] https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js
[*] [script<src>] https://github.githubassets.com/assets/environment-fc6543d75794.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js
[*] [script<src>] https://github.githubassets.com/assets/github-elements-3485f2997bc6.js
[*] [script<src>] https://github.githubassets.com/assets/element-registry-981cc2eaa259.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js
[*] [script<src>] https://github.githubassets.com/assets/behaviors-464f50283c96.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js
[*] [script<src>] https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_primer_behaviors_dist_esm_-f047dc-5af6fdc6ba3e.js
[*] [script<src>] https://github.githubassets.com/assets/profile-96509d82fe08.js
[*] [link<href>] https://github.githubassets.com/
[#] [link<href>] https://github.com/opensearch.xml
[#] [link<href>] https://github.com/fluidicon.png
[*] [link<href>] https://github.githubassets.com/pinned-octocat.svg
[#] [link<href>] https://github.githubassets.com/favicons/favicon.png
[*] [link<href>] https://github.githubassets.com/favicons/favicon.svg
[*] [link<href>] https://github.com/manifest.json
[+] [a<href>] https://github.com/mauricelambert/#start-of-content
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-8311888324b2.js
[*] [script<src>] https://github.githubassets.com/assets/sessions-04ec2c51e991.js
[+] [a<href>] https://github.com/
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2Fmauricelambert&source=header
[+] [a<href>] https://github.com/features/actions
[+] [a<href>] https://github.com/features/packages
[+] [a<href>] https://github.com/features/security
[+] [a<href>] https://github.com/features/codespaces
[+] [a<href>] https://github.com/features/copilot
[+] [a<href>] https://github.com/features/code-review
[+] [a<href>] https://github.com/features/issues
[+] [a<href>] https://github.com/features/discussions
[+] [a<href>] https://github.com/features
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://skills.github.com/
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/enterprise
[+] [a<href>] https://github.com/team
[+] [a<href>] https://github.com/enterprise/startups
[+] [a<href>] https://education.github.com
[+] [a<href>] https://github.com/solutions/ci-cd/
[+] [a<href>] https://resources.github.com/devops/
[+] [a<href>] https://resources.github.com/devops/fundamentals/devsecops/
[+] [a<href>] https://resources.github.com/learn/pathways/
[+] [a<href>] https://resources.github.com/
[+] [a<href>] https://github.com/customer-stories
[+] [a<href>] https://partner.github.com/
[+] [a<href>] https://github.com/sponsors
[+] [a<href>] https://github.com/readme
[+] [a<href>] https://github.com/topics
[+] [a<href>] https://github.com/trending
[+] [a<href>] https://github.com/collections
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [form<action>] https://github.com/search/feedback
[+] [form<action>] https://github.com/search/custom_scopes
[#] [auto-check<src>] https://github.com/search/custom_scopes/check_name
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert%3Ftab%3Dprojects
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2Fmauricelambert&source=header
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?s=64&v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert%3Ftab%3Dprojects
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?s=64&v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert%3Ftab%3Dprojects
[+] [a<href>] https://avatars.githubusercontent.com/u/50479118?v=4
[#] [img<src>] https://avatars.githubusercontent.com/u/50479118?v=4
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert%3Ftab%3Dprojects
[+] [a<href>] https://github.com/mauricelambert?tab=followers
[+] [a<href>] https://github.com/mauricelambert?tab=following
[+] [a<href>] https://github.com/mauricelambert?tab=achievements
[+] [a<href>] https://github.com/mauricelambert?achievement=quickdraw&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/quickdraw-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=starstruck&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/starstruck-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=pull-shark&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/pull-shark-default.png
[+] [a<href>] https://github.com/orgs/community/discussions/categories/profile
[+] [a<href>] https://github.com/mauricelambert?tab=achievements
[+] [a<href>] https://github.com/mauricelambert?achievement=quickdraw&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/quickdraw-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=starstruck&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/starstruck-default.png
[+] [a<href>] https://github.com/mauricelambert?achievement=pull-shark&tab=achievements
[#] [img<src>] https://github.githubassets.com/images/modules/profile/achievements/pull-shark-default.png
[+] [a<href>] https://github.com/orgs/community/discussions/categories/profile
[+] [form<action>] https://github.com/settings/blocked_users
[+] [a<href>] https://docs.github.com/en/articles/blocking-a-user-from-your-personal-account
[+] [a<href>] https://docs.github.com/en/articles/reporting-abuse-or-spam
[+] [a<href>] https://github.com/contact/report-abuse?report=mauricelambert+%28user%29
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com/mauricelambert
[+] [a<href>] https://github.com/mauricelambert?tab=repositories
[+] [a<href>] https://github.com/mauricelambert?tab=projects
[+] [a<href>] https://github.com/mauricelambert?tab=packages
[+] [a<href>] https://github.com/mauricelambert?tab=stars
[+] [a<href>] https://github.com
[+] [a<href>] https://docs.github.com/site-policy/github-terms/github-terms-of-service
[+] [a<href>] https://docs.github.com/site-policy/privacy-policies/github-privacy-statement
[+] [a<href>] https://github.com/security
[+] [a<href>] https://www.githubstatus.com/
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://support.github.com?tags=dotcom-footer
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://services.github.com
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/about
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github-cloud.s3.amazonaws.com
[*] [link<href>] https://user-images.githubusercontent.com/
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github.githubassets.com/assets/light-b92e9647318f.css
[*] [link<href>] https://github.githubassets.com/assets/dark-5d486a4ede8e.css
[*] [link<href>] https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css
[*] [link<href>] https://github.githubassets.com/assets/primer-d6dcdf72e61d.css
[*] [link<href>] https://github.githubassets.com/assets/global-faa25eb56e2e.css
[*] [link<href>] https://github.githubassets.com/assets/github-933ef5369a60.css
[*] [link<href>] https://github.githubassets.com/assets/site-00cc76652b8b.css
[*] [link<href>] https://github.githubassets.com/assets/feature-issues-c40a089d85fd.css
[*] [script<src>] https://github.githubassets.com/assets/wp-runtime-e49d85e88ee7.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js
[*] [script<src>] https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js
[*] [script<src>] https://github.githubassets.com/assets/environment-fc6543d75794.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js
[*] [script<src>] https://github.githubassets.com/assets/github-elements-3485f2997bc6.js
[*] [script<src>] https://github.githubassets.com/assets/element-registry-981cc2eaa259.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js
[*] [script<src>] https://github.githubassets.com/assets/behaviors-464f50283c96.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js
[*] [script<src>] https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-b4a243-3ebeb0ebdb7e.js
[*] [script<src>] https://github.githubassets.com/assets/marketing-5a69d86775d5.js
[*] [link<href>] https://github.githubassets.com/
[#] [link<href>] https://github.com/opensearch.xml
[#] [link<href>] https://github.com/fluidicon.png
[*] [link<href>] https://github.githubassets.com/static/fonts/github/mona-sans.woff2
[*] [link<href>] https://github.githubassets.com/pinned-octocat.svg
[#] [link<href>] https://github.githubassets.com/favicons/favicon.png
[*] [link<href>] https://github.githubassets.com/favicons/favicon.svg
[*] [link<href>] https://github.com/manifest.json
[+] [a<href>] https://github.com/mauricelambert/#start-of-content
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-8311888324b2.js
[*] [script<src>] https://github.githubassets.com/assets/sessions-04ec2c51e991.js
[+] [a<href>] https://github.com/
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2Ffeatures%2Fissues&source=header
[+] [a<href>] https://github.com/features/actions
[+] [a<href>] https://github.com/features/packages
[+] [a<href>] https://github.com/features/security
[+] [a<href>] https://github.com/features/codespaces
[+] [a<href>] https://github.com/features/copilot
[+] [a<href>] https://github.com/features/code-review
[+] [a<href>] https://github.com/features/issues
[+] [a<href>] https://github.com/features/discussions
[+] [a<href>] https://github.com/features
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://skills.github.com/
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/enterprise
[+] [a<href>] https://github.com/team
[+] [a<href>] https://github.com/enterprise/startups
[+] [a<href>] https://education.github.com
[+] [a<href>] https://github.com/solutions/ci-cd/
[+] [a<href>] https://resources.github.com/devops/
[+] [a<href>] https://resources.github.com/devops/fundamentals/devsecops/
[+] [a<href>] https://resources.github.com/learn/pathways/
[+] [a<href>] https://resources.github.com/
[+] [a<href>] https://github.com/customer-stories
[+] [a<href>] https://partner.github.com/
[+] [a<href>] https://github.com/sponsors
[+] [a<href>] https://github.com/readme
[+] [a<href>] https://github.com/topics
[+] [a<href>] https://github.com/trending
[+] [a<href>] https://github.com/collections
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [form<action>] https://github.com/search/feedback
[+] [form<action>] https://github.com/search/custom_scopes
[#] [auto-check<src>] https://github.com/search/custom_scopes/check_name
[+] [a<href>] https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Ffeatures%2Fissues
[+] [a<href>] https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2Ffeatures%2Fissues&source=header
[+] [a<href>] https://github.com/features/
[+] [a<href>] https://github.com/features/actions
[+] [a<href>] https://github.com/features/packages
[+] [a<href>] https://github.com/features/security
[+] [a<href>] https://github.com/features/codespaces
[+] [a<href>] https://github.com/features/copilot
[+] [a<href>] https://github.com/features/code-review
[+] [a<href>] https://github.com/features/code-search
[+] [a<href>] https://github.com/features/issues
[+] [a<href>] https://github.com/features/discussions
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/circle.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/circle-arrows.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-14.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-open.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-15.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-16.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-18.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-heart.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-17.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-19.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-20.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-open.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-22.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-21.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/icon-external.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-tada.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-23.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-24.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-merged.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-25.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-26.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-stack-2.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-ready.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-thumbs.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-thumbs.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-thumbs.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-27.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-13.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-open.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-12.png
[#] [img<src>] https://avatars.githubusercontent.com/pifafu?s=122&v=4
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-2.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-heart.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-22.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-1.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-6.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-stack.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-5.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-eyes.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-4.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-3.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-merged.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-8.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-10.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/pr-ready.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-thumbs.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-thumbs.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/emoji-thumbs.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/avatar-9.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/line-repeat.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/line-arrows.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/idea.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/hero/launch.png
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Ffeatures%2Fissues
[+] [a<href>] https://github.com/mobile
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/board-glow.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=2280&format=webpll 2280w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=1824&format=webpll 1824w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=1368&format=webpll 1368w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=1140&format=webpll 1140w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=912&format=webpll 912w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=456&format=webpll 456w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/layout-board.png 2280w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=1140 1140w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=912 912w,https://github.githubassets.com/images/modules/site/issues/layout-board.png?width=570 570w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/layout-board.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=2280&format=webpll 2280w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=1824&format=webpll 1824w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=1368&format=webpll 1368w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=1140&format=webpll 1140w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=912&format=webpll 912w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=456&format=webpll 456w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/layout-table.png 2280w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=1140 1140w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=912 912w,https://github.githubassets.com/images/modules/site/issues/layout-table.png?width=570 570w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/layout-table.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/logos/logo-shopify-mono.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/logos/logo-vercel.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/logos/logo-stripe.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/logos/logo-ford.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/logos/logo-nasa.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/issue-tasks-progress-reduced-motion.png
[#] [video<poster>] https://github.githubassets.com/images/modules/site/issues/issue-tasks-progress-placeholder.png
[#] [source<src>] https://github.githubassets.com/images/modules/site/issues/issue-tasks-progress.hevc.mp4
[#] [source<src>] https://github.githubassets.com/images/modules/site/issues/issue-tasks-progress.h264.mp4
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/event-1-avatar.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/avatar-bot.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/avatar-grrretel.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/avatar-chiedo.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/state-merged-icon.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/event-4-avatar.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/video-frame.webp
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/video-frame.png
[#] [video<poster>] https://github.githubassets.com/images/modules/site/issues/game-placeholder.jpg
[#] [source<src>] https://github.githubassets.com/images/modules/site/issues/game.mp4
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/avatar-preciselyalyss.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/state-open-icon.svg
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=1250&format=webpll 1250w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=1000&format=webpll 1000w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=750&format=webpll 750w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=625&format=webpll 625w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=500&format=webpll 500w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=250&format=webpll 250w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png 1250w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=625 625w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=500 500w,https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png?width=312 312w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/issues-plan.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=1250&format=webpll 1250w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=1000&format=webpll 1000w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=750&format=webpll 750w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=625&format=webpll 625w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=500&format=webpll 500w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=250&format=webpll 250w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png 1250w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=625 625w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=500 500w,https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png?width=312 312w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/issues-area.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=1250&format=webpll 1250w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=1000&format=webpll 1000w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=750&format=webpll 750w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=625&format=webpll 625w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=500&format=webpll 500w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=250&format=webpll 250w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png 1250w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=625 625w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=500 500w,https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png?width=312 312w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=1040&format=webpll 1040w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=832&format=webpll 832w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=624&format=webpll 624w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=520&format=webpll 520w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=416&format=webpll 416w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=208&format=webpll 208w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/command-palette.png 1040w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=520 520w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=416 416w,https://github.githubassets.com/images/modules/site/issues/command-palette.png?width=260 260w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/command-palette.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/issue-custom-fields-reduced-motion.jpg
[#] [video<poster>] https://github.githubassets.com/images/modules/site/issues/issue-custom-fields-placeholder.jpg
[#] [source<src>] https://github.githubassets.com/images/modules/site/issues/issue-custom-fields-v3.h264.mp4
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=1416&format=webpll 1416w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=1132&format=webpll 1132w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=849&format=webpll 849w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=708&format=webpll 708w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=566&format=webpll 566w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=283&format=webpll 283w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/custom-fields.png 1416w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=708 708w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=566 566w,https://github.githubassets.com/images/modules/site/issues/custom-fields.png?width=354 354w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/custom-fields.png
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/automations.png?width=2760&format=webpll 2760w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=2208&format=webpll 2208w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=1656&format=webpll 1656w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=1380&format=webpll 1380w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=1104&format=webpll 1104w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=552&format=webpll 552w
[#] [source<srcset>] https://github.githubassets.com/images/modules/site/issues/automations.png 2760w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=1380 1380w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=1104 1104w,https://github.githubassets.com/images/modules/site/issues/automations.png?width=690 690w
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/automations.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/issues-mobile-android.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/illo/issues-mobile-ios.png
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/shopify-testimonial.jpg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/logos/logo-shopify.svg
[#] [img<src>] https://github.githubassets.com/images/modules/site/issues/board-glow.png
[+] [a<href>] https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Ffeatures%2Fissues
[+] [a<href>] https://github.com/mobile
[+] [a<href>] https://github.com/
[+] [a<href>] https://resources.github.com/newsletter/
[+] [a<href>] https://github.com/features
[+] [a<href>] https://github.com/security
[+] [a<href>] https://github.com/team
[+] [a<href>] https://github.com/enterprise
[+] [a<href>] https://github.com/customer-stories?type=enterprise
[+] [a<href>] https://github.com/readme
[+] [a<href>] https://github.com/pricing
[+] [a<href>] https://resources.github.com
[+] [a<href>] https://github.com/github/roadmap
[+] [a<href>] https://resources.github.com/devops/tools/compare/
[+] [a<href>] https://docs.github.com/get-started/exploring-integrations/about-building-integrations
[+] [a<href>] https://partner.github.com
[+] [a<href>] https://www.electronjs.org
[+] [a<href>] https://desktop.github.com/
[+] [a<href>] https://docs.github.com
[+] [a<href>] https://github.community
[+] [a<href>] https://services.github.com/
[+] [a<href>] https://github.com/premium-support
[+] [a<href>] https://skills.github.com/
[+] [a<href>] https://www.githubstatus.com/
[+] [a<href>] https://support.github.com?tags=dotcom-footer
[+] [a<href>] https://github.com/about
[+] [a<href>] https://github.blog
[+] [a<href>] https://github.com/about/careers
[+] [a<href>] https://github.com/about/press
[+] [a<href>] https://github.com/about/diversity
[+] [a<href>] https://socialimpact.github.com/
[+] [a<href>] https://shop.github.com
[+] [a<href>] https://x.com/github
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/x.svg
[+] [a<href>] https://www.facebook.com/GitHub
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/facebook.svg
[+] [a<href>] https://www.linkedin.com/company/github
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/linkedin.svg
[+] [a<href>] https://www.youtube.com/github
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/youtube.svg
[+] [a<href>] https://www.twitch.tv/github
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/twitch.svg
[+] [a<href>] https://www.tiktok.com/@github
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/tiktok.svg
[+] [a<href>] https://github.com/github
[#] [img<src>] https://github.githubassets.com/images/modules/site/icons/footer/github-mark.svg
[+] [a<href>] https://docs.github.com/site-policy/github-terms/github-terms-of-service
[+] [a<href>] https://docs.github.com/site-policy/privacy-policies/github-privacy-statement
[+] [a<href>] https://github.com/github/site-policy/pull/582
[+] [a<href>] https://github.com/sitemap
[+] [a<href>] https://github.com/git-guides
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github-cloud.s3.amazonaws.com
[*] [link<href>] https://user-images.githubusercontent.com/
[*] [link<href>] https://github.githubassets.com
[*] [link<href>] https://avatars.githubusercontent.com
[*] [link<href>] https://github.githubassets.com/assets/light-b92e9647318f.css
[*] [link<href>] https://github.githubassets.com/assets/dark-5d486a4ede8e.css
[*] [link<href>] https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css
[*] [link<href>] https://github.githubassets.com/assets/primer-d6dcdf72e61d.css
[*] [link<href>] https://github.githubassets.com/assets/global-faa25eb56e2e.css
[*] [link<href>] https://github.githubassets.com/assets/github-933ef5369a60.css
[*] [script<src>] https://github.githubassets.com/assets/wp-runtime-e49d85e88ee7.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js
[*] [script<src>] https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js
[*] [script<src>] https://github.githubassets.com/assets/environment-fc6543d75794.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js
[*] [script<src>] https://github.githubassets.com/assets/github-elements-3485f2997bc6.js
[*] [script<src>] https://github.githubassets.com/assets/element-registry-981cc2eaa259.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js
[*] [script<src>] https://github.githubassets.com/assets/behaviors-464f50283c96.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js
[*] [script<src>] https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_delegated-events_di-94a48b-1bb8d005f757.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-677582870bfd.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_mini-throt-08ab15-28a3e371679d.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_filter-input_ts-11c4ac43bf80.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_ref-selector_ts-cad36de2ca60.js
[*] [script<src>] https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_settings_runner-groups_ts-app_-5e03dc-754c5af351eb.js
[*] [script<src>] https://github.githubassets.com/assets/settings-6899fc45ea3a.js
[*] [script<src>] https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-8311888324b2.js
[*] [script<src>] https://github.githubassets.com/assets/sessions-04ec2c51e991.js
[*] [script<src>] https://github.githubassets.com/assets/signup-9197d41c14b1.js
[*] [link<href>] https://github.githubassets.com/
[#] [link<href>] https://github.com/opensearch.xml
[#] [link<href>] https://github.com/fluidicon.png
[*] [link<href>] https://github.githubassets.com/assets/github-933ef5369a60.css
[*] [link<href>] https://github.com/login
[*] [link<href>] https://github.githubassets.com/pinned-octocat.svg
[#] [link<href>] https://github.githubassets.com/favicons/favicon.png
[*] [link<href>] https://github.githubassets.com/favicons/favicon.svg
[*] [link<href>] https://github.com/manifest.json
[+] [a<href>] https://github.com/mauricelambert/#start-of-content
[+] [a<href>] https://github.com/
[+] [form<action>] https://github.com/session
[+] [a<href>] https://github.com/password_reset
[+] [a<href>] https://github.com/signup?return_to=https%3A%2F%2Fgithub.com%2Fmauricelambert&source=login
[+] [a<href>] https://github.com/site/terms
[+] [a<href>] https://github.com/site/privacy
[+] [a<href>] https://docs.github.com/
[+] [a<href>] https://github.com/contact
[+]  99% |████████████████████|
~# 
"""

__version__ = "1.1.0"
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
Cr0wl3r  Copyright (C) 2023, 2024  Maurice Lambert
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

from logging import (
    basicConfig,
    debug,
    info,
    warning,
    error,
    critical,
    addLevelName,
    log,
)
from ssl import create_default_context, _create_unverified_context, SSLContext
from typing import Union, Set, List, Dict, Tuple, TypeVar, FrozenSet
from os.path import dirname, basename, normpath, join, exists
from urllib.parse import urlparse, ParseResult, quote
from http.client import HTTPResponse, IncompleteRead
from argparse import ArgumentParser, Namespace
from sys import exit, stderr, path as sys_path
from urllib.error import URLError, HTTPError
from collections import defaultdict, Counter
from urllib.request import urlopen, Request
from xml.etree.ElementTree import parse
from os import name, getcwd, makedirs
from http.cookies import SimpleCookie
from abc import ABC, abstractmethod
from html.parser import HTMLParser
from dataclasses import dataclass
from shutil import copyfileobj
from datetime import datetime
from time import sleep, time
from io import BytesIO
from json import dump
import logging


def download_requirements() -> None:
    filename = (
        "TerminalMessages.dll" if name == "nt" else "libTerminalMessages.so"
    )

    if exists(filename) and exists("TerminalMessagesInterface.py"):
        return None

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


try:
    download_requirements()
    sys_path.append(getcwd())
    from TerminalMessagesInterface import messagef
except ImportError:
    format_output: bool = False
else:
    format_output: bool = True

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

    def __init__(
        self, path: str = None, requested: bool = True, status: int = 200
    ):
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
    report: UrlReport
    readed: bool = False

    @property
    def status(self) -> int:
        return self.code

    @property
    def data(self) -> bytes:
        return self.response

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
        no_query_page: bool = False,
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
        self.urls_parsed: Set[str] = set()
        self.no_query_page = no_query_page
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

        url1 = parsed_url._replace(fragment="")
        url2 = url1._replace(query="")
        identifier_url = (url2 if self.no_query_page else url1).geturl()

        if request and identifier_url not in self.urls_parsed:
            self.urls_to_parse.add(url)
            self.urls_parsed.add(identifier_url)

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

        if type_ == "resource" or any(
            parsed_url.path.endswith(x) for x in extensions
        ):
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
        cross_domain_policy = parse(BytesIO(response.data)).getroot()
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
        urls_done.add(url)

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
            (
                (self.master_url.path + url.path)
                if self.master_url.path and self.master_url.path[-1] == "/"
                else (self.master_url.path + "/" + url.path)
            ),
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

        if writed or not self.store:
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
            info(
                "Do not request "
                + url
                + " response is write by previous crawls"
            )
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
        log(21, url)
        return response, url

    if selenium:
        _get_data = get_data

        def add_cookies(self) -> None:
            """
            This method adds cookie to selenium web driver.
            """

            if cookies_string := self.headers.get("Cookie"):
                cookies = SimpleCookie()
                cookies.load(cookies_string)

                for key, value in cookies.items():
                    driver.add_cookie({"name": key, "value": value})

        def get_data(
            self, url: ParseResult, first: bool
        ) -> Tuple[HttpResponse, str]:
            """
            This method gets the Web page content after javascript execution
            using selenium.
            """

            response, _ = self._get_data(url, first)
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
                    response.report,
                ),
                url,
            )


class _CrawlerPrinter(_Crawler):
    """
    ABC class for printers.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.printed: Set[str] = set()

    def should_print(self, url: str) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        parsed_url = urlparse(url)
        url1 = parsed_url._replace(fragment="")
        url2 = url1._replace(query="")
        identifier_url = (url2 if self.no_query_page else url1).geturl()

        if identifier_url in self.printed:
            return False

        self.printed.add(identifier_url)
        return True


if format_output:

    class CrawlerColoredPrinter(_CrawlerPrinter):
        """
        This class prints all URLs.
        """

        def get_pourcent(self):
            """
            This function returns the pourcents of URL requested.
            """

            divid = self.max_request or (
                len(self.urls_to_parse) + len(self.urls_parsed)
            )
            if divid == 0:
                return 0

            pourcent = round(self.counter / divid * 100)

            if pourcent == 100:
                return 99

            return pourcent

        def handle_web_page(
            self, from_url: str, url: str, tag: str, attribute: str
        ) -> Union[bool, None]:
            """
            This method prints the URL found.
            """

            if not self.should_print(url):
                messagef(
                    from_url, "OK", self.get_pourcent(), oneline_progress=True
                )
                return None

            messagef(f"[{tag}<{attribute}>] {url}", "OK", self.get_pourcent())

        def handle_static(
            self, from_url: str, url: str, tag: str, attribute: str
        ) -> Union[bool, None]:
            """
            This method prints the URL found.
            """

            if not self.should_print(url):
                messagef(
                    from_url,
                    "INFO",
                    self.get_pourcent(),
                    oneline_progress=True,
                )
                return None

            messagef(
                f"[{tag}<{attribute}>] {url}", "INFO", self.get_pourcent()
            )

        def handle_resource(
            self, from_url: str, url: str, tag: str, attribute: str
        ) -> Union[bool, None]:
            """
            This method prints the URL found.
            """

            if not self.should_print(url):
                messagef(
                    from_url,
                    "TODO",
                    self.get_pourcent(),
                    oneline_progress=True,
                )
                return None

            messagef(
                f"[{tag}<{attribute}>] {url}", "TODO", self.get_pourcent()
            )


class CrawlerRawPrinter(_CrawlerPrinter):
    """
    This class prints all URLs.
    """

    def handle_web_page(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        if not self.should_print(url):
            return None

        print("[+]", tag, attribute, url)

    def handle_static(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        if not self.should_print(url):
            return None

        print("[*]", tag, attribute, url)

    def handle_resource(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        if not self.should_print(url):
            return None

        print("[#]", tag, attribute, url)


class CrawlerRawUrlOnlyPrinter(_CrawlerPrinter):
    """
    This class prints all URLs.
    """

    def handle_web_page(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        if not self.should_print(url):
            return None

        print(url)

    def handle_static(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        if not self.should_print(url):
            return None

        print(url)

    def handle_resource(
        self, from_url: str, url: str, tag: str, attribute: str
    ) -> Union[bool, None]:
        """
        This method prints the URL found.
        """

        if not self.should_print(url):
            return None

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
            "Do not request only the base URL domain (request all domains)."
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
        help="Add cookies.",
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
        help="WebCrawler logs level.",
        default="WARNING",
        choices=["DEBUG", "INFO", "REQUEST", "WARNING", "ERROR", "CRITICAL"],
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
        choices=(
            {"raw", "raw-url-only", "colored"}
            if format_output
            else {"raw", "raw-url-only", "colored"}
        ),
        help="Output format.",
    )
    add(
        "--no-query-page",
        "--no-query",
        "-q",
        default=False,
        action="store_true",
        help=(
            "Request only when path is different, without this option the same"
            " path will be requested for each differents queries."
        ),
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

    addLevelName(21, "REQUEST")
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
        headers["Cookie"] = cookies

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
        no_query_page=arguments.no_query_page,
    )

    try:
        copy.crawl()
    except (ContentTypeError, CriticalUrllibError):
        print(
            "Critical exception on the first request"
            ", there is nothing to crawl....",
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
