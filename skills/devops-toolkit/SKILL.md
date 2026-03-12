---
name: devops-toolkit
description: DevOps toolkit — Docker, process management, log analysis, health monitoring, port scanning. Kết hợp với vps-monitor.
---

# DevOps Toolkit

> Mở rộng cho `vps-monitor` — thêm Docker, log analysis, port scanning nâng cao.

## Khi nào kích hoạt
- User nói: "docker", "container", "logs", "process", "port", "health check"
- User nói: "diagnostics", "debug server", "check service"
- Dùng bổ sung cho `vps-monitor` khi cần chi tiết hơn

## Docker Operations
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

# Restart container
docker restart <container>
```

## Process Management
```bash
# Top processes by CPU
ps aux --sort=-%cpu | head -15

# Top processes by memory
ps aux --sort=-%mem | head -15

# Ports đang listen
ss -tlnp | grep LISTEN

# Zombie processes
ps aux | awk '$8 ~ /Z/ {print}'

# Kill process by PID (CẦN CONFIRM)
# kill -15 <pid>
```

## Log Analysis
```bash
# Error pattern trong log
grep -iE "error|fail|critical|exception" /var/log/syslog | tail -20

# Log frequency analysis (top errors)
grep -iE "error|fail" /var/log/syslog | awk '{print $5}' | sort | uniq -c | sort -rn | head -10

# Journalctl cho service
journalctl -u <service> --since "1 hour ago" --no-pager | tail -30

# OpenClaw logs
find /root/openclaw/.openclaw/logs/ -name "*.log" -mtime 0 -exec tail -20 {} \; 2>/dev/null | grep -i "error\|fail"
```

## Health Checks
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

# Full system health
echo "=== CPU ===" && uptime
echo "=== RAM ===" && free -m | head -3
echo "=== DISK ===" && df -h / | tail -1
echo "=== DOCKER ===" && docker ps --format "{{.Names}}: {{.Status}}" 2>/dev/null || echo "Docker not running"
echo "=== LOAD ===" && cat /proc/loadavg
```

## Quy tắc
- ✅ Có thể chạy diagnostics bất kỳ lúc nào
- ✅ Kết hợp output vào daily-reporter
- ⚠️ Confirm trước khi restart/kill service
- ❌ KHÔNG xóa logs hoặc docker volumes
