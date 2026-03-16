# Tý Tech recovery — 2026-03-16

## Trạng thái hiện tại
- Content calendar vẫn còn: `memory/content-calendar.md`
- Blog autopilot vẫn còn job trong `~/.openclaw/cron/jobs.json`
- Facebook posting hiện bị chặn bởi token/app permission error:
  - `Cannot call API for app 1005409485170910 on behalf of user 122098477221071447`
- Script refresh token cũng fail với cùng lỗi trên

## Việc cần làm để khôi phục Tý Tech posting
1. Tạo lại Facebook user token hợp lệ cho app hiện tại
2. Lấy page token mới
3. Verify đọc/ghi được `/feed`
4. Sau đó thêm lại 3 job tự động cho Tý Tech:
   - sáng 07:45 GMT+7
   - trưa 12:15 GMT+7
   - tối 19:30 GMT+7

## Draft bài bù tối 16/03
Hook: Có nên luôn online sau giờ làm?
Angle: work-life dân IT, thực tế, không giáo điều.
CTA: Bạn có tắt notification sau giờ làm không?
