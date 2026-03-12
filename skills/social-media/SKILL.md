---
name: social-media
description: Quản lý social media đa nền tảng — đăng bài, lên lịch, tracking trên Facebook, LinkedIn, X/Twitter.
---

# Social Media Manager

## Mục đích
Giúp Sếp quản lý nội dung social media cho BKNS/Vcharge — đăng bài, lên lịch, theo dõi engagement.

## Khi nào kích hoạt
- User nói: "đăng bài", "post lên facebook/linkedin", "social media", "marketing"
- User muốn lên lịch đăng bài, tạo nội dung marketing

## Quy trình đăng bài

### 1. Soạn nội dung
Khi Sếp yêu cầu tạo bài đăng, tạo theo format:

```markdown
## 📱 Social Post — [Chủ đề]

**Platform**: [Facebook / LinkedIn / X / All]
**Tone**: [Chuyên nghiệp / Thân thiện / Urgent]
**Hashtags**: #BKNS #CloudVPS #Hosting

---

[Nội dung bài đăng — tối đa 280 ký tự cho X, 500 cho Facebook/LinkedIn]

---

📷 **Ảnh đề xuất**: [Mô tả ảnh cần thiết]
🔗 **Link**: [URL nếu có]
⏰ **Lịch đăng**: [Ngày giờ — GMT+7]
```

### 2. Đăng bài qua n8n workflow
```bash
# Trigger n8n social media workflow
curl -s -X POST "https://n8n.chaiko.info/webhook/social-post" \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "facebook",
    "content": "Nội dung bài đăng",
    "image_url": "https://...",
    "scheduled_at": "2026-03-13T09:00:00+07:00"
  }'
```

### 3. Content Calendar
Lưu lịch đăng bài tại: `workspace/memory/content-calendar.md`

```markdown
# 📅 Content Calendar

## Tuần [DD/MM - DD/MM]

| Ngày | Platform | Nội dung | Status |
|---|---|---|---|
| T2 | LinkedIn | [Mô tả] | ⏳ Scheduled |
| T4 | Facebook | [Mô tả] | ✅ Posted |
| T6 | X | [Mô tả] | 📝 Draft |
```

## Template nội dung theo ngành

### BKNS — Cloud/Hosting
- Focus: Giải pháp, so sánh gói, tips kỹ thuật
- Tone: Chuyên nghiệp, tech-savvy
- CTA: Link tới sản phẩm, hotline

### Vcharge — Sạc xe điện
- Focus: Tiện ích, tiết kiệm, trending EV
- Tone: Thân thiện, eco-friendly
- CTA: Liên hệ tư vấn

## Kết hợp
- `seo-writer`: Soạn bài blog dài → tóm gọn thành social posts
- `office-assistant`: Soạn email marketing → cross-post lên social
- `n8n-workflow`: Trigger đăng bài tự động qua workflow

## Quy tắc
- ✅ Confirm nội dung trước khi đăng
- ✅ Dùng hashtags phù hợp ngành
- ✅ Optimal posting times: 9h, 12h, 18h VN
- ❌ KHÔNG spam — tối đa 2 posts/ngày/platform
- ❌ KHÔNG đăng thông tin chưa xác thực
