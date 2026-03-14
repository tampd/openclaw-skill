# BKNS SEO Article Template

> Template chuẩn bài viết SEO theo phong cách BKNS.
> Sử dụng khi Tôm nhận lệnh `/seo-bkns [chủ đề]`.

---

## HTML Skeleton

```html
<!-- META -->
<title>[Keyword chính] — [Giá trị/Benefit] [Năm hiện tại]</title>
<meta name="description" content="[150-160 chars: keyword + lợi ích + CTA ẩn]" />

<!-- ARTICLE START -->
<article>

  <!-- H1: Title -->
  <h1>[Keyword chính]? [Giải pháp / Hướng dẫn] [cụm từ hấp dẫn] [năm hiện tại]</h1>

  <!-- HERO IMAGE — Ngay sau H1 -->
  <figure>
    <img src="[hero-image-url]" alt="[keyword chính] — [mô tả ngắn]" width="1200" height="628" />
    <figcaption>[Caption ngắn liên quan keyword]</figcaption>
  </figure>

  <!-- INTRO: 80-120 từ -->
  <p>[Keyword chính] giúp [đối tượng] [giải quyết vấn đề gì]. [2-3 câu giải thích ngắn].
  Khám phá [nội dung bài viết] trong bài viết chi tiết dưới đây của [thương hiệu].</p>

  <!-- TABLE OF CONTENTS -->
  <div class="toc">
    <strong>Mục lục</strong>
    <ul>
      <li><a href="#section-1">[H2 đầu tiên]</a></li>
      <li><a href="#section-2">[H2 thứ hai]</a>
        <ul>
          <li><a href="#sub-2-1">[H3 con]</a></li>
          <li><a href="#sub-2-2">[H3 con]</a></li>
        </ul>
      </li>
      <!-- ... 6-10 H2 sections ... -->
      <li><a href="#faq">Câu hỏi thường gặp (FAQ)</a></li>
    </ul>
  </div>

  <!-- === SECTION 1: Khái niệm === -->
  <h2 id="section-1">[Keyword chính] là gì?</h2>
  <!-- 🖼️ IMAGE: Infographic hoặc sơ đồ giải thích khái niệm -->
  <figure>
    <img src="[image-url]" alt="[keyword] là gì — sơ đồ giải thích" />
  </figure>
  <p>[200-300 từ giải thích khái niệm, cơ chế hoạt động]</p>

  <!-- === SECTION 2: Phù hợp cho ai / Vì sao cần === -->
  <h2 id="section-2">[Keyword] phù hợp cho những ai? / Vì sao cần [keyword]?</h2>
  <!-- 🖼️ IMAGE: Icon illustration các nhóm đối tượng -->
  <ul>
    <li><strong>[Nhóm 1]:</strong> [Giải thích 1-2 câu]</li>
    <li><strong>[Nhóm 2]:</strong> [Giải thích 1-2 câu]</li>
    <li><strong>[Nhóm 3]:</strong> [Giải thích 1-2 câu]</li>
    <!-- 5-7 items -->
  </ul>

  <!-- === SECTION 3: Nguyên tắc hoạt động / Cơ chế === -->
  <h2 id="section-3">Nguyên tắc hoạt động / Cách thức [keyword]</h2>
  <!-- 🖼️ IMAGE: Sơ đồ flow hoạt động -->
  <ul>
    <li><strong>[Bước/Yếu tố 1]:</strong> [Giải thích chi tiết]</li>
    <li><strong>[Bước/Yếu tố 2]:</strong> [Giải thích chi tiết]</li>
  </ul>

  <!-- === SECTION 4: Lợi ích / Tại sao chọn === -->
  <h2 id="section-4">Tại sao nên [hành động keyword] thay vì [alternative]?</h2>
  <h3 id="sub-4-1">[Lợi ích 1: Cụ thể, bold]</h3>
  <!-- 🖼️ IMAGE: comparison diagram -->
  <p>[150-200 từ giải thích với số liệu cụ thể]</p>
  <h3 id="sub-4-2">[Lợi ích 2]</h3>
  <p>[150-200 từ]</p>

  <!-- === SECTION 5: Phân loại === -->
  <h2 id="section-5">Phân loại [keyword]</h2>
  <!-- 🖼️ IMAGE: Bảng phân loại hoặc icons -->
  <h3>[Loại 1]</h3>
  <ul>
    <li>[Đặc điểm]</li>
    <li>[Phù hợp cho...]</li>
  </ul>
  <h3>[Loại 2]</h3>
  <h3>[Loại 3]</h3>

  <!-- === SECTION 6: Tiêu chí chọn === -->
  <h2 id="section-6">Tiêu chí chọn [keyword] tốt nhất</h2>
  <!-- 🖼️ IMAGE: Checklist infographic -->
  <ul>
    <li><strong>[Tiêu chí 1]:</strong> [Giải thích + gợi ý cụ thể]</li>
    <li><strong>[Tiêu chí 2]:</strong> [Giải thích + số liệu]</li>
    <!-- 6-9 tiêu chí -->
  </ul>

  <!-- === SECTION 7: Bảng so sánh === -->
  <h2 id="section-7">Bảng so sánh [Option A] và [Option B]</h2>
  <!-- 🖼️ IMAGE: Table comparison graphic hoặc dùng HTML table -->
  <table>
    <thead>
      <tr><th>Tiêu chí</th><th>[Option A]</th><th>[Option B]</th></tr>
    </thead>
    <tbody>
      <tr><td>Chi phí</td><td>[...]</td><td>[...]</td></tr>
      <tr><td>Hiệu suất</td><td>[...]</td><td>[...]</td></tr>
      <tr><td>Độ ổn định</td><td>[...]</td><td>[...]</td></tr>
      <!-- 5-8 rows -->
    </tbody>
  </table>

  <!-- === SECTION 8: Bảng giá (nếu có) === -->
  <h2 id="section-8">Bảng giá [keyword] — Cập nhật mới nhất [năm]</h2>
  <!-- ĐỌC DỮ LIỆU TỪ bkns-advisor knowledge files -->
  <table>
    <thead>
      <tr><th>Gói</th><th>Cấu hình</th><th>Giá/tháng</th></tr>
    </thead>
    <tbody>
      <tr><td>[...]</td><td>[...]</td><td>[...]</td></tr>
    </tbody>
  </table>
  <p><em>*Bảng giá chỉ mang tính tham khảo. Liên hệ hotline: <a href="tel:1800646884">1800 646 884</a> để nhận báo giá chính xác.</em></p>

  <!-- === SECTION 9: Lưu ý quan trọng === -->
  <h2 id="section-9">Một số lưu ý quan trọng khi [hành động]</h2>
  <!-- 🖼️ IMAGE: Warning/tips infographic -->
  <ul>
    <li>[Lưu ý 1 — cụ thể, actionable]</li>
    <li>[Lưu ý 2]</li>
    <li>[Lưu ý 3]</li>
  </ul>

  <!-- === SECTION 10: CTA + Giới thiệu BKNS === -->
  <h2 id="section-10">[Hành động] ở đâu tốt nhất?</h2>
  <!-- 🖼️ IMAGE: Logo BKNS + datacenter -->
  <p>[Giới thiệu BKNS 150-200 từ: ưu điểm, hạ tầng, support]</p>
  <ul>
    <li><strong>Giá cạnh tranh:</strong> [...]</li>
    <li><strong>Hạ tầng Tier III:</strong> [...]</li>
    <li><strong>Hỗ trợ 24/7:</strong> [...]</li>
  </ul>
  <p><strong>Đăng ký ngay <a href="https://www.bkns.vn/">[dịch vụ]</a> tại BKNS!</strong></p>

  <!-- === CONCLUSION === -->
  <p>[Tóm tắt 100-150 từ: keyword chính, lợi ích chính, khuyến khích hành động]</p>

  <!-- === FAQ === -->
  <h2 id="faq">Câu hỏi thường gặp (FAQ)</h2>
  <!-- Schema FAQ markup -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "[Câu hỏi 1]?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "[Trả lời trực tiếp, 2-4 câu]"
        }
      }
    ]
  }
  </script>
  <h3>[Câu hỏi 1]?</h3>
  <p>[Trả lời trực tiếp]</p>
  <h3>[Câu hỏi 2]?</h3>
  <p>[Trả lời]</p>
  <h3>[Câu hỏi 3]?</h3>
  <p>[Trả lời]</p>

  <!-- === RELATED POSTS === -->
  <div class="related-posts">
    <h3>Bài viết liên quan</h3>
    <ul>
      <li><a href="[url]">[Title bài 1]</a></li>
      <li><a href="[url]">[Title bài 2]</a></li>
      <li><a href="[url]">[Title bài 3]</a></li>
    </ul>
  </div>

</article>
```

---

## Quy tắc số liệu

| Metric | Target |
|---|---|
| Tổng từ | 2500–3500 từ |
| Số H2 | 8–12 headings |
| Số H3 | 2–4 per H2 (nếu cần) |
| Số ảnh | ≥8 (mỗi H2 ≥ 1) |
| Số bảng | ≥1 (comparison hoặc pricing) |
| Bullet lists | ≥5 lists |
| Internal links | 3–5 links |
| External links | 1–2 authoritative |
| FAQ items | 3–5 câu hỏi |
