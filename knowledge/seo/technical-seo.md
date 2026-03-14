# Technical SEO — Kiến thức chuyên sâu

## Core Web Vitals (2025-2026)

### LCP (Largest Contentful Paint)
- **Tốt**: ≤ 2.5s | **Cần cải thiện**: 2.5s–4.0s | **Kém**: > 4.0s
- Fix: Optimize images (WebP/AVIF), preload critical resources, CDN, lazy load below-fold

### INP (Interaction to Next Paint) — thay thế FID từ 2024
- **Tốt**: ≤ 200ms | **Cần cải thiện**: 200ms–500ms | **Kém**: > 500ms
- Fix: Minimize JS execution, split long tasks, use web workers

### CLS (Cumulative Layout Shift)
- **Tốt**: ≤ 0.1 | **Cần cải thiện**: 0.1–0.25 | **Kém**: > 0.25
- Fix: Set width/height cho images/videos, avoid dynamic content injection above fold

---

## Crawlability & Indexability

### robots.txt
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Sitemap: https://example.com/sitemap.xml
```

### XML Sitemap
- Giới hạn 50,000 URLs / file, < 50MB uncompressed
- Dùng `<lastmod>`, `<changefreq>`, `<priority>`
- Submit qua Google Search Console
- Auto-generate: Yoast SEO, RankMath, All in One SEO

### Canonical Tags
```html
<link rel="canonical" href="https://example.com/trang-chinh" />
```
- Tránh duplicate content từ params (?sort=, ?page=)
- Self-referencing canonical trên mọi trang

### Hreflang (đa ngôn ngữ)
```html
<link rel="alternate" hreflang="vi" href="https://example.com/vi/" />
<link rel="alternate" hreflang="en" href="https://example.com/en/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/" />
```

---

## Schema Markup (Structured Data)

### Quan trọng nhất cho BKNS
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Cloud VPS Intel",
  "description": "VPS hiệu suất cao...",
  "offers": {
    "@type": "Offer",
    "price": "89000",
    "priceCurrency": "VND",
    "availability": "InStock"
  }
}
```

### Các schema phổ biến
| Schema | Use case |
|---|---|
| `Organization` | Trang chủ công ty |
| `Product` | Trang sản phẩm/dịch vụ |
| `Article` | Blog post |
| `FAQPage` | Trang FAQ |
| `BreadcrumbList` | Breadcrumb navigation |
| `LocalBusiness` | SEO địa phương |
| `HowTo` | Hướng dẫn step-by-step |
| `Review` | Đánh giá |

### Validate: [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## Mobile-First Indexing
- Google dùng bản mobile để index — responsive design MANDATORY
- Test: Google Mobile-Friendly Test
- Font size ≥ 14px cho mobile, tap targets ≥ 48x48px
- Viewport meta: `<meta name="viewport" content="width=device-width, initial-scale=1">`

## HTTPS
- SSL certificate bắt buộc — Google xác nhận là ranking signal
- Mixed content (HTTP resources trên HTTPS page) → fix ngay
- HSTS header: `Strict-Transport-Security: max-age=31536000; includeSubDomains`

## Site Architecture
- Depth ≤ 3 clicks từ homepage đến bất kỳ trang nào
- Flat architecture > deep hierarchy
- Internal linking dạng silo/topic cluster
- Breadcrumb navigation

## Page Speed Optimization
1. Image: WebP/AVIF, lazy loading, srcset responsive
2. CSS: Critical CSS inline, defer non-critical
3. JS: Async/defer, code splitting, tree shaking
4. Server: HTTP/2 hoặc /3, Gzip/Brotli compression, CDN
5. Caching: Browser cache (Cache-Control), server cache (Varnish/Redis)

## JavaScript SEO
- SSR (Server-Side Rendering) hoặc SSG (Static Site Generation) tốt hơn CSR
- Dynamic rendering cho bot nếu cần (Rendertron)
- Đảm bảo Googlebot render được JS content
- Test: URL Inspection tool trong GSC → "View Tested Page"

## Tools
| Tool | Mục đích | Giá |
|---|---|---|
| Google PageSpeed Insights | Core Web Vitals test | Free |
| Google Lighthouse | Audit tổng hợp (SEO, Performance, a11y) | Free |
| Screaming Frog | Crawl site, tìm lỗi technical | Free ≤500 URLs |
| GTmetrix | Page speed analysis | Free |
| Ahrefs Site Audit | Technical SEO audit toàn diện | Paid |
| Google Search Console | Index, crawl stats, CWV | Free |
