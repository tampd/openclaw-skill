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

## 2. Calendar (Lịch)
```bash
# Xem lịch hôm nay
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar events primary --today

# Xem lịch tuần này
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar events primary --week

# Xem lịch khoảng thời gian cụ thể
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar events primary --from "2026-03-17T00:00:00+07:00" --to "2026-03-17T23:59:59+07:00"

# Tạo sự kiện (NOTE: dùng --summary, --from, --to — KHÔNG dùng --title, --start, --end)
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar create primary --summary "Họp team" --from "2026-03-15T09:00:00+07:00" --to "2026-03-15T10:00:00+07:00"

# Tạo sự kiện + nhắc trước 30 phút + địa điểm
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar create primary --summary "Họp khách hàng" --from "2026-03-18T14:00:00+07:00" --to "2026-03-18T15:00:00+07:00" --reminder popup:30m --location "Phòng họp A"

# Tìm sự kiện
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar search "họp" --from today --days 7

# Xóa sự kiện (cần eventId — lấy từ events list --json)
/root/openclaw/workspace/scripts/gog_wrapper.sh calendar delete primary <eventId> --force

# Xem đầy đủ options:
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
