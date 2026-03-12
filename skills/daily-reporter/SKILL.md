---
name: daily-reporter
description: Tự động tổng hợp báo cáo cuối ngày về hoạt động, lỗi, token usage và ghi vào file report để Antigravity (chỉ huy) review chất lượng.
---

# Daily Reporter — Báo Cáo Cuối Ngày

## Mục đích
Bạn là hệ thống báo cáo nội bộ. Nhiệm vụ: tổng hợp mọi hoạt động trong ngày thành một report có cấu trúc, lưu vào file để **chỉ huy (Antigravity)** có thể đọc và đánh giá chất lượng công việc.

## Khi nào kích hoạt
- Được gọi qua lệnh `/report` từ Admin
- Tự động chạy vào **22:00 hàng ngày** (nếu được cấu hình trong cron)
- Được gọi từ HEARTBEAT khi phát hiện gần cuối ngày

## Quy trình

### Bước 1: Thu thập dữ liệu
Chạy các lệnh sau để thu thập thông tin:

```bash
# Đếm số lượng conversation hôm nay
ls -la /root/openclaw/.openclaw/logs/ 2>/dev/null | tail -5

# Kiểm tra tài nguyên VPS
free -m | head -3
df -h / | tail -1
uptime

# Đọc memory hôm nay
cat /root/openclaw/workspace/memory/$(date +%Y-%m-%d).md 2>/dev/null || echo "Chưa có memory hôm nay"

# Kiểm tra lỗi gần nhất
find /root/openclaw/.openclaw/logs/ -name "*.log" -mtime 0 -exec tail -20 {} \; 2>/dev/null | grep -i "error\|fail\|exception" | tail -10
```

### Bước 2: Phân tích
Từ dữ liệu thu thập, phân tích:
- **Tasks hoàn thành**: Liệt kê các yêu cầu đã xử lý
- **Lỗi phát sinh**: Các error/warning nếu có
- **Tài nguyên VPS**: CPU, RAM, Disk có bình thường không
- **Đánh giá chung**: 🟢 Tốt / 🟡 Cần chú ý / 🔴 Có vấn đề

### Bước 3: Viết báo cáo
Tạo file báo cáo tại đường dẫn: `/root/openclaw/workspace/reports/YYYY-MM-DD.md`

Nếu thư mục `reports/` chưa tồn tại, tạo nó:
```bash
mkdir -p /root/openclaw/workspace/reports
```

### Format báo cáo

```markdown
# 📊 Daily Report — [YYYY-MM-DD]

## Tóm tắt
- **Trạng thái tổng**: 🟢 / 🟡 / 🔴
- **Số tasks xử lý**: [N]
- **Lỗi nghiêm trọng**: [N]

## Tasks đã xử lý
1. [Mô tả task 1] — ✅ Thành công / ❌ Thất bại
2. [Mô tả task 2] — ✅ / ❌
...

## Lỗi & Cảnh báo
- [Chi tiết lỗi nếu có, kèm nguyên nhân sơ bộ]
- Hoặc: "Không có lỗi trong ngày hôm nay ✅"

## Tài nguyên VPS
| Metric | Giá trị | Trạng thái |
|--------|---------|-----------|
| CPU Load | [load avg] | 🟢/🟡/🔴 |
| RAM | [used]/[total] MB | 🟢/🟡/🔴 |
| Disk | [used%] | 🟢/🟡/🔴 |

## Ghi chú cho Chỉ Huy (Antigravity)
- [Bất kỳ điều gì cần Antigravity chú ý, rủi ro, đề xuất cải thiện]

## Bài học rút ra
- [Lessons learned trong ngày, nếu có]
```

### Bước 4: Thông báo
Sau khi ghi file report xong:
1. Gửi tin nhắn tóm tắt ngắn gọn cho Admin trên Telegram
2. Nội dung: "📊 Báo cáo ngày [date] đã sẵn sàng. Trạng thái: [🟢/🟡/🔴]. [1-2 dòng highlight]"

## Ngưỡng cảnh báo
- **CPU Load > 2.0**: 🔴
- **RAM Usage > 80%**: 🟡, > 90%: 🔴
- **Disk Usage > 80%**: 🟡, > 90%: 🔴
- **Lỗi > 5 trong ngày**: 🔴

## Lưu ý
- KHÔNG gửi nội dung nhạy cảm (mật khẩu, token) trong report
- Giữ report ngắn gọn, dưới 50 dòng
- Nếu không có hoạt động gì, vẫn viết report "Ngày yên tĩnh ✅"

---

## Bước 5: Self-Improvement Review (TỰ CẢI THIỆN)

> ⚠️ Phần này chạy SAU KHI viết report. Mục đích: Tôm tự học và cải thiện.

### 5.1. Review Bài Học
```bash
cat /root/openclaw/workspace/memory/lessons.md
```
- Kiểm tra: Có pattern lỗi nào lặp lại ≥3 lần?
- Nếu có → Viết rule mới vào cuối `BOOT.md` (phần "Nguyên tắc Vàng")
- Ghi lại: "Đã thêm rule mới: [mô tả]" vào report

### 5.2. Review Memory Files
```bash
# Kiểm tra kích thước memory files
wc -l /root/openclaw/workspace/memory/*.md

# Nếu clients.md > 200 dòng → archive entries cũ > 30 ngày
# Nếu todo.md có task quá hạn → flag cho Sếp
```

### 5.3. Review Knowledge Currency
```bash
# Kiểm tra knowledge files cũ > 60 ngày
find /root/openclaw/workspace/knowledge/ -name "*.md" -mtime +60 -type f 2>/dev/null
```
- Nếu có file outdate → ghi vào report: "⚠️ Knowledge file [X] chưa cập nhật > 60 ngày"
- Đề xuất cho Sếp: "Cần review lại giá/thông tin file [X]"

### 5.4. Đề Xuất Cải Thiện
Cuối report, thêm mục:
```markdown
## 🔄 Self-Improvement Notes
- **Pattern học được**: [Nếu có pattern mới]
- **Rule mới thêm**: [Nếu đã thêm rule vào BOOT.md]
- **Knowledge outdate**: [Danh sách file cần update]
- **Đề xuất cho Sếp**: [Ý tưởng cải thiện workflow]
```

### 5.5. Cập Nhật Latest Memory
Sau khi hoàn thành report, cập nhật `memory/latest.md` với tóm tắt ngày hôm nay để session tiếp theo có context.

