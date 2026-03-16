---
name: capability-evolver
description: Self-evolution engine — phân tích runtime, đề xuất cải thiện, CHỈ áp dụng sau khi được owner duyệt (Review Mode)
---

# Capability Evolver — Review Mode

> ⚠️ **CHỈ REVIEW MODE** — Mọi thay đổi phải được owner (@phamduytam) duyệt trước khi áp dụng.
> TUYỆT ĐỐI KHÔNG tự động sửa code, xóa file, hoặc thay đổi config mà không có sự đồng ý.

## Mục đích
Tự phân tích hiệu suất, phát hiện lỗi/bottleneck, và **đề xuất** (không tự thực thi) các cải thiện.

## Quy trình

### 1. Thu thập dữ liệu
- Đọc LESSONS.md, INSTINCTS.md, INSIGHTS.md
- Phân tích session logs gần nhất
- Kiểm tra error patterns, response time, task completion rate

### 2. Phân tích
- Xác định top 3-5 vấn đề cần cải thiện
- Đánh giá severity (critical/medium/low)
- Tìm root cause cho mỗi vấn đề

### 3. Đề xuất (KHÔNG tự thực thi)
Với mỗi vấn đề, trình bày:
```
## Đề xuất #N: [Tên]
- **Vấn đề**: Mô tả ngắn gọn
- **Root cause**: Nguyên nhân gốc
- **Giải pháp đề xuất**: Chi tiết cách fix
- **Rủi ro**: Potential side effects
- **Ước tính effort**: Thời gian cần thiết
- **Cần duyệt**: ✅ Chờ owner approve
```

### 4. Áp dụng (CHỈ sau khi được duyệt)
- Owner review từng đề xuất
- Owner approve/reject từng item
- Chỉ thực thi những item được approve
- Log kết quả vào LESSONS.md/INSTINCTS.md

## Lệnh kích hoạt
- `/evolve` hoặc `/tự-đánh-giá` — Chạy full cycle phân tích + đề xuất
- `/evolve status` — Xem trạng thái cải thiện gần nhất
- `/evolve apply #N` — Áp dụng đề xuất #N (sau khi đã duyệt)

## Giới hạn an toàn
1. **KHÔNG** xóa file nào
2. **KHÔNG** sửa openclaw.json
3. **KHÔNG** chạy lệnh hệ thống (rm, dd, shutdown...)
4. **KHÔNG** thay đổi quyền file
5. CHỈ được ghi vào: LESSONS.md, INSTINCTS.md, INSIGHTS.md, ACTIVE_CONTEXT.md
6. CHỈ được tạo file mới trong workspace/skills/ (skill mới)
7. Mọi thay đổi khác → phải hỏi owner trước

## Tích hợp APEX
- Đề xuất thành công → ghi vào INSTINCTS.md (+0.1 confidence)
- Đề xuất bị reject → ghi lesson learned
- Sau 5 cycles → tạo INSIGHTS.md compound insight
