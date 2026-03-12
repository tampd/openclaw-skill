# TOOLS.md - Local Notes

## VPS (Máy chủ hiện tại)

> ⚠️ **QUAN TRỌNG**: Bạn đang chạy TRỰC TIẾP trên VPS này. Mọi lệnh terminal đều chạy trên máy localhost.
> Khi user yêu cầu "kiểm tra VPS" → chạy lệnh ngay, KHÔNG cần hỏi IP hay hostname.

- **Hostname**: localhost (chính máy này)
- **OS**: Ubuntu Linux
- **User**: root
- **OpenClaw path**: `/root/openclaw/`
- **Workspace path**: `/root/openclaw/workspace/`
- **Blog**: blog.chaiko.info (WordPress)
- **GCP Project**: duytam-n8n (Vertex AI)

## Khả năng của bạn

### Có thể làm ngay (không cần hỏi):
- Chạy lệnh shell: `free -m`, `df -h`, `uptime`, `ls`, `cat`, `find`, `grep`
- Đọc/ghi file trong workspace
- Tạo cron jobs
- Gọi API bằng `curl`

### Không có trình duyệt (nhưng có scripts nâng cao):
- ❌ **Trình duyệt web** — không thể mở browser trực tiếp
- ✅ **Thay thế**: Dùng Python scripts trong `scripts/`:
  - `python3 scripts/web_search.py "query"` — tìm kiếm web (DuckDuckGo)
  - `python3 scripts/web_fetch.py "URL"` — đọc & trích nội dung trang web
  - `curl -sL URL | python3 -m json.tool` — cho API/JSON endpoints

### Cần hỏi trước:
- Xóa file bên ngoài workspace
- Restart service
- Gửi email/tin nhắn public

## WordPress (blog.chaiko.info)
- **API Endpoint**: `https://blog.chaiko.info/wp-json/wp/v2/posts`
- **Credentials file**: `/root/openclaw/workspace/wp_credentials.txt`
- Dùng `curl` để gọi WordPress REST API

## Timezone
- Server timezone: UTC
- User timezone: **GMT+7 (Việt Nam)**
- Khi user nói "3h chiều" = 15:00 GMT+7 = 08:00 UTC

## AI Models
- **Mặc định**: `openai-codex/gpt-5.4` (ChatGPT Team, thinking model — thông minh nhất)
- **Có sẵn**: `openai-codex/gpt-4o`, `google-vertex/gemini-2.5-flash`, `google-vertex/gemini-2.5-pro`
- **Auth**: OAuth Codex (gptinfo@bkns.vn) — token tự refresh
- Model được cấu hình trong `/root/openclaw/.openclaw/openclaw.json`
- Khi ChatGPT hết quota → đổi primary sang `google-vertex/gemini-2.5-flash` rồi restart

## Telegram
- **Sếp Telegram ID**: `882968821`
- **Telegram target**: `telegram:882968821` (dùng trong cron jobs để gửi tin nhắn)
- **Bot ID**: `8755389014`
