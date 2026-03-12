---
name: blog-auditor
description: Kiểm tra sức khỏe blog blog.chaiko.info — phát hiện bài trùng lặp, lỗi, và đánh giá SEO cơ bản qua WordPress REST API.
---

# Blog Auditor — Kiểm Tra Sức Khỏe Blog

## Mục đích
Kiểm tra blog **blog.chaiko.info** để phát hiện vấn đề: bài viết trùng lặp, bài lỗi, SEO thiếu sót. Báo cáo cho Admin để xử lý.

## ⚠️ QUAN TRỌNG
- Dùng **WordPress REST API** qua `curl`, KHÔNG dùng browser
- API endpoint: `https://blog.chaiko.info/wp-json/wp/v2/posts`
- Credentials: đọc từ `/root/openclaw/workspace/wp_credentials.txt`

## Khi nào kích hoạt
- User yêu cầu: "Kiểm tra blog", "Blog có vấn đề gì không?"
- Lệnh `/audit-blog` từ Admin
- Tự động 1 lần/tuần qua cron

## Quy trình

### Bước 1: Lấy danh sách bài viết

```bash
# Lấy 50 bài gần nhất (JSON)
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=50&orderby=date&order=desc" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
for p in posts:
    print(f\"ID:{p['id']} | Status:{p['status']} | Date:{p['date']} | Title:{p['title']['rendered']}\")
"

# Lấy tổng số bài
curl -sI "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=1" | grep -i x-wp-total
```

### Bước 2: Phân tích

Kiểm tra các vấn đề sau:

#### 2a. Bài trùng lặp (Duplicate Detection)
```bash
# Tìm bài có tiêu đề giống nhau
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=100&_fields=id,title,status,date" \
  | python3 -c "
import json, sys
from collections import Counter
posts = json.load(sys.stdin)
titles = [p['title']['rendered'] for p in posts]
dupes = {t: c for t, c in Counter(titles).items() if c > 1}
if dupes:
    print('⚠️ BÀI TRÙNG LẶP:')
    for title, count in dupes.items():
        matching = [p for p in posts if p['title']['rendered'] == title]
        for m in matching:
            print(f\"  ID:{m['id']} | {m['status']} | {m['date'][:10]} | {title}\")
else:
    print('✅ Không có bài trùng lặp')
"
```

#### 2b. Bài lỗi / Draft bị bỏ quên
```bash
# Tìm drafts cũ (> 7 ngày)
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?status=draft&per_page=50" \
  -u "admin:$(cat /root/openclaw/workspace/wp_credentials.txt | grep -oP 'password:\s*\K.*')" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
for p in posts:
    print(f\"DRAFT | ID:{p['id']} | {p['date'][:10]} | {p['title']['rendered']}\")
"
```

#### 2c. SEO Check cơ bản
Cho mỗi bài published, kiểm tra:
- Tiêu đề có > 60 ký tự? (quá dài cho SEO)
- Tiêu đề có < 20 ký tự? (quá ngắn)
- Nội dung có < 300 từ? (thin content)

### Bước 3: Xóa bài trùng (NẾU được Admin cho phép)

> ⚠️ **KHÔNG TỰ XÓA**. Liệt kê bài cần xóa và **chờ Admin xác nhận "xóa đi"** trước.

```bash
# Xóa bài (chỉ khi Admin nói OK)  
curl -X DELETE "https://blog.chaiko.info/wp-json/wp/v2/posts/[POST_ID]?force=true" \
  -u "admin:$(cat /root/openclaw/workspace/wp_credentials.txt | grep -oP 'password:\s*\K.*')"
```

### Bước 4: Báo cáo

```
📋 **Báo Cáo Audit Blog — blog.chaiko.info**

📊 **Tổng quan:**
- Tổng bài viết: [N]
- Published: [N] | Draft: [N]

⚠️ **Vấn đề phát hiện:**

🔁 **Bài trùng lặp** ([N] nhóm):
1. "[Tiêu đề]" — [N] bản (ID: [X], [Y])
   → Đề xuất: Giữ ID [X], xóa ID [Y]

📝 **Draft cũ** ([N] bài):
1. ID:[X] | "[Tiêu đề]" | Tạo: [date]
   → Đề xuất: Xóa hoặc publish

📏 **SEO Issues** ([N] bài):
1. ID:[X] — Tiêu đề quá dài (65 ký tự)
2. ID:[Y] — Nội dung quá ngắn (150 từ)

✅ **Bài OK**: [N] bài không có vấn đề

🎯 **Hành động cần làm:**
- [ ] Xóa [N] bài trùng lặp
- [ ] Dọn [N] draft cũ
- [ ] Sửa [N] bài SEO issues
```

## Lưu kết quả audit
Lưu vào: `/root/openclaw/workspace/reports/blog-audit-[YYYY-MM-DD].md`

## Lưu ý bảo mật
- Đọc credentials từ file, KHÔNG hiển thị password trong chat
- Log audit KHÔNG chứa credentials
