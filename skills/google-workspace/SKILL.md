---
name: google-workspace
description: Tích hợp Google Workspace — Gmail, Calendar, Drive, Contacts, Sheets, Docs qua CLI. DÙNG CLI, KHÔNG DÙNG BROWSER.
---

# Google Workspace Integration

## Mục đích
Kết nối Sếp với Google Workspace (Gmail, Calendar, Drive, Sheets, Docs).

## ⚠️ QUY TẮC TỐI THƯỢNG (CRITICAL)
- **TUYỆT ĐỐI KHÔNG** dùng `agent-browser` hoặc Browser Relay để vào web Google.
- **BẮT BUỘC** dùng script CLI `/root/openclaw/workspace/scripts/gog_wrapper.sh` cho mọi thao tác.

## 1. Gmail
```bash
# Tìm email gần đây
/root/openclaw/workspace/scripts/gog_wrapper.sh gmail search 'newer_than:7d' --max 10

# Gửi email
/root/openclaw/workspace/scripts/gog_wrapper.sh gmail send --to recipient@email.com --subject "Tiêu đề" --body "Nội dung"
```

## 2. Calendar (Tạo Lịch)
```bash
# Xem lịch hôm nay
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar events primary --from $(date -u +%Y-%m-%dT00:00:00Z) --to $(date -u +%Y-%m-%dT23:59:59Z)

# Tạo lịch (Ví dụ tạo lịch: 09:00 - 10:00 ngày 15/03/2026)
# NOTE: Luôn dùng format ISO 8601 kèm múi giờ +07:00
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar create primary --title "Họp team" --start "2026-03-15T09:00:00+07:00" --end "2026-03-15T10:00:00+07:00"

# Nếu có nhắc trước (ví dụ 2 ngày trước sự kiện = thêm options vào nội dung lịch hoặc description)
# Cú pháp đầy đủ có thể xem bằng:
# /root/openclaw/workspace/scripts/gog_wrapper.sh calendar create --help
```

## 3. Drive & Sheets
```bash
# Tìm file
/root/openclaw/workspace/scripts/gog_wrapper.sh drive search "báo giá" --max 10

# Đọc Sheets
/root/openclaw/workspace/scripts/gog_wrapper.sh sheets get <sheetId> "Sheet1!A1:D10" --json
```

## Quy tắc
- ✅ Luôn gọi /root/openclaw/workspace/scripts/gog_wrapper.sh
- ❌ KHÔNG BAO GIỜ yêu cầu user bật Browser Relay để đọc email hay tạo lịch!
