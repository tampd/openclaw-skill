---
name: social-media
description: Quản lý social media đa nền tảng — đăng bài, trả lời comment/inbox, theo dõi insights trên Facebook (Tý Tech), LinkedIn, X/Twitter.
---

# Social Media Manager

## Mục đích
Giúp Sếp quản lý nội dung social media — đặc biệt fanpage **Tý Tech** trên Facebook + các nền tảng khác.

## Khi nào kích hoạt
- User nói: "đăng bài", "post lên facebook", "social media", "marketing", "tý tech", "fanpage"
- User muốn lên lịch đăng bài, tạo nội dung marketing, xem insights
- User hỏi về comment, inbox fanpage

## Credentials
```bash
# Load Facebook credentials
source /root/openclaw/.openclaw/credentials/fb-credentials.env
```

---

## Facebook Graph API — Fanpage Tý Tech

### Thông tin Fanpage
- **Tên**: Tý Tech
- **Page ID**: 1012410591957125
- **Category**: Tech · Internet marketing service
- **API Version**: v22.0
- **Knowledge file**: `workspace/knowledge/facebook-tytech.md`

### 1. Đăng bài (Text)
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s -X POST "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/feed" \
  -d "message=Nội dung bài đăng" \
  -d "access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 2. Đăng bài kèm ảnh (URL)
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s -X POST "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/photos" \
  -d "url=https://example.com/image.jpg" \
  -d "message=Caption cho ảnh" \
  -d "access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 3. Đăng bài kèm link
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s -X POST "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/feed" \
  -d "message=Mô tả bài viết" \
  -d "link=https://blog.chaiko.info/bai-viet" \
  -d "access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 4. Lên lịch đăng bài (Scheduled Post)
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
# scheduled_publish_time = Unix timestamp (phải >= 10 phút sau, <= 75 ngày)
SCHEDULE_TIME=$(date -d "2026-03-15 09:00:00 +0700" +%s)
curl -s -X POST "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/feed" \
  -d "message=Bài đăng lên lịch" \
  -d "published=false" \
  -d "scheduled_publish_time=${SCHEDULE_TIME}" \
  -d "access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 5. Đọc bài viết trên page
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/feed?\
fields=message,created_time,likes.summary(true),comments.summary(true),shares&\
limit=10&access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 6. Đọc comments trên 1 bài viết
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/{POST_ID}/comments?\
fields=from,message,created_time&access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 7. Trả lời comment
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s -X POST "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/{COMMENT_ID}/comments" \
  -d "message=Cảm ơn bạn nhé! 🙏" \
  -d "access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 8. Đọc inbox (Conversations)
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/conversations?\
fields=participants,messages{message,from,created_time}&\
access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 9. Trả lời inbox
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s -X POST "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/{CONVERSATION_ID}/messages" \
  -d "message=Chào bạn, cảm ơn đã liên hệ Tý Tech!" \
  -d "access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 10. Page Insights
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
# Metrics: page_impressions, page_engaged_users, page_fan_adds, page_views_total
curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/insights?\
metric=page_impressions,page_engaged_users,page_fan_adds,page_views_total&\
period=day&access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### 11. Xóa bài viết
```bash
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s -X DELETE "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/{POST_ID}?\
access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

---

## Soạn nội dung Social Post

Khi Sếp yêu cầu tạo bài đăng, soạn theo format:

```markdown
## 📱 Social Post — [Chủ đề]

**Platform**: Facebook (Tý Tech)
**Tone**: [Hài hước / Chuyên nghiệp / Insight]
**Hashtags**: #TýTech #IT #Developer

---

[Nội dung bài đăng]

---

📷 **Ảnh**: [Mô tả ảnh / URL]
🔗 **Link**: [URL nếu có]
⏰ **Lịch đăng**: [Ngày giờ — GMT+7]
```

## Content Calendar
Lưu tại: `workspace/memory/content-calendar.md`

## Kết hợp
- `seo-writer`: Blog dài → tóm gọn thành social posts
- `wp-publisher`: Đăng bài blog → cross-post lên Facebook
- `n8n-workflow`: Trigger đăng bài tự động qua webhook
- `seo-expert`: Tối ưu nội dung cho engagement

## Quy tắc
- ✅ **LUÔN confirm** nội dung trước khi đăng lên Facebook
- ✅ Dùng hashtags phù hợp (#TýTech, #ITLife, #Developer)
- ✅ Optimal posting: 7h30, 12h, 19h-21h VN (3 slots/ngày)
- ✅ Đa dạng content: memes, tips, stories, insights
- ✅ **3 posts/ngày** — theo lịch content-calendar + facebook-tytech.md
- ❌ KHÔNG đăng thông tin chưa xác thực
- ❌ KHÔNG tiết lộ credentials trong bài đăng

## Cross-post Blog → Fanpage
Khi có bài mới trên blog.chaiko.info:
1. Tóm gọn nội dung thành 300-500 ký tự
2. Thêm link blog + CTA: "Đọc full bài tại blog.chaiko.info"
3. Hashtags phù hợp chủ đề + #TýTech
4. Đăng vào slot phù hợp pillar (AI → sáng, Tips → tối)

## ⚠️ Post-Action Verification (BẮT BUỘC)
Sau mỗi lần đăng bài:
1. Gọi API đọc lại bài vừa đăng → xác nhận nội dung đúng
2. Ghi Post ID vào content-calendar
3. Nếu lỗi → báo cáo ngay, KHÔNG giả vờ đã đăng thành công
