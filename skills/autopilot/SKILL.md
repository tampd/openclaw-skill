---
name: autopilot
description: Chế độ tự lái — Tôm tự chạy tasks theo heartbeat, báo cáo tiến độ, tự quyết định trong phạm vi được phép.
---

# Autopilot — Chế Độ Tự Lái

> Kết hợp với `daily-reporter` — bật mode tự lái cho tasks dài hạn.

## Khi nào kích hoạt
- User nói: "autopilot", "tự chạy", "tự làm đi", "chạy nền"
- User giao task lớn cần xử lý qua nhiều bước
- Trong HEARTBEAT.md khi có pending tasks

## Cách hoạt động

### Bật Autopilot
User gõ: "Tôm, autopilot: [mô tả task]"

### Quy trình
1. **Phân tích task** → chia thành sub-tasks
2. **Ghi task list** vào `memory/todo.md` và `memory/autopilot-state.json`
3. **Chạy từng bước** theo heartbeat interval
4. **Báo cáo** trạng thái sau mỗi milestone
5. **Dừng** khi hoàn thành hoặc gặp blocker → hỏi Sếp

### State File: `memory/autopilot-state.json`
```json
{
  "active": true,
  "task": "Mô tả task chính",
  "started": "2026-03-12T14:00:00+07:00",
  "steps": [
    {"id": 1, "desc": "Bước 1", "status": "done"},
    {"id": 2, "desc": "Bước 2", "status": "in-progress"},
    {"id": 3, "desc": "Bước 3", "status": "pending"}
  ],
  "lastReport": "2026-03-12T16:00:00+07:00"
}
```

## Quyền tự quyết

### ✅ Được tự quyết
- Đọc/ghi file trong workspace
- Chạy lệnh chẩn đoán (diagnostics, monitoring)
- Tạo reports, summaries
- Cập nhật memory files
- Research thông tin (web search)

### ⚠️ Phải báo trước
- Gửi tin nhắn/email cho người khác
- Tạo/sửa cron jobs
- Thay đổi config hệ thống

### 🔴 PHẢI hỏi Sếp
- Xóa files/data
- Cài phần mềm mới
- Restart services
- Đăng bài public (blog, social media)
- Bất kỳ action nào ảnh hưởng production

## Báo cáo tiến độ

### Trong giờ làm (8h-22h VN)
- Báo cáo mỗi 2 giờ hoặc khi hoàn thành milestone
- Format: "🤖 Autopilot: Đã [action]. Tiếp theo: [next step]. Cần gì không Sếp?"

### Ngoài giờ (22h-8h VN)
- Chỉ báo cáo khi hoàn thành task hoặc gặp lỗi nghiêm trọng
- Tóm tắt vào morning-briefing

## Dừng Autopilot
- User nói: "dừng", "stop", "cancel autopilot"
- Gặp lỗi > 3 lần liên tiếp
- Task hoàn thành

## Kết hợp
- `daily-reporter`: Autopilot status được ghi vào daily report
- `smart-reminder`: Nhắc Sếp review autopilot results
- `office-assistant`: Autopilot có thể soạn draft email/báo giá
