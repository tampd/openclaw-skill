---
name: wp-publisher
description: "WordPress manager cho blog.chaiko.info: đăng bài, quản lý category/tag, Yoast SEO, audit, scheduling, media, analytics. Đọc knowledge/ để biết config blog."
---

# WordPress Manager — Blog Chaiko.info

## Mục đích
Quản trị toàn diện blog.chaiko.info: đăng bài, lên lịch, tối ưu SEO Yoast, audit, quản lý media, phân loại bài viết, và analytics.

## ⚠️ QUAN TRỌNG — ĐỌC TRƯỚC KHI LÀM GÌ
- **Config**: đọc `knowledge/blog-config.md` để biết categories, tags, author
- **API**: đọc `knowledge/api-reference.md` khi cần cú pháp curl
- **Content**: đọc `knowledge/content-guidelines.md` khi viết/review bài
- **Templates**: đọc `knowledge/posting-templates.md` khi tạo bài mới
- **Credentials**: `/root/openclaw/workspace/wp_credentials.txt` — **KHÔNG hiển thị password**

---

## Routing Table — Keyword → Action

| Keyword / Trigger | Action |
|---|---|
| "đăng bài", "publish", "post bài" | → [1. Đăng Bài](#1-đăng-bài) |
| "audit blog", "kiểm tra blog" | → [2. Audit Blog](#2-audit-blog) |
| "lịch đăng", "calendar", "lên lịch" | → [3. Scheduling](#3-scheduling) |
| "sửa bài", "update post", "edit" | → [4. Edit Post](#4-edit-post) |
| "upload ảnh", "featured image" | → [5. Media](#5-media-upload) |
| "thống kê blog", "analytics" | → [6. Analytics](#6-analytics) |
| "re-categorize", "phân loại lại" | → [7. Re-categorize](#7-re-categorize) |
| "viết bài SEO" | → Chuyển cho `seo-writer` → quay lại đăng |

---

## 1. Đăng Bài

### Quy trình 7 bước (BẮT BUỘC theo thứ tự)

### PRE-FLIGHT GATE — được publish hay không?
Trước khi tạo hoặc publish post, tự check đủ 4 điều kiện sau:
- [ ] Nội dung đúng tone với audience mục tiêu (nếu chủ đề rộng/đang trend → ưu tiên dễ hiểu, ít jargon, gần gũi)
- [ ] Có ít nhất **3 ảnh dùng lại được** và đã chuẩn bị alt text + credit/source
- [ ] Có ít nhất **1 featured image**
- [ ] Có internal links + external source

**Nếu thiếu một trong các điều kiện trên:**
- **KHÔNG ĐƯỢC publish**
- chỉ được tạo `draft` hoặc tiếp tục hoàn thiện
- nếu user yêu cầu "đăng luôn" nhưng bài vẫn thiếu ảnh/tone chưa đạt → phải sửa xong rồi mới publish, không được bỏ qua gate này


#### Bước 1: Kiểm tra trùng lặp
```bash
TITLE="Tiêu đề bài viết"
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?search=$(echo "$TITLE" | head -c 50 | sed 's/ /+/g')&_fields=id,title,status" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
dupes = [p for p in posts if p['title']['rendered'].strip().lower() == sys.argv[1].strip().lower()]
if dupes:
    print('⚠️ BÀI TRÙNG! DỪNG.')
    for d in dupes: print(f\"  ID:{d['id']} | {d['title']['rendered']}\")
else:
    print('✅ Không trùng, tiếp tục')
" "$TITLE"
```
> ⚠️ Nếu trùng → **DỪNG**, thông báo Admin.

#### Bước 2: Chọn Category
Đọc `knowledge/blog-config.md` → match keyword triggers → chọn đúng category ID.

**KHÔNG BAO GIỜ** đăng vào Uncategorized (ID: 1).

```
Category Map (tham khảo nhanh):
  2 = Nghiên cứu AI     | 3 = Hướng dẫn      | 4 = Phân tích
  5 = Bảo mật           | 6 = Công nghệ lõi   | 7 = Tương lai
```

#### Bước 3: Chọn Tags
- Tìm tag hiện có: `curl -s "...tags?search=keyword&_fields=id,name"`
- Nếu chưa có → tạo mới via API (xem `api-reference.md`)
- **Tối đa 5 tags/bài**, format: tiếng Anh, lowercase, gạch ngang

#### Bước 4: Chuẩn bị SEO + Tone
- **Slug**: ngắn gọn, chứa keyword chính, tiếng Việt không dấu + dấu gạch ngang
- **Excerpt**: 120-155 ký tự, tóm tắt giá trị bài viết (dùng làm meta desc)
- **Focus keyphrase**: 1 keyword target chính
- **Tone check**: nếu bài nhằm phổ cập trend/công nghệ mới cho số đông, phải viết theo hướng giải thích dễ hiểu trước, kỹ thuật sâu sau; tránh mở bài quá học thuật hoặc quá nhiều jargon liên tiếp

#### Bước 5: Chuẩn bị ảnh (BẮT BUỘC)
- Tối thiểu **3 ảnh dùng lại được** cho mỗi bài publish
- Tối thiểu **1 featured image**
- Mỗi ảnh phải có:
  - file local hoặc URL nguồn rõ ràng
  - alt text tiếng Việt
  - ghi chú license/nguồn nếu cần
- Upload ảnh trước hoặc cùng lúc với bài; set featured image trước khi chốt publish
- Nếu không tìm được ảnh hợp lệ → **không publish**, chỉ tạo draft hoặc báo Sếp

#### Bước 6: Đăng bài
```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)
curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts" \
  -u "admin:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tiêu đề",
    "content": "<p>Nội dung HTML — dùng template từ posting-templates.md</p>",
    "status": "draft",
    "categories": [2],
    "tags": [12],
    "slug": "tieu-de-bai-viet",
    "excerpt": "Meta description 120-155 chars",
    "author": 1
  }'
```

**Quy tắc status**:
- Mặc định: `draft` → thông báo Admin review
- `publish`: CHỈ khi Admin nói rõ "đăng luôn" / "publish" **và** đã vượt qua PRE-FLIGHT GATE (đủ ảnh, tone đạt, SEO đạt)
- `future`: khi lên lịch (kèm `date`)

---

## 2. Audit Blog

### Trigger
- "kiểm tra blog", "audit blog", "blog có vấn đề gì?"
- Lệnh `/audit-blog`

### Quy trình audit toàn diện

```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)

echo "=== THỐNG KÊ ==="
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=1" -I 2>/dev/null | grep -i x-wp-total

echo "=== BÀI TRÙNG ==="
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=100&_fields=id,title,status,date,categories" \
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

echo "=== DRAFT CŨ ==="
curl -s -u "admin:$WP_PASS" "https://blog.chaiko.info/wp-json/wp/v2/posts?status=draft&per_page=50&_fields=id,title,date" \
  | python3 -c "
import json, sys
for p in json.load(sys.stdin):
    print(f\"DRAFT | ID:{p['id']} | {p['date'][:10]} | {p['title']['rendered']}\")
"

echo "=== UNCATEGORIZED ==="
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?categories=1&per_page=50&_fields=id,title,date" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
if posts:
    print(f'⚠️ {len(posts)} bài chưa phân loại:')
    for p in posts:
        print(f\"  ID:{p['id']} | {p['date'][:10]} | {p['title']['rendered']}\")
else:
    print('✅ Tất cả đã phân loại')
"

echo "=== SEO CHECK ==="
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=100&_fields=id,title,content" \
  | python3 -c "
import json, sys, re
posts = json.load(sys.stdin)
issues = []
for p in posts:
    title_len = len(p['title']['rendered'])
    content_text = re.sub(r'<[^>]+>', '', p['content']['rendered'])
    word_count = len(content_text.split())
    problems = []
    if title_len > 60: problems.append(f'title quá dài ({title_len} chars)')
    if title_len < 20: problems.append(f'title quá ngắn ({title_len} chars)')
    if word_count < 300: problems.append(f'thin content ({word_count} words)')
    if problems:
        issues.append(f\"  ID:{p['id']} | {p['title']['rendered'][:50]} → {', '.join(problems)}\")
if issues:
    print(f'⚠️ {len(issues)} bài có vấn đề SEO:')
    for i in issues: print(i)
else:
    print('✅ SEO OK')
"

echo "=== PHÂN BỐ CATEGORY ==="
curl -s "https://blog.chaiko.info/wp-json/wp/v2/categories?_fields=id,name,count" \
  | python3 -c "
import json, sys
for c in json.load(sys.stdin):
    bar = '█' * c['count']
    print(f\"  {c['name']:15} ({c['id']}): {c['count']:3} {bar}\")
"
```

### Format báo cáo
```
📋 **Audit Blog — blog.chaiko.info**
📊 Tổng: [N] bài | Published: [N] | Draft: [N] | Scheduled: [N]
🔁 Trùng lặp: [N] nhóm
📝 Draft cũ: [N] bài
📂 Uncategorized: [N] bài ← CẦN PHÂN LOẠI
📏 SEO issues: [N] bài
📊 Phân bố: [chart]
✅ Điểm sức khỏe: [X/10]
```

---

## 3. Scheduling

```bash
# Đăng bài lên lịch
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)
curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts" \
  -u "admin:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tiêu đề",
    "content": "<p>Nội dung</p>",
    "status": "future",
    "date": "2026-03-15T09:00:00",
    "categories": [2]
  }'

# Xem bài scheduled
curl -s -u "admin:$WP_PASS" \
  "https://blog.chaiko.info/wp-json/wp/v2/posts?status=future&_fields=id,title,date" \
  | python3 -c "
import json, sys
for p in json.load(sys.stdin):
    print(f\"📅 {p['date'][:16]} | {p['title']['rendered']}\")
"
```

### Lịch đề xuất (từ content-guidelines.md)
- T2: Nghiên cứu AI / Phân tích (dài, chuyên sâu)
- T4: Hướng dẫn / Tutorial
- T6: Bảo mật / Trend / Tin nhanh
- Giờ tối ưu: **09:00** hoặc **20:00** (GMT+7 = UTC+7)

---

## 4. Edit Post

```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)

# Update title, categories, status
curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts/POST_ID" \
  -u "admin:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tiêu đề mới",
    "categories": [2, 4],
    "status": "publish"
  }'
```

---

## 5. Media Upload

```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)

# Upload image
MEDIA_ID=$(curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/media" \
  -u "admin:$WP_PASS" \
  -H "Content-Disposition: attachment; filename=image.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @/path/to/image.jpg \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")

# Set as featured image
curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts/POST_ID" \
  -u "admin:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d "{\"featured_media\": $MEDIA_ID}"
```

---

## 6. Analytics

```bash
# Phân bố bài theo thời gian
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=100&_fields=date,categories" \
  | python3 -c "
import json, sys
from collections import Counter
posts = json.load(sys.stdin)
months = Counter(p['date'][:7] for p in posts)
print('📊 Bài viết theo tháng:')
for m, c in sorted(months.items()):
    print(f'  {m}: {c} bài {\"█\" * c}')
print(f'📈 Tổng: {len(posts)} bài')
print(f'📅 Trung bình: {len(posts)/max(len(months),1):.1f} bài/tháng')
"

# Content Calendar — 10 bài gần nhất
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?per_page=10&_fields=id,title,date,categories,status" \
  | python3 -c "
import json, sys
CAT_MAP = {1:'Uncategorized', 2:'AI', 3:'Tutorial', 4:'Phân tích', 5:'Bảo mật', 6:'Hardware', 7:'Tương lai'}
for p in json.load(sys.stdin):
    cats = ', '.join(CAT_MAP.get(c, str(c)) for c in p['categories'])
    icon = '✅' if p['status'] == 'publish' else '📝'
    print(f\"{icon} {p['date'][:10]} | [{cats}] {p['title']['rendered'][:60]}\")
"
```

---

## 7. Re-categorize

Khi bài bị đặt sai Uncategorized hoặc sai category:

```bash
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)

# Di chuyển bài sang đúng category
curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts/POST_ID" \
  -u "admin:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{"categories": [2]}'
```

### Auto-suggest category
Đọc tiêu đề bài → match với keyword triggers trong `knowledge/blog-config.md` → đề xuất category.

---

## Pipeline tích hợp

```
seo-writer (viết bài SEO)
    ↓
wp-publisher (đăng blog — skill này)
    ↓
social-media (cross-post ra FB/LinkedIn)
    ↓
daily-reporter (báo cáo kết quả)
```

## Quy tắc An toàn

| Quy tắc | Chi tiết |
|---|---|
| ✅ Luôn kiểm tra trùng | Bước 1 là BẮT BUỘC trước khi đăng |
| ✅ Default = draft | Trừ khi Admin nói "publish" / "đăng luôn" |
| ✅ Chọn đúng category | KHÔNG đăng vào Uncategorized |
| ✅ SEO trước khi publish | Slug + excerpt + tags phải có |
| ✅ Ảnh trước khi publish | Ít nhất 3 ảnh + 1 featured image + alt text |
| ✅ Tone đúng audience | Bài trend/phổ cập phải dễ hiểu trước, kỹ thuật sau |
| ❌ KHÔNG hiển thị password | Đọc từ file, không in ra chat |
| ❌ KHÔNG xóa bài | Chưa được Admin duyệt → liệt kê rồi hỏi |
| ❌ KHÔNG bulk publish | Tối đa 3 bài/lần, confirm với Admin |

## Lưu kết quả
- Audit: `workspace/reports/blog-audit-YYYY-MM-DD.md`
- Post log: ghi ID + URL bài vừa đăng vào chat

## ⚠️ Post-Action Verification (BẮT BUỘC)

Sau **MỖI** action (publish, edit, re-categorize, media upload):

```bash
# Verify bài đã thay đổi đúng
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts/POST_ID?_fields=id,title,status,categories,slug" | python3 -m json.tool
```

**Quy tắc:**
1. Gọi API verify → so sánh với expected state → confirm hoặc báo lỗi
2. Nếu API trả kết quả khác expected → retry 1 lần → nếu vẫn sai → báo Sếp
3. **KHÔNG BAO GIỜ** nói "đã xong" mà không verify qua API

## ⚠️ Audit-Then-Fix (BẮT BUỘC)

Khi chạy audit phát hiện lỗi:
1. **FIX NGAY** các lỗi có thể tự sửa (re-categorize, SEO meta, draft cleanup)
2. Chỉ report mà KHÔNG fix → **VI PHẠM** kỷ luật thực thi
3. Lỗi không thể tự fix (cần sửa front-end, cần Sếp quyết) → báo rõ "Cần Sếp xử lý: [lý do]"
