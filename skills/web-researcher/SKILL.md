---
name: web-researcher
description: Tìm kiếm Internet, tóm tắt URL/bài viết, nghiên cứu chủ đề chuyên sâu. Dùng scripts nâng cao thay thế curl thô.
---

# Web Researcher — Trợ Lý Nghiên Cứu Internet

## Mục đích
Giúp user nghiên cứu thông tin trên Internet nhanh chóng, chính xác, và có cấu trúc. Dùng scripts Python nâng cao thay vì `curl | sed` thô.

## ⚠️ QUAN TRỌNG: Không có trình duyệt

> Bạn **KHÔNG CÓ** trình duyệt web. KHÔNG BAO GIỜ thử mở browser hay browse tool.
> Thay vào đó, dùng **scripts Python** trong `/root/openclaw/workspace/scripts/`:

## 🛠️ Công Cụ Chính

### 1. `web_fetch.py` — Đọc & trích nội dung trang web
```bash
# Đọc link, trích nội dung chính (bài viết, docs...)
python3 /root/openclaw/workspace/scripts/web_fetch.py "https://example.com"

# Giới hạn độ dài output
python3 /root/openclaw/workspace/scripts/web_fetch.py "https://example.com" --max-chars 5000

# Output JSON (title, author, date, content)
python3 /root/openclaw/workspace/scripts/web_fetch.py "https://example.com" --json

# Chỉ lấy metadata (title, description, headings)
python3 /root/openclaw/workspace/scripts/web_fetch.py "https://example.com" --meta-only

# Lấy HTML thô (debug)
python3 /root/openclaw/workspace/scripts/web_fetch.py "https://example.com" --raw
```

### 2. `web_search.py` — Tìm kiếm web
```bash
# Tìm kiếm (mặc định: DuckDuckGo, 5 kết quả, tiếng Việt)
python3 /root/openclaw/workspace/scripts/web_search.py "từ khóa tìm kiếm"

# Nhiều kết quả hơn
python3 /root/openclaw/workspace/scripts/web_search.py "query" --num 8

# Tìm tiếng Anh
python3 /root/openclaw/workspace/scripts/web_search.py "query" --lang en

# Output JSON
python3 /root/openclaw/workspace/scripts/web_search.py "query" --json

# Chọn engine cụ thể
python3 /root/openclaw/workspace/scripts/web_search.py "query" --engine ddg
python3 /root/openclaw/workspace/scripts/web_search.py "query" --engine google
```

### 3. `curl` — Fallback khi scripts fail
```bash
# API / JSON endpoints (curl vẫn tốt nhất cho API)
curl -sL "https://api.example.com/data" | python3 -m json.tool

# Trang đơn giản
curl -sL "https://example.com" | python3 -c "
import sys, html2text
h = html2text.HTML2Text()
h.ignore_images = True
h.body_width = 0
print(h.handle(sys.stdin.read())[:3000])
"

# Download file
wget -q "https://example.com/file.pdf" -O /tmp/file.pdf
```

## Các Chế Độ Hoạt Động

### 1. Tóm tắt URL
**Trigger**: User gửi link hoặc nói "tóm tắt link này"

**Quy trình**:
1. Chạy `web_fetch.py` → lấy nội dung sạch
2. Đọc output, tóm tắt 3-5 điểm chính
3. Trả lời format Telegram

```bash
python3 /root/openclaw/workspace/scripts/web_fetch.py "[URL]" --max-chars 4000
```

**Format trả lời**:
```
📄 **Tóm tắt**: [Tiêu đề bài viết]
🔗 Nguồn: [URL]

**Điểm chính:**
1. [Ý chính 1]
2. [Ý chính 2]
3. [Ý chính 3]

**Kết luận:** [1-2 câu kết luận]
```

### 2. Research Chủ Đề
**Trigger**: "Tìm hiểu về...", "Research về...", "So sánh X và Y"

**Quy trình**:
1. `web_search.py` → tìm top kết quả
2. `web_fetch.py` → đọc 2-3 link hay nhất
3. Tổng hợp thành báo cáo

```bash
# Bước 1: Search
python3 /root/openclaw/workspace/scripts/web_search.py "chủ đề research" --num 6

# Bước 2: Đọc chi tiết từ top results
python3 /root/openclaw/workspace/scripts/web_fetch.py "[URL-1]" --max-chars 3000
python3 /root/openclaw/workspace/scripts/web_fetch.py "[URL-2]" --max-chars 3000
```

**Format trả lời**:
```
🔍 **Báo cáo Research: [Chủ đề]**

## TL;DR
- [2-3 bullet points]

## Chi tiết
### [Khía cạnh 1]
[Nội dung]

### [Khía cạnh 2]
[Nội dung]

## Nguồn tham khảo
1. [Tên nguồn](URL) — [Ghi chú]
2. [Tên nguồn](URL) — [Ghi chú]
```

### 3. Tin Tức / Xu Hướng
**Trigger**: "Tin mới nhất về...", "Xu hướng AI hôm nay"

```bash
python3 /root/openclaw/workspace/scripts/web_search.py "tin tức [chủ đề] 2026" --num 8
```

**Format trả lời**:
```
📰 **Tin tức [Lĩnh vực] — [Ngày]**

1. 🔴 **[Tin hot nhất]**
   [Tóm tắt] — [Nguồn]

2. 🟡 **[Tin đáng chú ý]**
   [Tóm tắt] — [Nguồn]
```

## 🔧 Troubleshooting

| Lỗi | Nguyên nhân | Giải pháp |
|---|---|---|
| `Timeout` | Server chậm | Thử lại hoặc dùng `curl -sL --connect-timeout 10` |
| `HTTP 403` | Bị block | Dùng `--engine google` hoặc thử URL khác |
| `HTTP 429` | Rate limited | Chờ 30s rồi thử lại |
| `Không trích xuất được` | JS-heavy site | Dùng `--meta-only` hoặc tìm API/docs thay thế |
| `ImportError` | Thiếu thư viện | `pip3 install --break-system-packages trafilatura html2text beautifulsoup4` |
| DDG 0 kết quả | DDG bị block/maintenance | Script tự chuyển sang DDG Lite → Google |

## Lưu Kết Quả Research
```bash
mkdir -p /root/openclaw/workspace/research
# Lưu tại: research/[topic]-[YYYY-MM-DD].md
```

## Nguyên tắc
- ✅ **Luôn trích dẫn nguồn** — không bịa thông tin
- ✅ **Ưu tiên nguồn chính thức** — docs, GitHub, trang chủ > blog cá nhân > forum
- ✅ **Scripts trước, curl sau** — dùng `web_fetch.py` và `web_search.py` trước khi fallback `curl`
- ✅ **Cảnh báo khi thông tin lỗi thời** (> 6 tháng tuổi)
- ✅ **Viết tiếng Việt**, giữ thuật ngữ kỹ thuật tiếng Anh
- ✅ **Giới hạn output** — tóm gọn ≤30 dòng cho Telegram
- ❌ **KHÔNG mở browser** — chỉ dùng CLI tools
- ❌ **KHÔNG gửi raw HTML** cho user — luôn parse thành text sạch
