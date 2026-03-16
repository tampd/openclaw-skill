# WordPress REST API Reference — blog.chaiko.info

> Tham chiếu API đầy đủ. Đọc khi cần thao tác với blog.

## Authentication

```bash
# Đọc credentials
WP_USER="admin"
WP_PASS=$(grep -oP 'WP_APP_PASSWORD="\K[^"]+' /root/openclaw/workspace/wp_credentials.txt)

# Auth header (cho curl)
-u "$WP_USER:$WP_PASS"
```

> ⚠️ KHÔNG hiển thị password trong chat. Luôn đọc từ file.
> ⚠️ Mọi thao tác tạo/sửa/xóa đều CẦN auth. Chỉ GET public endpoints không cần.

## Base URL
```
https://blog.chaiko.info/wp-json/wp/v2
```

---

## Posts API

### List Posts
```bash
# Public — 10 bài mới nhất
curl -s "$BASE/posts?per_page=10&_fields=id,title,date,categories,tags,status,slug"

# Authenticated — bao gồm draft
curl -s -u "$WP_USER:$WP_PASS" "$BASE/posts?status=draft,publish,future&per_page=50&_fields=id,title,date,status,categories"

# Search
curl -s "$BASE/posts?search=keyword&_fields=id,title,status"

# By category
curl -s "$BASE/posts?categories=2&per_page=20&_fields=id,title,date"

# By tag
curl -s "$BASE/posts?tags=12&per_page=20&_fields=id,title,date"
```

### Create Post
```bash
curl -X POST "$BASE/posts" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tiêu đề bài viết",
    "content": "<p>Nội dung HTML</p>",
    "status": "draft",
    "categories": [2],
    "tags": [12],
    "slug": "tieu-de-bai-viet",
    "excerpt": "Mô tả ngắn cho meta description",
    "featured_media": 0,
    "author": 1
  }'
```

**Status values**: `draft` (mặc định), `publish`, `future` (scheduled), `pending`, `private`

**Scheduled post**: Đặt `status: "future"` + `date: "2026-03-15T09:00:00"`

### Update Post
```bash
curl -X POST "$BASE/posts/POST_ID" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tiêu đề mới",
    "categories": [2, 4],
    "status": "publish"
  }'
```

### Delete Post
```bash
# Move to trash
curl -X DELETE "$BASE/posts/POST_ID" -u "$WP_USER:$WP_PASS"

# Permanent delete
curl -X DELETE "$BASE/posts/POST_ID?force=true" -u "$WP_USER:$WP_PASS"
```

> ⚠️ KHÔNG xóa mà chưa được Admin duyệt. Luôn liệt kê trước.

---

## Categories API

```bash
# List all
curl -s "$BASE/categories?per_page=100&_fields=id,name,slug,count"

# Create new category
curl -X POST "$BASE/categories" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{"name": "Tên Category", "slug": "ten-category", "description": "Mô tả"}'
```

---

## Tags API

```bash
# List all
curl -s "$BASE/tags?per_page=100&_fields=id,name,slug,count"

# Create new tag
curl -X POST "$BASE/tags" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{"name": "tag-name"}'

# Search tags
curl -s "$BASE/tags?search=ai&_fields=id,name"
```

---

## Media API (Featured Image)

### Upload Image
```bash
curl -X POST "$BASE/media" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Disposition: attachment; filename=image-name.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @/path/to/image.jpg
```

### Set Featured Image
```bash
# Sau khi upload, lấy media ID → gán vào post
curl -X POST "$BASE/posts/POST_ID" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{"featured_media": MEDIA_ID}'
```

---

## Yoast SEO Fields (Custom)

> Yoast SEO v27 expose các field qua REST API (nếu đã cấu hình):

```bash
# Đọc Yoast data
curl -s "$BASE/posts/POST_ID?_fields=id,yoast_head_json"

# Set Yoast meta khi tạo/update post
curl -X POST "$BASE/posts/POST_ID" \
  -u "$WP_USER:$WP_PASS" \
  -H "Content-Type: application/json" \
  -d '{
    "yoast_meta": {
      "yoast_wpseo_focuskw": "focus keyword",
      "yoast_wpseo_metadesc": "Meta description 120-155 chars",
      "yoast_wpseo_title": "SEO Title %%sep%% %%sitename%%"
    }
  }'
```

> ⚠️ Yoast REST API có thể cần plugin "Yoast SEO REST API" hoặc custom hook. Nếu 403 → dùng excerpt thay cho meta desc.

---

## Users API

```bash
curl -s "$BASE/users?_fields=id,name,slug"
# Response: [{"id":1,"name":"Chaiko Team","slug":"admin"}]
```

---

## Error Codes

| HTTP | Nguyên nhân | Xử lý |
|---|---|---|
| 200 | OK | — |
| 201 | Created | Bài/media đã tạo |
| 400 | Bad request | Check JSON format |
| 401 | Unauthorized | Đọc lại credentials, retry 1 lần |
| 403 | Forbidden | Không đủ quyền — báo Admin |
| 404 | Not found | Post/category ID sai |
| 500 | Server error | Chờ 30s, retry tối đa 2 lần |

## Pagination

```bash
# Response headers
# X-WP-Total: tổng items
# X-WP-TotalPages: tổng trang
# Dùng ?page=2&per_page=50 để phân trang
```

## Useful `_fields` Combinations

| Use case | _fields |
|---|---|
| List overview | `id,title,date,status,categories` |
| Full post | `id,title,content,excerpt,date,status,categories,tags,slug,featured_media` |
| Audit | `id,title,status,date,categories,modified` |
| WHOIS check | `id,title` |
