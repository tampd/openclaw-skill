# Audit blog.chaiko.info — cấu trúc liên kết & đồng bộ hình ảnh

Ngày audit: 2026-03-15 02:57 UTC

## 1) Kết luận nhanh

blog.chaiko.info đang có front-end riêng (Next.js) chạy phía trước WordPress API.

Điểm mạnh:
- UI hiện đại, tông màu teal/violet/cyan rõ cá tính
- SEO meta cơ bản có đủ ở các trang chính
- Có các trang trụ cột tốt để làm internal linking: `/posts`, `/tools`, `/roadmap`, `/about`

Điểm yếu lớn:
- Footer/legal đang có nhiều link chết (404)
- Một link category trong menu bị 404
- Core pages chưa có `og:image` / `twitter:image`
- Bộ ảnh bài viết chưa thống nhất tỉ lệ và phong cách
- 3 bài WordPress vẫn nằm `Uncategorized`, làm yếu phân loại và liên kết theo chủ đề
- Fanpage Tý Tech và blog Chaiko Blog chưa có cầu nối nhận diện rõ ràng

---

## 2) Bằng chứng kỹ thuật

### Route status
- `/` → 200
- `/posts` → 200
- `/about` → 200
- `/roadmap` → 200
- `/tools` → 200
- `/bookmarks` → 200
- `/privacy` → 404
- `/terms` → 404
- `/cookies` → 404
- `/guidelines` → 404
- `/categories/tutorials` → 404

### Metadata
Các route chính có `title` + `description`, nhưng chưa có `og:image` / `twitter:image`:
- `/`
- `/posts`
- `/about`
- `/roadmap`
- `/tools`
- `/bookmarks`

### WordPress content structure
- WordPress có posts + categories + tags bình thường
- WordPress API trả về `pages = []`
- Suy ra các route public như `/about`, `/roadmap`, `/tools` nhiều khả năng là page tĩnh ở front-end, không phải WP page

### Ảnh bài viết đang dùng
- `ai-workers-2026-cover.png` → 1280x720
- `featured-1.png` → 640x640
- `gemini-featured.png` → 640x640
- `mcp-hero.jpg` → 1200x630

=> Tỉ lệ đang lẫn giữa **16:9**, **1:1**, và **1.91:1**

---

## 3) Vấn đề liên kết nội bộ

### A. Link chết cần sửa ngay
1. Footer pháp lý đang trỏ tới 4 route 404:
   - `/privacy`
   - `/terms`
   - `/cookies`
   - `/guidelines`
2. Menu đang có link `/categories/tutorials` nhưng route này 404

### B. Liên kết nội dung chưa thành hệ thống
Hiện blog có nội dung tốt, nhưng chưa thấy cấu trúc nối rõ giữa:
- bài nền tảng
- bài hướng dẫn
- bài phân tích
- trang roadmap
- trang tools

### C. Category mapping còn thủng
Ba bài mới vẫn ở `Uncategorized`:
- ID 140 — MCP là gì? Vì sao 2026 là năm bùng nổ AI coding agents
- ID 133 — AI Workers và Multimodal AI 2026
- ID 131 — Agentic AI 2026

Điều này làm yếu:
- trang category
- bài liên quan theo chủ đề
- breadcrumb / cluster logic

---

## 4) Đề xuất internal linking

## Tầng 1 — Trang trụ cột
### Trang chủ
Nên đẩy rõ 3 cổng vào chính:
- `Bắt đầu học AI` → `/roadmap`
- `Khám phá tất cả bài viết` → `/posts`
- `So sánh công cụ AI` → `/tools`

### Roadmap
Mỗi roadmap nên gắn bài đọc theo chặng.

Ví dụ cụm hợp lý:
- **AI Fundamentals**
  - `RAG là gì?`
  - `Tối ưu hóa Vector Database`
  - `Hướng dẫn xây dựng AI Agent từ A-Z với LangChain`
- **AI Security**
  - `Tấn công Prompt Injection là gì?`
  - `Zero-Trust Architecture cho AI`
  - `Clean-room AI đang đe dọa Open Source?`
- **AI Trends / Strategy**
  - `Agentic AI 2026`
  - `AI Workers và Multimodal AI 2026`
  - `MCP là gì?`

### Tools
Trang tools nên link ra 3 loại đích:
- bài review sâu từng tool
- bài hướng dẫn dùng tool trong workflow thực tế
- bài so sánh tool theo use case

Ví dụ:
- `Gemini` → bài “Cách nhận Google Gemini Pro miễn phí 4 tháng”
- `AI coding tools` → bài `MCP là gì?` + các bài agentic AI

### About
Nên có CTA kép:
- `Xem lộ trình học AI` → `/roadmap`
- `Đọc bài mới nhất` → `/posts`

