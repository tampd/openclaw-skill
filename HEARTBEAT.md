# HEARTBEAT.md

# Checklist mỗi heartbeat cycle (~30 phút):

## 1. Nhắc nhở
- Kiểm tra file `reminders/active.json`: có nhắc nhở nào sắp đến (trong 2h tới)?
- Nếu có → gửi cảnh báo sớm cho user

## 2. Sức khỏe VPS (2-3 lần/ngày)
- Chạy `free -m` và `df -h /`
- Nếu RAM > 80% hoặc Disk > 80% → cảnh báo user

## 3. Báo cáo cuối ngày (1 lần, ~22:00)
- Nếu giờ hiện tại gần 22:00 và chưa có file `reports/[today].md` → chạy skill `daily-reporter`

## 4. Memory maintenance (1 lần/tuần)
- Đọc lại memory files gần đây
- Cập nhật MEMORY.md nếu có insight đáng giữ
