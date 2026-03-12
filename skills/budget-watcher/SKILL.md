---
name: budget-watcher
description: Theo dõi token usage và chi phí Vertex AI. Cảnh báo khi gần vượt ngưỡng ngân sách $300 free credits.
---

# Budget Watcher — Giám Sát Chi Phí AI

## Mục đích
Theo dõi lượng token tiêu thụ trên Google Vertex AI, ước tính chi phí, và cảnh báo khi gần vượt ngưỡng ngân sách $300 free credits.

## Thông tin cơ bản
- **GCP Project**: `duytam-n8n`
- **Tổng credits**: $300
- **Model chính**: `gemini-2.5-flash` (Input: $0.30/1M tokens, Output: $2.50/1M tokens)
- **Model phụ**: `gemini-2.5-pro` (Input: $1.25/1M tokens, Output: $10.00/1M tokens)

## Khi nào kích hoạt
- User hỏi: "Chi phí bao nhiêu?", "Còn bao nhiêu credits?", "Token usage?"
- Lệnh `/budget` từ Admin
- Tự động kiểm tra 1 lần/ngày qua heartbeat (sáng sớm)

## Quy trình

### Bước 1: Thu thập dữ liệu

```bash
# Kiểm tra log size (ước tính hoạt động)
du -sh /root/openclaw/.openclaw/logs/
ls -lt /root/openclaw/.openclaw/logs/ | head -10

# Đếm số session/conversation gần đây
find /root/openclaw/.openclaw/logs/ -name "*.log" -mtime -1 | wc -l
find /root/openclaw/.openclaw/logs/ -name "*.log" -mtime -7 | wc -l

# Kiểm tra GCP billing (nếu gcloud CLI có sẵn)
gcloud billing accounts list 2>/dev/null || echo "gcloud CLI không khả dụng"
```

### Bước 2: Ước tính chi phí

Vì không có API trực tiếp đếm tokens, ước tính dựa trên:
- **Số lượng conversations/ngày** × **avg tokens/conversation**
- Ước tính trung bình: 1 conversation ≈ 5,000-15,000 tokens (input+output)

**Bảng ước tính** (model Flash):
| Conversations/ngày | Est. Tokens/ngày | Est. Cost/ngày | Số ngày còn lại (từ $300) |
|---------------------|-----------------|----------------|---------------------------|
| 5 | ~50K | ~$0.15 | ~2000 ngày |
| 20 | ~200K | ~$0.55 | ~545 ngày |
| 50 | ~500K | ~$1.40 | ~214 ngày |
| 100 | ~1M | ~$2.80 | ~107 ngày |

### Bước 3: Trả lời

```
💰 **Báo Cáo Ngân Sách AI**

📊 **Hoạt động hôm nay:**
- Conversations: [N]
- Est. tokens: ~[N]K

💵 **Ước tính chi phí:**
- Hôm nay: ~$[X]
- 7 ngày qua: ~$[X]
- Tổng ước tính: ~$[X] / $300

📈 **Dự báo:**
- Tốc độ tiêu: ~$[X]/ngày
- Credits còn lại: ~$[X]
- Dùng được thêm: ~[N] ngày

[🟢 An toàn / 🟡 Cần tiết kiệm / 🔴 Sắp hết]
```

### Bước 4: Cảnh báo tự động

| Mức | Ngưỡng | Hành động |
|-----|--------|-----------|
| 🟢 | < $100 đã dùng | Không cần cảnh báo |
| 🟡 | $100-200 đã dùng | Cảnh báo 1 lần/tuần |
| 🔴 | > $200 đã dùng | Cảnh báo hàng ngày + đề xuất giảm heartbeat |
| ⚫ | > $250 đã dùng | Cảnh báo khẩn + đề xuất chuyển Flash-Lite |

## Ghi log chi phí
Lưu tracking vào file: `/root/openclaw/workspace/reports/budget-log.json`

```json
{
  "entries": [
    {
      "date": "2026-03-12",
      "conversations": 15,
      "est_tokens": 150000,
      "est_cost_usd": 0.42,
      "model": "gemini-2.5-flash",
      "cumulative_est_usd": 0.42
    }
  ]
}
```

Mỗi ngày append 1 entry mới. Đây là nguồn dữ liệu cho daily-reporter.

## Đề xuất tiết kiệm
Khi ở mức 🟡 hoặc 🔴, đề xuất:
1. Tăng heartbeat interval (30 phút → 1 giờ → 2 giờ)
2. Giảm context window (compaction aggressive hơn)
3. Chuyển tasks đơn giản sang Flash-Lite
4. Hạn chế research dài (giới hạn curl output)