### Mỗi bài viết
Nên có block cuối bài gồm:
- `Đọc tiếp cùng chủ đề`
- `Bắt đầu từ lộ trình phù hợp` → `/roadmap`
- `Khám phá công cụ liên quan` → `/tools`

---

## 5) Đề xuất đồng bộ hình ảnh

## Thực trạng nhận diện hiện tại
### Blog
- Brand hiện tại: **Chaiko Blog**
- Biểu tượng: `neurology`
- Tông UI: teal `#0D9488`, amber `#F59E0B`, violet/cyan gradient, kiểu glassmorphism

### Fanpage
- Brand hiện tại: **Tý Tech**
- Nhận diện: mascot/owner artwork neon, gần gũi, trẻ hơn, đậm social hơn

### Nhận xét
Hai bên **chưa cùng một hệ nhận diện**.
Không hẳn sai, nhưng khi fanpage link sang blog sẽ có cảm giác:
- người dùng đang từ brand A sang brand B
- thiếu câu chuyện “Tý Tech thuộc Chaiko” hay “Tý Tech là social face của Chaiko”

## Hướng đồng bộ hợp lý nhất
### Option khuyến nghị: kiến trúc thương hiệu mẹ - con
- **Blog** giữ tên: `Chaiko Blog`
- **Fanpage** giữ tên: `Tý Tech`
- Thêm cầu nối rõ: `Tý Tech by Chaiko` hoặc `Tý Tech • powered by Chaiko Blog`

### Cần đồng bộ 5 thứ
1. **Màu chủ đạo**
   - Giữ teal/cyan/violet làm xương sống cho cả blog và fanpage
   - Dùng amber làm màu CTA phụ, không để fanpage đi sang palette khác
2. **Kiểu ảnh featured image**
   - Chốt 1 chuẩn chính: **1200x630** cho blog/social share
   - Có thể render thêm bản 1080x1080 cho fanpage, nhưng source design nên cùng template
3. **Typography cảm giác**
   - Blog đang nghiêng nghiêm túc, tech, sạch
   - Fanpage đang thân thiện, vui hơn
   - Cần 1 lớp chung: headline mạnh, neon accent, icon/circuit pattern nhẹ
4. **Logo/brand bridge**
   - Trên blog nên thêm mention nhỏ ở footer/about: `Tý Tech là social channel của Chaiko Blog`
   - Trên fanpage bio nên giữ website blog.chaiko.info và mô tả là kênh nội dung của hệ Chaiko
5. **OG/social preview images**
   - Tạo default social cover cho homepage, posts page, roadmap, tools, about
   - Cùng phong cách với featured images bài viết

## Chuẩn hình ảnh nên dùng
### Bộ chuẩn đề xuất
- **Homepage / landing OG**: 1200x630
- **Post featured**: 1200x630
- **Social square variant**: 1080x1080
- **Author/about/team images**: 4:5 hoặc 1:1
- **Roadmap cards / tool cards**: dùng cùng icon style + cùng gradient nền

### Template hình ảnh thống nhất
Mỗi ảnh nên có:
- nền dark tech + gradient teal/violet
- 1 vùng title lớn, dễ đọc trên mobile
- 1 nhãn nhỏ category (AI / Hướng dẫn / Phân tích / Bảo mật / Tương lai)
- 1 chi tiết nhận diện cố định: icon, line circuit, hoặc badge Chaiko/Tý Tech

---

## 6) Thứ tự ưu tiên xử lý

### Ưu tiên 1 — sửa lỗi cấu trúc
1. Tạo hoặc bỏ 4 link pháp lý đang 404
2. Sửa link `/categories/tutorials` thành route đúng
3. Re-categorize 3 bài `Uncategorized`

### Ưu tiên 2 — tăng khả năng link qua lại
4. Thêm block “bài liên quan / đọc tiếp” ở cuối post
5. Gắn CTA từ `/about`, `/tools`, `/roadmap` sang `/posts`
6. Gắn CTA ngược từ bài viết sang `/roadmap` hoặc `/tools`

### Ưu tiên 3 — đồng bộ nhận diện hình ảnh
7. Chốt 1 template featured image chuẩn 1200x630
8. Tạo default OG images cho các trang chính
9. Thêm cầu nối nhận diện giữa Tý Tech và Chaiko Blog

---

## 7) Kết luận ngắn

Blog có nền tảng tốt, nhưng đang thiếu 3 thứ để thành một hệ thống chặt:
- **link nội bộ có chủ đích**
- **ảnh nhận diện đồng bộ**
- **cầu nối thương hiệu giữa Chaiko Blog và Tý Tech**

Nếu triển khai đúng, fanpage sẽ không chỉ kéo traffic về blog, mà còn kéo người dùng đi tiếp giữa `roadmap` → `posts` → `tools` thay vì đọc xong rồi thoát.
