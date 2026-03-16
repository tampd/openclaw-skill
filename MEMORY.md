# 🧠 MEMORY.md — Tôm's Long-Term Memory

> Cập nhật lần cuối: 2026-03-16
> File này là bộ nhớ dài hạn. Chỉ load trong main session.

## Sếp & Môi trường
- Sếp: Phạm Duy Tâm, timezone GMT+7, thích kết quả nhanh
- Công cụ: Antigravity (chỉ huy) + OpenClaw/Tôm (thực thi) + n8n (automation)
- VPS: Ubuntu, localhost, root access
- Blog: blog.chaiko.info (WordPress, REST API)
- Fanpage: Tý Tech (Page ID: 1012410591957125)

## Nhân viên
- @TrangMin (ID: 1077372918) — nhân viên sales, quyền giới hạn, thư mục riêng staff/TrangMin/

## Bài học quan trọng
- Facebook App bị sanction → cần tạo app mới, App ID mới: 1337446871770985 (2026-03-16)
- Token Page Access: never-expires nếu lấy từ Long-Lived User Token qua /me/accounts
- Luôn verify kết quả thực tế trước khi báo cáo (Luật cứng #3)
- Sếp ghét câu sáo rỗng — nói thẳng, ngắn gọn, có bằng chứng
- wp_credentials.txt → đã move sang .openclaw/credentials/ (2026-03-16)

## Dự án đang theo dõi
- Content 5 bài/ngày cho Tý Tech (content-calendar + viral-content-hunter)
- Blog SEO automation (seo-writer + wp-publisher)
- Tư vấn BKNS + VCharge cho khách hàng

## Quy trình đã thiết lập
- FB token healthcheck: cron hàng ngày 7h VN
- FB token refresh: cron mỗi 50 ngày
- Daily report: heartbeat ~22h VN
- Heartbeat: ~30 phút/lần, check reminders, VPS health, fanpage comments
