# Posting Templates — Chaiko Tech Blog

> Template HTML cho từng loại bài. Copy template → fill content → đăng.

---

## Template 1: Bài Nghiên Cứu AI (Category 2)

```html
<p><strong>[Hook 1-2 câu hấp dẫn — đặt vấn đề, thống kê gây sốc, hoặc câu hỏi]</strong></p>

<p>[Đoạn mở đầu 2-3 câu — bối cảnh, tại sao topic này quan trọng ngay bây giờ]</p>

<h2>1. [Phần tổng quan — What/Why]</h2>
<p>[Giải thích concept chính, định nghĩa, nguồn gốc]</p>

<h2>2. [Phần phân tích sâu — How]</h2>
<p>[Chi tiết kỹ thuật, cơ chế hoạt động, architecture]</p>

<h3>[Sub-section nếu cần]</h3>
<p>[Chi tiết bổ sung]</p>

<h2>3. [Ứng dụng thực tế — Use Cases]</h2>
<p>[Ví dụ cụ thể, case study, demo]</p>
<ul>
  <li><strong>[Use case 1]:</strong> [Mô tả]</li>
  <li><strong>[Use case 2]:</strong> [Mô tả]</li>
  <li><strong>[Use case 3]:</strong> [Mô tả]</li>
</ul>

<h2>4. [Thách thức & Hạn chế]</h2>
<p>[Nhìn nhận đa chiều — limitations, risks, ethical concerns]</p>

<h2>Kết luận</h2>
<p>[Tổng kết 3-4 câu — key takeaway, call to action, tương lai]</p>

<h2>FAQ</h2>
<h3>[Câu hỏi phổ biến 1]?</h3>
<p>[Trả lời ngắn gọn, chính xác]</p>
<h3>[Câu hỏi phổ biến 2]?</h3>
<p>[Trả lời ngắn gọn, chính xác]</p>
```

**SEO settings**: slug format `[topic]-[keyword]-[year]`, excerpt 120-155 chars

---

## Template 2: Hướng Dẫn / Tutorial (Category 3)

```html
<p><strong>[Hook — kết quả reader sẽ đạt được sau khi đọc]</strong></p>

<p>[Bối cảnh — ai cần đọc, prerequisites, thời gian ước tính]</p>

<h2>Yêu cầu trước khi bắt đầu</h2>
<ul>
  <li>[Công cụ/phần mềm cần có]</li>
  <li>[Kiến thức nền tảng]</li>
  <li>[Tài khoản/quyền truy cập]</li>
</ul>

<h2>Bước 1: [Tên bước]</h2>
<p>[Giải thích bước này làm gì]</p>
<pre><code>[Code hoặc lệnh cần chạy]</code></pre>
<p>[Giải thích output expected]</p>

<h2>Bước 2: [Tên bước]</h2>
<p>[...]</p>

<h2>Bước 3: [Tên bước]</h2>
<p>[...]</p>

<h2>Xử lý lỗi thường gặp</h2>
<table>
  <thead><tr><th>Lỗi</th><th>Nguyên nhân</th><th>Cách fix</th></tr></thead>
  <tbody>
    <tr><td>[Lỗi 1]</td><td>[Nguyên nhân]</td><td>[Fix]</td></tr>
    <tr><td>[Lỗi 2]</td><td>[Nguyên nhân]</td><td>[Fix]</td></tr>
  </tbody>
</table>

<h2>Kết luận</h2>
<p>[Tóm tắt những gì đã làm + next steps]</p>
```

**SEO settings**: slug format `cach-[action]-[object]-[detail]`

---

## Template 3: Phân Tích / So Sánh (Category 4)

