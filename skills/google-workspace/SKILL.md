---
name: google-workspace
description: Tích hợp Google Workspace — Gmail, Calendar, Drive, Contacts, Sheets, Docs qua CLI gog.
---

# Google Workspace Integration

## Mục đích
Kết nối Tôm với Google Workspace (Gmail, Calendar, Drive, Sheets, Docs) qua CLI `gog`.

## Khi nào kích hoạt
- User nói: "email", "gmail", "lịch", "calendar", "drive", "spreadsheet", "google docs"
- User muốn gửi/đọc email, quản lý lịch, truy cập Drive, tạo spreadsheet

## Setup (cần cài 1 lần)
```bash
# Cài gog CLI
pip3 install --break-system-packages gogcli || brew install steipete/tap/gogcli

# Setup OAuth
gog auth credentials /path/to/client_secret.json
gog auth add phamduytam@gmail.com --services gmail,calendar,drive,contacts,sheets,docs
gog auth list
```

## Gmail
```bash
# Tìm email gần đây
gog gmail search 'newer_than:7d' --max 10

# Gửi email
gog gmail send --to recipient@email.com --subject "Tiêu đề" --body "Nội dung"

# Đọc email cụ thể
gog gmail read <messageId>
```

## Calendar
```bash
# Xem lịch hôm nay
gog calendar events primary --from $(date -u +%Y-%m-%dT00:00:00Z) --to $(date -u +%Y-%m-%dT23:59:59Z)

# Tạo event
gog calendar create primary --title "Họp team" --start "2026-03-13T09:00:00+07:00" --end "2026-03-13T10:00:00+07:00"
```

## Drive
```bash
# Tìm file
gog drive search "báo giá" --max 10

# Upload file
gog drive upload /path/to/file.pdf

# Download file
gog drive download <fileId> --out /tmp/file.pdf
```

## Sheets
```bash
# Đọc data
gog sheets get <sheetId> "Sheet1!A1:D10" --json

# Ghi data
gog sheets update <sheetId> "Sheet1!A1:B2" --values-json '[["Name","Price"],["VPS","500000"]]' --input USER_ENTERED

# Thêm dòng mới
gog sheets append <sheetId> "Sheet1!A:C" --values-json '[["x","y","z"]]' --insert INSERT_ROWS
```

## Docs
```bash
# Đọc nội dung Google Doc
gog docs cat <docId>

# Export
gog docs export <docId> --format txt --out /tmp/doc.txt
```

## Kết hợp với office-assistant
- Khi soạn email → dùng `gog gmail send` thay vì chỉ draft text
- Khi tạo báo giá → có thể ghi vào Google Sheets
- Khi ghi meeting → sync với Google Calendar

## Quy tắc
- ✅ Confirm trước khi gửi email hoặc tạo event
- ✅ Set `GOG_ACCOUNT=phamduytam@gmail.com` trong .env
- ❌ KHÔNG đọc email private mà không hỏi Sếp trước
