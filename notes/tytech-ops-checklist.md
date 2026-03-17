# Tý Tech Ops Checklist

## Mục tiêu
Đảm bảo job đăng bài và heartbeat fanpage chạy đúng, có tự kiểm tra, và khi phát hiện lỗi thì báo anh Tâm ngay để xin ý kiến sửa.

## 1. Trước khi đăng bài
- Nhắn ngắn cho anh Tâm: đang xử lý slot nào.
- Đọc `memory/content-calendar.md`
- Đọc `knowledge/facebook-tytech.md`
- Kiểm tra token/page còn đọc được:
  - `/{page_id}?fields=id,name`

## 2. Khi đăng bài
- Ưu tiên bài có ảnh hoặc link preview hợp lệ
- Không ghi log thành công trước khi verify live

## 3. Sau khi đăng bài (bắt buộc)
- Đọc lại feed:
  - `/feed?fields=id,message,created_time,permalink_url&limit=5`
- Xác nhận post mới xuất hiện thật
- Nếu là bài share, kiểm tra thêm preview/media hợp lệ
- Chạy anonymous visibility check: mở `permalink_url` bằng request không đăng nhập
- Chỉ ghi thành công nếu không bị redirect sang `/login` và không ra trang lỗi / không xem được nội dung
- Ghi `Post ID`, trạng thái, link vào `memory/content-calendar.md`
- Báo cáo thực tế cho anh Tâm

## 4. Kiểm tra heartbeat fanpage
- Feed query đúng:
  - `/feed?fields=message,created_time,comments{from,message,created_time,id}.limit(5)&limit=5`
- Inbox query đúng:
  - `/conversations?fields=updated_time,participants,messages{message,from,created_time}.limit(5)&limit=5`

## 5. Khi phát hiện lỗi phải báo ngay
Các lỗi phải báo ngay để xin ý kiến sửa:
- Graph API syntax error
- Token refresh fail
- Permission error / object missing
- Scheduler job không xuất hiện trong `jobs.json`
- Gateway sống nhưng job bị kẹt `runningAtMs`
- Đăng xong nhưng feed không thấy bài

## 6. Cơ chế tự học
Khi gặp lỗi mới:
1. Ghi lỗi thực tế + command + response vào note hoặc memory
2. Sửa quy trình/HEARTBEAT/skill nếu xác định được nguyên nhân
3. Báo anh Tâm ngắn gọn: lỗi gì, ảnh hưởng gì, đề xuất sửa gì
4. Chỉ ghi là "đã xong" sau khi verify lại thành công

## 7. Bài học cố định về cron đăng bài
- Không cấu hình cron đăng bài quan trọng bằng kiểu cũ `prompt + target + sessionTarget: main`.
- Nếu job cần tự chạy đúng giờ và gửi báo cáo về Telegram, dùng schema chuẩn:
  - `sessionTarget: "isolated"`
  - `payload.kind: "agentTurn"`
  - `delivery.mode: "announce"`
- Mặc định áp dụng mô hình **2 lớp** cho bài đăng quan trọng:
  1. **job chính** đăng bài + tự retry/sửa lỗi tối đa 3 vòng trong cùng lượt
  2. **watchdog hậu kiểm** sau 10-20 phút để verify feed; nếu thiếu bài thì tự đăng bù và báo cáo
- Sau khi sửa cron phải kiểm tra lại bằng cách đọc `~/.openclaw/cron/jobs.json` và xác nhận:
  - `sessionTarget = isolated`
  - có `payload`
  - có `delivery`
  - các watchdog đã tồn tại
  - không còn `runningAtMs` treo cũ nếu vừa recover job.
