---
name: wp-publisher
description: "WordPress manager: đăng bài, audit blog, kiểm tra trùng lặp, SEO check cho blog.chaiko.info qua REST API."
---

# WordPress Manager — Publish & Audit

## Mục đích
Quản lý blog.chaiko.info: đăng bài, kiểm tra trùng lặp, audit SEO, dọn draft cũ.

## ⚠️ QUAN TRỌNG
- API endpoint: `https://blog.chaiko.info/wp-json/wp/v2/posts`
- Credentials: đọc từ `/root/openclaw/workspace/wp_credentials.txt`
- **KHÔNG hiển thị password** trong chat

---

## 1. Đăng Bài (Publish)

### Bước 0: Kiểm tra trùng lặp (BẮT BUỘC)
```bash
TITLE="Tiêu đề bài viết"
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?search=$(echo "$TITLE" | head -c 50 | sed 's/ /+/g')&_fields=id,title,status" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
dupes = [p for p in posts if p['title']['rendered'].strip().lower() == sys.argv[1].strip().lower()]
if dupes:
    print('⚠️ BÀI TRÙNG! Không đăng.')
    for d in dupes: print(f\"  ID:{d['id']} | {d['title']['rendered']}\")
else:
    print('✅ Không trùng, an toàn để đăng')
" "$TITLE"
```
> ⚠️ Nếu bài trùng → **DỪNG**, thông báo Admin.

### Bước 1: Chuẩn bị
- Trích xuất Title, Content (HTML), Status (`draft` mặc định, `publish` nếu Admin yêu cầu)

### Bước 2: Đăng bài
```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)
curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts" \
     -u "admin:$WP_PASS" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Tiêu đề",
           "content": "<p>Nội dung HTML</p>",
           "status": "draft"
         }'
```

### Error Recovery

| HTTP Code | Nguyên nhân | Xử lý |
|-----------|-------------|-------|
| 401 | Sai credentials | Đọc lại `wp_credentials.txt`, thử 1 lần |
| 403 | Không quyền | Báo Admin |
| 500 | Server lỗi | Chờ 30s, retry tối đa 2 lần |

---

## 2. Audit Blog

### Trigger
- User: "Kiểm tra blog", "Blog có vấn đề gì?"
- Lệnh `/audit-blog`
- Tự động 1 lần/tuần qua cron

### Bước 1: Lấy danh sách bài
```bash
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=50&orderby=date&order=desc&_fields=id,title,status,date" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
for p in posts:
    print(f\"ID:{p['id']} | {p['status']} | {p['date'][:10]} | {p['title']['rendered']}\")
"
```

### Bước 2a: Phát hiện bài trùng
```bash
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=100&_fields=id,title,status,date" \
  | python3 -c "
import json, sys
from collections import Counter
posts = json.load(sys.stdin)
titles = [p['title']['rendered'] for p in posts]
dupes = {t: c for t, c in Counter(titles).items() if c > 1}
if dupes:
    print('⚠️ BÀI TRÙNG:')
    for title, count in dupes.items():
        matching = [p for p in posts if p['title']['rendered'] == title]
        for m in matching:
            print(f\"  ID:{m['id']} | {m['status']} | {m['date'][:10]} | {title}\")
else:
    print('✅ Không trùng lặp')
"
```

### Bước 2b: Draft cũ
```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?status=draft&per_page=50" \
  -u "admin:$WP_PASS" \
  | python3 -c "
import json, sys
for p in json.load(sys.stdin):
    print(f\"DRAFT | ID:{p['id']} | {p['date'][:10]} | {p['title']['rendered']}\")
"
```

### Bước 2c: SEO Check
- Tiêu đề > 60 ký tự? → Quá dài
- Tiêu đề < 20 ký tự? → Quá ngắn
- Nội dung < 300 từ? → Thin content

### Bước 3: Xóa bài trùng (CHỈ KHI ADMIN CHO PHÉP)
```bash
# KHÔNG TỰ XÓA — liệt kê rồi chờ "xóa đi"
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)
curl -X DELETE "https://blog.chaiko.info/wp-json/wp/v2/posts/[POST_ID]?force=true" \
  -u "admin:$WP_PASS"
```

### Bước 4: Format báo cáo
```
📋 **Audit Blog — blog.chaiko.info**
📊 Tổng: [N] bài | Published: [N] | Draft: [N]
🔁 Trùng lặp: [N] nhóm
📝 Draft cũ: [N] bài
📏 SEO issues: [N] bài
✅ OK: [N] bài
```

## Kết hợp
- `seo-writer` → viết bài → wp-publisher đăng
- `social-media` → cross-post từ blog ra social
- `daily-reporter` → audit results feed vào báo cáo ngày

## Lưu kết quả
- Audit: `workspace/reports/blog-audit-YYYY-MM-DD.md`

## Quy tắc
- ✅ Luôn kiểm tra trùng trước khi đăng
- ✅ Default status = `draft` (trừ khi Admin nói publish)
- ❌ KHÔNG hiển thị password trong chat
- ❌ KHÔNG xóa bài mà chưa được Admin duyệt
