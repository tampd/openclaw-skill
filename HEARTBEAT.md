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

## 4. Fanpage Tý Tech (nhiều lần/ngày)
- Kiểm tra comment/inbox mới của fanpage Tý Tech
- Nếu có comment hợp lệ → ưu tiên trả lời sớm, ngắn gọn, đúng tone page
- Nếu có comment hay → ghi nhận để tái sử dụng làm ý tưởng content
- Nếu phát hiện spam/độc hại → báo user khi cần, tránh tranh cãi

## 5. Memory maintenance (1 lần/tuần)
- Đọc lại memory files gần đây
- Cập nhật MEMORY.md nếu có insight đáng giữ
