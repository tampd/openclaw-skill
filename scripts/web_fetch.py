#!/usr/bin/env python3
"""
web_fetch.py — Fetch & extract clean content from a URL.
Used by OpenClaw (Tôm) as a replacement for raw `curl | sed`.

Usage:
    python3 web_fetch.py <URL> [--max-chars 3000] [--raw] [--json]

Output: Clean markdown text of the article/page content.
"""

import sys
import json
import argparse
import traceback

import requests
import trafilatura
import html2text
from bs4 import BeautifulSoup


# --- Config ---
DEFAULT_MAX_CHARS = 3000
REQUEST_TIMEOUT = 15
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "vi,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}


def fetch_html(url: str) -> str:
    """Fetch HTML content from URL with proper headers."""
    resp = requests.get(
        url,
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT,
        allow_redirects=True,
        verify=True,
    )
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or "utf-8"
    return resp.text


def extract_with_trafilatura(html: str, url: str) -> dict | None:
    """Extract article content using trafilatura (best quality)."""
    result = trafilatura.extract(
        html,
        url=url,
        include_comments=False,
        include_tables=True,
        include_links=True,
        include_images=False,
        output_format="txt",
        favor_recall=True,
    )
    if not result or len(result.strip()) < 50:
        return None

    metadata = trafilatura.extract(
        html, url=url, output_format="json", include_comments=False
    )
    meta = {}
    if metadata:
        try:
            meta = json.loads(metadata)
        except (json.JSONDecodeError, TypeError):
            pass

    return {
        "title": meta.get("title", ""),
        "author": meta.get("author", ""),
        "date": meta.get("date", ""),
        "content": result.strip(),
        "method": "trafilatura",
    }


def extract_with_html2text(html: str, url: str) -> dict | None:
    """Fallback: convert HTML to markdown using html2text."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0  # No wrapping
    h.skip_internal_links = True
    h.inline_links = True

    text = h.handle(html)
    if not text or len(text.strip()) < 50:
        return None

    # Extract title from HTML
    soup = BeautifulSoup(html, "lxml")
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    return {
        "title": title,
        "author": "",
        "date": "",
        "content": text.strip(),
        "method": "html2text",
    }


def extract_metadata_bs4(html: str) -> dict:
    """Extract basic metadata using BeautifulSoup."""
    soup = BeautifulSoup(html, "lxml")
    meta = {}

    # Title
    title_tag = soup.find("title")
    meta["title"] = title_tag.get_text(strip=True) if title_tag else ""

    # Meta description
    desc_tag = soup.find("meta", attrs={"name": "description"})
    if desc_tag:
        meta["description"] = desc_tag.get("content", "")

    # OG tags
    og_title = soup.find("meta", attrs={"property": "og:title"})
    if og_title and not meta["title"]:
        meta["title"] = og_title.get("content", "")

    og_desc = soup.find("meta", attrs={"property": "og:description"})
    if og_desc and "description" not in meta:
        meta["description"] = og_desc.get("content", "")

    # Headings overview
    headings = []
    for h in soup.find_all(["h1", "h2", "h3"], limit=10):
        headings.append(f"{h.name}: {h.get_text(strip=True)}")
    meta["headings"] = headings

    return meta


def truncate(text: str, max_chars: int) -> str:
    """Truncate text to max_chars at a clean break point."""
    if len(text) <= max_chars:
        return text
    # Find last newline before max_chars
    cut = text[:max_chars].rfind("\n")
    if cut < max_chars * 0.5:
        cut = max_chars
    return text[:cut] + f"\n\n[... cắt bớt, tổng {len(text)} ký tự]"


def main():
    parser = argparse.ArgumentParser(description="Fetch & extract web content")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument(
        "--max-chars",
        type=int,
        default=DEFAULT_MAX_CHARS,
        help=f"Max output chars (default: {DEFAULT_MAX_CHARS})",
    )
    parser.add_argument(
        "--raw", action="store_true", help="Output raw HTML (for debugging)"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output as JSON"
    )
    parser.add_argument(
        "--meta-only", action="store_true", help="Only extract metadata"
    )
    args = parser.parse_args()

    try:
        html = fetch_html(args.url)
    except requests.exceptions.Timeout:
        print(f"❌ Timeout: Server không phản hồi trong {REQUEST_TIMEOUT}s", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code} — {args.url}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print(f"❌ Không thể kết nối đến: {args.url}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Lỗi fetch: {e}", file=sys.stderr)
        sys.exit(1)

    if args.raw:
        print(html[:args.max_chars])
        return

    if args.meta_only:
        meta = extract_metadata_bs4(html)
        if args.json:
            print(json.dumps(meta, ensure_ascii=False, indent=2))
        else:
            print(f"📄 **{meta.get('title', 'N/A')}**")
            if meta.get("description"):
                print(f"📝 {meta['description']}")
            if meta.get("headings"):
                print("\n📑 Headings:")
                for h in meta["headings"]:
                    print(f"  - {h}")
        return

    # Try extraction methods in order
    result = extract_with_trafilatura(html, args.url)
    if not result:
        result = extract_with_html2text(html, args.url)
    if not result:
        print("❌ Không thể trích xuất nội dung từ trang này.", file=sys.stderr)
        # Fallback: show metadata
        meta = extract_metadata_bs4(html)
        print(f"📄 **{meta.get('title', 'N/A')}**")
        if meta.get("description"):
            print(f"📝 {meta['description']}")
        sys.exit(0)

    content = truncate(result["content"], args.max_chars)

    if args.json:
        result["content"] = content
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if result["title"]:
            print(f"📄 **{result['title']}**")
        if result["author"]:
            print(f"✍️ {result['author']}", end="")
            if result["date"]:
                print(f" — {result['date']}")
            else:
                print()
        elif result["date"]:
            print(f"📅 {result['date']}")
        print(f"🔗 {args.url}")
        print(f"⚙️ Method: {result['method']}")
        print(f"---")
        print(content)


if __name__ == "__main__":
    main()