```html
<p><strong>[Hook — tình huống thực tế buộc phải lựa chọn]</strong></p>

<p>[Tổng quan 2-3 câu — tiêu chí so sánh, phạm vi]</p>

<h2>Tổng quan nhanh</h2>
<table>
  <thead><tr><th>Tiêu chí</th><th>[Sản phẩm A]</th><th>[Sản phẩm B]</th><th>[Sản phẩm C]</th></tr></thead>
  <tbody>
    <tr><td>Giá</td><td>[...]</td><td>[...]</td><td>[...]</td></tr>
    <tr><td>Tính năng chính</td><td>[...]</td><td>[...]</td><td>[...]</td></tr>
    <tr><td>Ưu điểm</td><td>[...]</td><td>[...]</td><td>[...]</td></tr>
    <tr><td>Nhược điểm</td><td>[...]</td><td>[...]</td><td>[...]</td></tr>
    <tr><td><strong>Verdict</strong></td><td>[...]</td><td>[...]</td><td>[...]</td></tr>
  </tbody>
</table>

<h2>[Sản phẩm A] — Phân tích chi tiết</h2>
<h3>Ưu điểm</h3>
<ul><li>[...]</li></ul>
<h3>Nhược điểm</h3>
<ul><li>[...]</li></ul>

<h2>[Sản phẩm B] — Phân tích chi tiết</h2>
<p>[...]</p>

<h2>Nên chọn gì?</h2>
<ul>
  <li><strong>Chọn [A] nếu:</strong> [use case]</li>
  <li><strong>Chọn [B] nếu:</strong> [use case]</li>
</ul>

<h2>Kết luận</h2>
<p>[Recommendation rõ ràng, không mập mờ]</p>
```

**SEO settings**: slug format `so-sanh-[a]-vs-[b]-[year]`

---

## Template 4: Bảo Mật (Category 5)

```html
<p><strong>⚠️ [Alert — mức độ nghiêm trọng, ai bị ảnh hưởng]</strong></p>

<p>[Bối cảnh — timeline, phát hiện khi nào, tác động]</p>

<h2>Tóm tắt mối đe dọa</h2>
<table>
  <thead><tr><th>Item</th><th>Chi tiết</th></tr></thead>
  <tbody>
    <tr><td>Tên</td><td>[CVE/Malware name]</td></tr>
    <tr><td>Mức độ</td><td>[Critical/High/Medium/Low]</td></tr>
    <tr><td>Ảnh hưởng</td><td>[Ai, hệ thống nào]</td></tr>
    <tr><td>Đã patch?</td><td>[Có/Chưa]</td></tr>
  </tbody>
</table>

<h2>Chi tiết kỹ thuật</h2>
<p>[Cơ chế tấn công, exploit chain]</p>

<h2>Cách phòng tránh</h2>
<ol>
  <li>[Bước 1 — immediate action]</li>
  <li>[Bước 2 — long-term fix]</li>
  <li>[Bước 3 — monitoring]</li>
</ol>

<h2>Kiểm tra hệ thống</h2>
<pre><code>[Lệnh kiểm tra]</code></pre>

<h2>Kết luận</h2>
<p>[Tóm tắt, khuyến nghị hành động ngay]</p>
```

---

## Template 5: Tin Nhanh / Tương Lai (Category 7)

```html
<p><strong>[TL;DR — 1 câu tóm tắt tin chính]</strong></p>

<p>[Bối cảnh 2-3 câu — nguồn tin, thời gian, ai liên quan]</p>

<h2>[Chuyện gì đang xảy ra?]</h2>
<p>[Facts, số liệu, quote từ nguồn chính thức]</p>

<h2>[Tại sao quan trọng?]</h2>
<p>[Phân tích tác động — với developer, doanh nghiệp, user]</p>

<h2>[Dự đoán tiếp theo]</h2>
<p>[Xu hướng, timeline dự kiến, kịch bản]</p>

<h2>Kết luận</h2>
<p>[Key takeaway + link nguồn gốc]</p>
```

---

## Ghi chú kỹ thuật

- **HTML output**: WordPress API nhận HTML trong field `content`
- **Không dùng Markdown** trong content — chuyển sang HTML trước khi đăng
- **Shortcodes**: không dùng — giữ HTML thuần
- **Code blocks**: dùng `<pre><code>...</code></pre>`, KHÔNG dùng triple backticks
- **Links**: `<a href="URL" target="_blank" rel="noopener">text</a>`
- **Images trong bài**: `<img src="URL" alt="Mô tả" width="800" />`
