---
name: devops-toolkit
description: "DevOps & VPS monitoring: Docker, process management, log analysis, health monitoring, port scanning, VPS resource checks. Chạy trực tiếp trên localhost."
---

# DevOps & VPS Toolkit

> ⚠️ Bạn đang chạy **TRÊN MÁY CHỦ NÀY**. Mọi lệnh đều chạy trên **localhost**.
> KHÔNG BAO GIỜ hỏi user "IP là gì?" — chỉ cần chạy lệnh ngay.

## Khi nào kích hoạt
- User nói: "VPS", "server", "RAM", "CPU", "disk", "dung lượng"
- User nói: "docker", "container", "logs", "process", "port", "health check"
- User nói: "diagnostics", "debug server", "check service", "kiểm tra VPS"
- Heartbeat check (2-3 lần/ngày)
- Lệnh `/health` từ Admin

---

## 1. VPS Quick Check (nhanh)

### Thu thập & đánh giá
```bash
# Memory + CPU + Disk — one shot
echo "=== RAM ===" && free -m | head -3
echo "=== CPU ===" && uptime
echo "=== DISK ===" && df -h / | tail -1
echo "=== LOAD ===" && cat /proc/loadavg
```

### Ngưỡng cảnh báo

| Metric | 🟢 Tốt | 🟡 Cảnh báo | 🔴 Nguy hiểm |
|--------|---------|-------------|---------------|
| CPU Load | < 1.0 | 1.0 - 2.0 | > 2.0 |
| RAM Usage | < 70% | 70% - 85% | > 85% |
| Disk Usage | < 70% | 70% - 85% | > 85% |

### Format trả lời
```
🖥️ **Báo cáo VPS**
* **CPU Load**: [load avg] [emoji]
* **RAM**: [Used]/[Total] MB ([%]) [emoji]
* **Ổ cứng**: [Used]/[Total] ([%]) [emoji]
* **Uptime**: [X days, Y hours]
* **Docker**: [N] containers running
[Trạng thái tổng: 🟢/🟡/🔴]
```

### Cảnh báo tự động
Nếu bất kỳ metric nào 🔴 → gửi cảnh báo Sếp ngay + liệt kê top 3 process ngốn tài nguyên.

---

## 2. Docker Operations
```bash
# Tổng quan containers
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}"

# Logs container có filter
docker logs <container> --tail 100 2>&1 | grep -iE "error|warn|fail"

# Docker resource usage
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"

# Container health
docker inspect --format='{{.State.Health.Status}}' <container> 2>/dev/null || echo "No healthcheck"

# Docker compose status
docker compose -f /path/to/docker-compose.yml ps

# Restart container (CẦN CONFIRM)
docker restart <container>
```

## 3. Process Management
```bash
# Top processes by CPU
ps aux --sort=-%cpu | head -15

# Top processes by memory
ps aux --sort=-%mem | head -15

# Ports đang listen
ss -tlnp | grep LISTEN

# Zombie processes
ps aux | awk '$8 ~ /Z/ {print}'
```

## 4. Log Analysis
```bash
# Error pattern trong log
grep -iE "error|fail|critical|exception" /var/log/syslog | tail -20

# Log frequency analysis
grep -iE "error|fail" /var/log/syslog | awk '{print $5}' | sort | uniq -c | sort -rn | head -10

# Journalctl cho service
journalctl -u <service> --since "1 hour ago" --no-pager | tail -30

# OpenClaw logs
find /root/openclaw/.openclaw/logs/ -name "*.log" -mtime 0 -exec tail -20 {} \; 2>/dev/null | grep -i "error\|fail"
```

## 5. Health Checks
```bash
# HTTP endpoint check
curl -sL -o /dev/null -w "HTTP %{http_code} — %{time_total}s" https://blog.chaiko.info

# Multi-endpoint check
for url in "https://blog.chaiko.info" "https://n8n.chaiko.info"; do
  code=$(curl -sL -o /dev/null -w "%{http_code}" "$url")
  echo "$url → HTTP $code"
done

# Port scan local
for port in 80 443 8080 18789 5678; do
  (echo >/dev/tcp/localhost/$port) 2>/dev/null && echo "Port $port: OPEN" || echo "Port $port: CLOSED"
done
```

## Quy tắc
- ✅ Có thể chạy diagnostics bất kỳ lúc nào — KHÔNG cần hỏi
- ✅ Kết hợp output vào daily-reporter
- ✅ Parse output thành format đẹp, KHÔNG gửi raw terminal
- ⚠️ Confirm trước khi restart/kill service
- ❌ KHÔNG xóa logs hoặc docker volumes
