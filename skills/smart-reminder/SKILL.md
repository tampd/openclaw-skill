---
name: smart-reminder
description: Quản lý nhắc nhở, lịch hẹn, deadline thông minh với context. Hỗ trợ cú pháp tự nhiên tiếng Việt. Sử dụng cron main-session để đảm bảo tin nhắn gửi đúng kênh.
---

# Smart Reminder — Trợ Lý Nhắc Lịch Thông Minh

## Mục đích
Giúp user quản lý thời gian hiệu quả. Nhận yêu cầu bằng ngôn ngữ tự nhiên (tiếng Việt), tạo và quản lý nhắc nhở tự động.

## ⚠️ QUY TẮC QUAN TRỌNG

### Về thời gian
> **CRITICAL**: User ở timezone **GMT+7 (Việt Nam)**. Server chạy **UTC**.
> Khi user nói "30 phút nữa" → tính từ LÚC NÀY + 30 phút.
> KHÔNG ĐƯỢC nhắc sớm hơn thời gian đã hẹn. Nhắc sớm = BUG NGHIÊM TRỌNG.

### Về phương pháp nhắc (CRITICAL — ĐỌC KỸ)
> ⚠️ **KHÔNG DÙNG SUB-AGENT** để gửi nhắc nhở! Sub-agent không có chat context → tin nhắn sẽ THẤT BẠI.
> 
> Thay vào đó, dùng một trong hai cách:
> 1. **Cách 1 (Ưu tiên): Cron job `main-session`** — nhắc nhở chạy trong session chính, có sẵn chat context
> 2. **Cách 2 (Fallback): Ghi file + Heartbeat check** — ghi reminder vào file, heartbeat sẽ đọc và nhắc

## Cách tính thời gian đúng

### Bước 1: Lấy giờ hiện tại
```bash
# Giờ UTC (server)
date -u "+%Y-%m-%d %H:%M:%S UTC"

# Giờ VN (user)  
TZ='Asia/Ho_Chi_Minh' date "+%Y-%m-%d %H:%M:%S VN"
```

### Bước 2: Tính thời điểm nhắc
```bash
# Ví dụ: "nhắc sau 30 phút"
NOW_UTC=$(date -u +%s)
REMIND_UTC=$((NOW_UTC + 1800))  # +30 phút = +1800 giây

# Chuyển sang cron format (UTC)
REMIND_MIN=$(date -u -d @$REMIND_UTC +%M)
REMIND_HOUR=$(date -u -d @$REMIND_UTC +%H)
REMIND_DAY=$(date -u -d @$REMIND_UTC +%d)
REMIND_MONTH=$(date -u -d @$REMIND_UTC +%m)
echo "Cron schedule (UTC): $REMIND_MIN $REMIND_HOUR $REMIND_DAY $REMIND_MONTH *"
```

### Quy đổi giờ VN → UTC
| User nói | Giờ VN | Giờ UTC (cron) |
|----------|--------|----------------|
| "8h sáng" | 08:00 | 01:00 |
| "12h trưa" | 12:00 | 05:00 |
| "3h chiều" | 15:00 | 08:00 |
| "9h tối" | 21:00 | 14:00 |

## Phương pháp 1: Cron Job (Main Session)

Ghi cron job vào `/root/openclaw/.openclaw/cron/jobs.json`:

```json
{
  "version": 1,
  "jobs": [
    {
      "id": "rem-001",
      "schedule": "30 3 12 3 *",
      "prompt": "Đây là nhắc nhở tự động. Hãy gửi tin nhắn cho Sếp: '⏰ Nhắc nhở: Đến giờ uống nước rồi! 💧'. Sau đó cập nhật file reminders/active.json đánh dấu rem-001 là done.",
      "channel": "telegram",
      "target": "telegram:882968821",
      "enabled": true
    }
  ]
}
```

> **Quan trọng**: 
> - `target` PHẢI là `telegram:882968821` (Telegram ID của Sếp)
> - `schedule` dùng giờ **UTC**, format: `phút giờ ngày tháng *`
> - Đọc file `jobs.json` hiện tại TRƯỚC, thêm job mới vào mảng `jobs`, KHÔNG ghi đè

### Cách đọc-thêm-ghi đúng:
```bash
# Đọc jobs hiện tại
cat /root/openclaw/.openclaw/cron/jobs.json

# Thêm job mới bằng python3
python3 -c "
import json
with open('/root/openclaw/.openclaw/cron/jobs.json', 'r') as f:
    data = json.load(f)
data['jobs'].append({
    'id': 'rem-XXX',
    'schedule': 'MIN HOUR DAY MONTH *',
    'prompt': 'Gửi tin nhắn nhắc nhở cho Sếp: ⏰ [NỘI DUNG]',
    'channel': 'telegram',
    'target': 'telegram:882968821',
    'enabled': True
})
with open('/root/openclaw/.openclaw/cron/jobs.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('✅ Đã tạo cron job')
"
```

## Phương pháp 2: File + Heartbeat (Fallback)

Nếu cron job không khả dụng, ghi reminder vào file:

File: `/root/openclaw/workspace/reminders/active.json`
```json
{
  "reminders": [
    {
      "id": "rem-001",
      "content": "Uống nước 💧",
      "datetime_utc": "2026-03-12T03:30:00Z",
      "datetime_vn": "2026-03-12T10:30:00+07:00",
      "status": "active"
    }
  ]
}
```

HEARTBEAT sẽ check file này mỗi 30 phút và nhắc nếu đến giờ.

## Cách sử dụng

### Tạo nhắc nhở
User nhắn bằng tiếng Việt tự nhiên:
- "Nhắc tôi họp team lúc 3h chiều mai"
- "30 phút nữa nhắc tôi uống nước"
- "Deadline nộp proposal ngày 15/3"

### Xem/xóa
- "Xem lịch nhắc" → đọc `reminders/active.json`
- "Bỏ nhắc X" → xóa entry + xóa cron job tương ứng

## Xác nhận khi tạo
```
✅ Đã ghi nhớ!
📌 [Nội dung]
⏰ [Giờ VN] (= [Giờ UTC] UTC, sau [X] phút nữa)
📡 Gửi qua: Telegram → Sếp
🔄 [Một lần / Lặp lại]
```

## Dọn dẹp
Sau khi nhắc xong reminder one-time:
1. Cập nhật `active.json` → status: "done"
2. Xóa cron job đã hoàn thành khỏi `jobs.json`
