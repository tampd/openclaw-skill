---
name: agent-browser
description: Headless browser cho Tôm — truy cập web, điền form, screenshot, scrape dữ liệu từ portal/website.
---

# Agent Browser — Trình Duyệt AI

## Mục đích
Cho phép Tôm truy cập web portal, kiểm tra website, screenshot, scrape dữ liệu — bổ sung cho `web-researcher`.

## Khi nào kích hoạt
- User nói: "mở trang", "kiểm tra website", "screenshot", "kiểm tra SSL"
- Cần đăng nhập portal, kiểm tra WHOIS, test trang web
- `web-researcher` không đủ (cần JavaScript rendering)

## Công cụ (chọn 1)

### Option A: Playwright (khuyến nghị)
```bash
# Cài đặt
pip3 install --break-system-packages playwright
playwright install chromium

# Screenshot trang web
python3 -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://blog.chaiko.info')
    page.screenshot(path='/tmp/screenshot.png')
    print(page.title())
    browser.close()
"

# Đọc nội dung trang (có JS rendering)
python3 -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('$URL')
    print(page.inner_text('body')[:3000])
    browser.close()
"
```

### Option B: Curl nâng cao (không cần cài thêm)
```bash
# Kiểm tra SSL cert
echo | openssl s_client -connect blog.chaiko.info:443 -servername blog.chaiko.info 2>/dev/null | openssl x509 -noout -dates -subject -issuer

# WHOIS domain
whois chaiko.info | head -30

# Check HTTP headers
curl -sI https://blog.chaiko.info | head -15

# Check page load time
curl -sL -o /dev/null -w "DNS: %{time_namelookup}s\nConnect: %{time_connect}s\nTTFB: %{time_starttransfer}s\nTotal: %{time_total}s\n" https://blog.chaiko.info
```

## Kết hợp với skills khác
- `web-researcher`: Browser cho JS-heavy sites, web-researcher cho API/static
- `blog-auditor`: Browser kiểm tra UI/UX, auditor kiểm tra nội dung
- `devops-toolkit`: Browser kiểm tra endpoints, devops kiểm tra ports

## Quy tắc
- ✅ Có thể screenshot và đọc public websites
- ⚠️ Confirm trước khi điền form hoặc click buttons
- ❌ KHÔNG tự đăng nhập vào accounts mà chưa được phép
- ❌ KHÔNG scrape quá 100 pages/lần (respect robots.txt)
