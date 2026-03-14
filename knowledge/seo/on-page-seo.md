# On-Page SEO — Kiến thức chuyên sâu

## Keyword Research

### Search Intent (Ý định tìm kiếm)
| Loại | Mô tả | Ví dụ | Content phù hợp |
|---|---|---|---|
| **Informational** | Tìm thông tin | "VPS là gì" | Blog, guide, FAQ |
| **Navigational** | Tìm trang cụ thể | "BKNS đăng nhập" | Landing page |
| **Commercial** | So sánh, review | "VPS BKNS vs Vultr" | Comparison, review |
| **Transactional** | Mua/đăng ký | "mua VPS giá rẻ" | Product page, pricing |

### Quy trình nghiên cứu từ khóa
1. **Seed keywords** → brainstorm từ khóa gốc (VPS, hosting, tên miền)
2. **Mở rộng** → Google Keyword Planner, Ubersuggest, AnswerThePublic
3. **Phân tích** → Volume, Keyword Difficulty (KD), CPC, SERP features
4. **Lọc** → Loại KD quá cao (>70), volume quá thấp (<10/tháng)
5. **Nhóm** → Topic clusters: 1 pillar + nhiều cluster pages
6. **Map** → Gắn keyword → URL cụ thể (keyword mapping)

### Long-tail Keywords
- Ít traffic nhưng **conversion rate cao hơn** 2-3x
- Ví dụ: "mua VPS giá rẻ cho WordPress" vs "VPS"
- Dễ rank hơn cho site mới

### Keyword Research cho tiếng Việt
- Google Keyword Planner (set location: Vietnam, language: Vietnamese)
- Khác biệt: dấu vs không dấu ("tên miền" vs "ten mien")
- Google Suggest (autocomplete) rất hữu ích
- AnswerThePublic, AlsoAsked cho câu hỏi phổ biến

---

## Content Optimization

### E-E-A-T Framework (Experience, Expertise, Authoritativeness, Trustworthiness)
- **Experience**: Thể hiện kinh nghiệm thực tế (case study, screenshots, testimonials)
- **Expertise**: Nội dung chuyên sâu, chính xác, có data/source
- **Authoritativeness**: Author bio, credentials, backlinks từ site uy tín
- **Trustworthiness**: HTTPS, privacy policy, contact info, reviews

### Cấu trúc bài viết SEO chuẩn
1. **Title Tag** (50-60 ký tự): keyword chính + compelling hook
   - Pattern: `[Primary Keyword] — [Benefit/Year] | [Brand]`
   - Ví dụ: `Cloud VPS Giá Rẻ — Từ 69K/tháng, SSD NVMe 2026 | BKNS`
2. **Meta Description** (130-160 ký tự): tóm tắt + CTA + keyword
3. **URL**: ngắn, có keyword, dùng gạch nối
   - ✅ `/vps-gia-re` | ❌ `/san-pham?id=123&cat=vps`
4. **H1**: 1 per page, chứa primary keyword
5. **H2-H6**: subheadings có keyword variants/LSI
6. **First 100 words**: chứa primary keyword tự nhiên
7. **Body**: keyword density 1-2%, LSI keywords, NLP entities
8. **Images**: alt text mô tả + keyword, file name có keyword

### Content Length Guidelines
| Loại content | Độ dài khuyên dùng |
|---|---|
| Blog post thường | 1,000-1,500 từ |
| Pillar/guide | 2,500-5,000 từ |
| Product page | 500-1,000 từ |
| FAQ | 100-300 từ / answer |
| Landing page | 300-800 từ |

---

## Internal Linking Strategy

### Topic Cluster Model
```
        [Pillar: "VPS Là Gì"]
           /     |     \
[Cluster 1]  [Cluster 2]  [Cluster 3]
VPS Linux    VPS Windows   VPS vs Hosting
```

### Best Practices
- Anchor text mô tả, có keyword (không "click here")
- Mỗi trang nên có 3-5 internal links
- Link từ high-authority pages → new/important pages
- Dùng breadcrumb cho navigation
- Tránh orphan pages (trang không có link nào trỏ đến)

---

## Image Optimization
- **Alt text**: mô tả chính xác, có keyword khi tự nhiên
- **File name**: `vps-gia-re-bkns.webp` (không `IMG_1234.jpg`)
- **Format**: WebP > JPEG > PNG (cho photos), SVG cho icons
- **Size**: compress trước upload, max 200KB cho blog images
- **Lazy loading**: `loading="lazy"` cho images below fold
- **Responsive**: `srcset` cho multiple sizes

## Featured Snippets
- **Paragraph snippet**: Trả lời câu hỏi trong 40-60 từ ngay sau H2
- **List snippet**: Sử dụng numbered/bulleted list
- **Table snippet**: Dùng `<table>` cho so sánh/data
- **Trigger**: Target câu hỏi "là gì", "cách", "tại sao", "bao nhiêu"

## Content Freshness
- Cập nhật bài cũ mỗi 3-6 tháng (update date, stats, links)
- Google ưu tiên content fresh cho query có tính thời sự
- Content audit quarterly: loại/merge bài traffic thấp, update bài tiềm năng
