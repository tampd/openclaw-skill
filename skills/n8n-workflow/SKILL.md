---
name: n8n-workflow
description: Quản lý n8n workflows tại n8n.chaiko.info — tạo, chạy, debug, optimize workflows qua API.
---

# n8n Workflow Manager

## Mục đích
Kết nối Tôm với n8n server (n8n.chaiko.info) để quản lý workflows tự động hóa.

## Khi nào kích hoạt
- User nói: "n8n", "workflow", "automation", "tự động hóa"
- User muốn trigger workflow, kiểm tra trạng thái, hoặc tạo workflow mới

## Setup
```bash
# Cần N8N_API_KEY và N8N_BASE_URL trong .env
# N8N_BASE_URL=https://n8n.chaiko.info
# N8N_API_KEY=<lấy từ n8n UI → Settings → API>
```

## Lệnh

### Quản lý Workflow
```bash
# List tất cả workflows
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_BASE_URL/api/v1/workflows" | python3 -m json.tool

# Xem chi tiết workflow
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_BASE_URL/api/v1/workflows/<id>" | python3 -m json.tool

# Activate/Deactivate workflow
curl -s -X PATCH -H "X-N8N-API-KEY: $N8N_API_KEY" -H "Content-Type: application/json" \
  -d '{"active": true}' "$N8N_BASE_URL/api/v1/workflows/<id>"

# Xem execution history
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_BASE_URL/api/v1/executions?workflowId=<id>&limit=10" | python3 -m json.tool
```

### Trigger Workflow
```bash
# Trigger webhook workflow
curl -s -X POST "$N8N_BASE_URL/webhook/<webhook-path>" \
  -H "Content-Type: application/json" \
  -d '{"message": "Triggered by Tôm"}'
```

### Debug & Monitor
```bash
# Xem executions lỗi gần nhất
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" \
  "$N8N_BASE_URL/api/v1/executions?status=error&limit=5" | python3 -m json.tool
```

## Quy tắc
- ✅ Luôn confirm trước khi activate/deactivate workflow
- ✅ Kiểm tra status trước khi trigger
- ❌ KHÔNG xóa workflow mà chỉ deactivate
- ❌ KHÔNG tạo workflow có infinite loop
