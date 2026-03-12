---
name: vps-monitor
description: Kiểm tra sức khỏe và tài nguyên (CPU, RAM, Disk) của VPS hiện tại. Chạy trực tiếp trên localhost.
---

# VPS System Monitoring

## QUAN TRỌNG
> ⚠️ Bạn đang chạy TRÊN MÁY CHỦ NÀY. Mọi lệnh đều chạy trên **localhost**.
> KHÔNG BAO GIỜ hỏi user "IP là gì?" hay "hostname là gì?" — chỉ cần chạy lệnh ngay.

## Khi nào kích hoạt
- User hỏi: "Dung lượng VPS", "RAM bao nhiêu?", "Server có ổn không?", "Kiểm tra VPS"
- Heartbeat check (2-3 lần/ngày)
- Lệnh `/health` từ Admin

## Quy trình

### Bước 1: Thu thập (chạy ngay, KHÔNG hỏi)
```bash
# Memory
free -m

# Disk
df -h /

# CPU + Uptime
uptime

# Top processes (nếu cần)
ps aux --sort=-%mem | head -6
```

### Bước 2: Parse & đánh giá

| Metric | 🟢 Tốt | 🟡 Cảnh báo | 🔴 Nguy hiểm |
|--------|---------|-------------|---------------|
| CPU Load | < 1.0 | 1.0 - 2.0 | > 2.0 |
| RAM Usage | < 70% | 70% - 85% | > 85% |
| Disk Usage | < 70% | 70% - 85% | > 85% |

### Bước 3: Trả lời (format đẹp)
```
🖥️ **Báo cáo Trạng thái VPS**

* **CPU Load**: [load avg 1m/5m/15m] [emoji]
* **RAM**: [Used] / [Total] MB ([%]) [emoji]
* **Ổ cứng**: [Used] / [Total] ([%]) [emoji]
* **Uptime**: [X days, Y hours]

[Trạng thái tổng: 🟢 Hệ thống khỏe mạnh / 🟡 Cần chú ý / 🔴 Cần xử lý ngay]
```

### Bước 4: Cảnh báo tự động
Nếu bất kỳ metric nào ở mức 🔴:
- Gửi cảnh báo ngay cho Sếp: "⚠️ VPS Alert: [metric] đang cao bất thường!"
- Liệt kê top 3 process ngốn RAM/CPU nhất

## Lưu ý
- Do NOT show raw terminal output — luôn parse thành format đẹp
- Do NOT ask for IP, hostname, hoặc SSH credentials — bạn ĐÃ Ở TRÊN máy này
