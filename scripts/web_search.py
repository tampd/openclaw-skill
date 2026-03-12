#!/usr/bin/env python3
"""
web_search.py — Search the web from command line (no API key needed).
Uses DuckDuckGo HTML search as primary, with fallback methods.

Usage:
    python3 web_search.py "search query" [--num 5] [--lang vi] [--json]

Output: List of search results with title, URL, and snippet.
"""

import sys
import json
import argparse
import re
import urllib.parse
import traceback

import requests
from bs4 import BeautifulSoup


# --- Config ---
REQUEST_TIMEOUT = 12
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


def search_duckduckgo_html(query: str, num_results: int = 5, lang: str = "vi") -> list:
    """
    Search DuckDuckGo via HTML (no API key needed).
    Returns list of {title, url, snippet}.
    """
    params = {
        "q": query,
        "kl": f"{lang}-vn" if lang == "vi" else f"{lang}-us",
        "df": "",
    }
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html",
        "Accept-Language": f"{lang},en;q=0.9",
    }

    url = "https://html.duckduckgo.com/html/"
    resp = requests.post(url, data=params, headers=headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    results = []

    for item in soup.select(".result"):
        title_el = item.select_one(".result__a")
        snippet_el = item.select_one(".result__snippet")

        if not title_el:
            continue

        title = title_el.get_text(strip=True)
        href = title_el.get("href", "")

        # DDG wraps URLs in redirect — extract actual URL
        actual_url = href
        if "uddg=" in href:
            match = re.search(r"uddg=([^&]+)", href)
            if match:
                actual_url = urllib.parse.unquote(match.group(1))

        snippet = snippet_el.get_text(strip=True) if snippet_el else ""

        if title and actual_url and not actual_url.startswith("//duckduckgo"):
            results.append({
                "title": title,
                "url": actual_url,
                "snippet": snippet,
            })

        if len(results) >= num_results:
            break

    return results


def search_duckduckgo_lite(query: str, num_results: int = 5) -> list:
    """
    Fallback: DuckDuckGo Lite (even simpler HTML).
    """
    params = {"q": query}
    headers = {"User-Agent": USER_AGENT}

    url = "https://lite.duckduckgo.com/lite/"
    resp = requests.post(url, data=params, headers=headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    results = []

    # Lite version uses tables
    for link in soup.select("a.result-link"):
        title = link.get_text(strip=True)
        href = link.get("href", "")
        if title and href and href.startswith("http"):
            results.append({
                "title": title,
                "url": href,
                "snippet": "",
            })
        if len(results) >= num_results:
            break

    return results


def search_google_scrape(query: str, num_results: int = 5, lang: str = "vi") -> list:
    """
    Fallback: Google search via curl-like scraping.
    May be blocked by CAPTCHA — use as last resort.
    """
    params = {
        "q": query,
        "hl": lang,
        "num": num_results + 3,
    }
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html",
    }

    url = "https://www.google.com/search"
    resp = requests.get(url, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    results = []

    for g in soup.select("div.g"):
        title_el = g.select_one("h3")
        link_el = g.select_one("a[href]")
        snippet_el = g.select_one("div.VwiC3b") or g.select_one("span.aCOpRe")

        if not title_el or not link_el:
            continue

        href = link_el.get("href", "")
        if not href.startswith("http"):
            continue

        results.append({
            "title": title_el.get_text(strip=True),
            "url": href,
            "snippet": snippet_el.get_text(strip=True) if snippet_el else "",
        })

        if len(results) >= num_results:
            break

    return results


def format_results(results: list, query: str, as_json: bool = False) -> str:
    """Format search results for display."""
    if as_json:
        return json.dumps({"query": query, "results": results}, ensure_ascii=False, indent=2)

    if not results:
        return f'❌ Không tìm thấy kết quả cho: "{query}"'

    lines = [f'🔍 **Kết quả tìm kiếm: "{query}"**', ""]

    for i, r in enumerate(results, 1):
        lines.append(f"**{i}. [{r['title']}]({r['url']})**")
        if r["snippet"]:
            lines.append(f"   {r['snippet'][:200]}")
        lines.append("")

    lines.append(f"📊 Tổng: {len(results)} kết quả")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Web search from command line")
    parser.add_argument("query", help="Search query")
    parser.add_argument(
        "--num", type=int, default=5, help="Number of results (default: 5)"
    )
    parser.add_argument(
        "--lang", default="vi", help="Language code (default: vi)"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output as JSON"
    )
    parser.add_argument(
        "--engine",
        choices=["ddg", "ddg-lite", "google", "auto"],
        default="auto",
        help="Search engine (default: auto)",
    )
    args = parser.parse_args()

    results = []
    errors = []

    engines = {
        "ddg": ("DuckDuckGo", lambda: search_duckduckgo_html(args.query, args.num, args.lang)),
        "ddg-lite": ("DuckDuckGo Lite", lambda: search_duckduckgo_lite(args.query, args.num)),
        "google": ("Google", lambda: search_google_scrape(args.query, args.num, args.lang)),
    }

    if args.engine == "auto":
        order = ["ddg", "ddg-lite", "google"]
    else:
        order = [args.engine]

    for engine_key in order:
        name, search_fn = engines[engine_key]
        try:
            results = search_fn()
            if results:
                break
            errors.append(f"{name}: 0 kết quả")
        except requests.exceptions.Timeout:
            errors.append(f"{name}: timeout")
        except requests.exceptions.HTTPError as e:
            errors.append(f"{name}: HTTP {e.response.status_code}")
        except Exception as e:
            errors.append(f"{name}: {str(e)[:80]}")

    if not results and errors:
        print(f"⚠️ Lỗi tìm kiếm: {'; '.join(errors)}", file=sys.stderr)

    print(format_results(results, args.query, as_json=args.json))


if __name__ == "__main__":
    main()
