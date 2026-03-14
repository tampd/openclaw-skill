# Image Strategy — SEO Article Images

> Hướng dẫn chiến lược hình ảnh cho bài viết SEO chuẩn BKNS.
> **Quy tắc vàng**: Mỗi H2 section phải có ≥1 hình ảnh minh họa.

---

## 1. Quy tắc bắt buộc

| Rule | Chi tiết |
|---|---|
| **Số lượng tối thiểu** | 8 ảnh / bài viết (1 hero + 1 per H2) |
| **Hero image** | Ngay sau H1, 1200×628px, chứa keyword trong alt text |
| **Alt text** | `[keyword] — [mô tả nội dung ảnh]` (không spam keyword) |
| **Format ưu tiên** | WebP > JPEG > PNG (chất lượng 80-85%) |
| **Max file size** | ≤200KB (hero ≤300KB) |
| **Kích thước body** | Width: 800px (auto height), retina-ready |
| **Lazy loading** | Bật cho tất cả ảnh trừ hero (above the fold) |
| **Caption** | Bắt buộc cho infographic, bảng giá — optional cho minh họa |

---

## 2. Loại ảnh theo vị trí trong bài

### 🎯 Hero Image (sau H1)
- **Loại**: Banner chuyên nghiệp, gradient background + text overlay
- **Nội dung**: Keyword chính + visual liên quan dịch vụ
- **Kích thước**: 1200×628px (chuẩn OG/social share)
- **Gợi ý prompt AI**: `"Professional banner for [topic], modern gradient, corporate style, clean typography, Vietnamese tech company"`

### 📊 Infographic / Sơ đồ (section khái niệm, cơ chế)
- **Loại**: Flow diagram, process chart, mind map
- **Khi nào dùng**: Giải thích quy trình, nguyên lý hoạt động, so sánh
- **Gợi ý prompt AI**: `"Clean infographic showing [process], flat design, numbered steps, blue/white corporate palette"`

### 📸 Screenshot / UI (section hướng dẫn)
- **Loại**: Screenshot thực tế dashboard, giao diện, kết quả
- **Khi nào dùng**: Hướng dẫn step-by-step, review giao diện
- **Chú ý**: Crop chính xác, highlight vùng quan trọng bằng box đỏ/mũi tên

### 🎨 Illustration (section lợi ích, phù hợp cho ai)
- **Loại**: Flat illustration, isometric, hoạt hình đơn giản
- **Khi nào dùng**: Minh họa khái niệm trừu tượng (tiết kiệm, bảo mật, tốc độ)
- **Gợi ý prompt AI**: `"Flat illustration showing [concept], modern tech style, pastel colors, no text"`

### 📋 Table / Chart Image (section so sánh, bảng giá)
- **Loại**: Rendered table hoặc chart (bar, pie)
- **Khi nào dùng**: Khi bảng HTML quá phức tạp hoặc cần visual impact
- **Chú ý**: Luôn kèm bảng HTML text cho accessibility + SEO

### ✅ Icon / Badge (section tiêu chí, lưu ý)
- **Loại**: Custom icon set, checkmark badges, warning icons
- **Khi nào dùng**: Highlight tiêu chí quan trọng, danh sách ưu/nhược điểm
- **Gợi ý**: Dùng icon inline (32×32 hoặc 48×48) kèm bullet list

---

## 3. Image Placement Map (theo template)

```
[H1 Title]
  └── 🖼️ HERO IMAGE (1200×628)

[H2: Khái niệm]
  └── 🖼️ INFOGRAPHIC — sơ đồ giải thích

[H2: Đối tượng / Vì sao]
  └── 🖼️ ILLUSTRATION — nhóm user icons

[H2: Cơ chế hoạt động]
  └── 🖼️ INFOGRAPHIC — flow diagram

[H2: Lợi ích]
  └── 🖼️ ILLUSTRATION — so sánh visual (TRƯỚC vs SAU)
  └── 🖼️ ILLUSTRATION — từng lợi ích (nếu có H3)

[H2: Phân loại]
  └── 🖼️ ILLUSTRATION — category icons/cards

[H2: Tiêu chí chọn]
  └── 🖼️ ICON SET — checklist infographic

[H2: Bảng so sánh]
  └── 🖼️ TABLE IMAGE — comparison matrix

[H2: Bảng giá]
  └── 🖼️ TABLE/CHART — pricing visual

[H2: Lưu ý]
  └── 🖼️ WARNING ICONS — tips graphic

[H2: CTA / Giới thiệu]
  └── 🖼️ BRAND IMAGE — logo + datacenter

[H2: FAQ]
  └── (Không cần ảnh — text-only section)
```

---

## 4. Tạo ảnh bằng AI — Workflow

Khi viết bài `/seo-bkns`, Tôm tự xác định cần ảnh gì cho mỗi section:

### Bước 1: Lên danh sách ảnh
Sau khi outline xong, liệt kê ảnh cần tạo:
```
📸 Danh sách ảnh cho bài "[title]":
1. Hero: [mô tả]
2. Section "[H2 name]": [loại ảnh] — [mô tả nội dung]
3. ...
```

### Bước 2: Tạo alt text trước
Alt text phải ready trước khi tạo ảnh:
```
alt="[keyword chính] — [mô tả cụ thể nội dung ảnh, 10-15 từ]"
```

### Bước 3: Gợi ý prompt
Với mỗi ảnh, gợi ý prompt phù hợp cho tool tạo ảnh AI:
- Phong cách: Professional, corporate, clean, modern
- Palette: Blue/white (BKNS brand), hoặc tùy chủ đề
- Layout: Flat design, no clutter, minimal text
- Ngôn ngữ prompt: English (chất lượng output tốt hơn)

### Bước 4: Naming convention
```
[slug]-[section]-[type].webp
Ví dụ:
  vps-treo-game-hero-banner.webp
  vps-treo-game-classification-infographic.webp
  vps-treo-game-comparison-table.webp
```

---

## 5. Tối ưu SEO cho ảnh

- ✅ Filename chứa keyword (dùng dấu gạch ngang)
- ✅ Alt text unique cho mỗi ảnh (không copy paste)
- ✅ Title attribute (optional): tooltip khi hover
- ✅ Caption: dùng `<figcaption>` cho context
- ✅ Structured data: ảnh trong Article schema
- ❌ KHÔNG dùng alt text rỗng (`alt=""`) 
- ❌ KHÔNG nhồi keyword trong alt text
- ❌ KHÔNG dùng ảnh stock generic không liên quan
