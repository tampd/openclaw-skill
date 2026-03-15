# Blog SEO Autopilot — blog.chaiko.info

## Mục tiêu
Tự nghiên cứu trend mới nhất, viết bài chuẩn SEO cho blog.chaiko.info, dùng keyword ngắn để slug gọn, kèm ít nhất 3 ảnh không bản quyền lấy từ internet, rồi đăng đúng lịch.

## Kênh liên kết thương hiệu
- Blog chính: https://blog.chaiko.info
- Fanpage social: https://www.facebook.com/1012410591957125
- Khi phù hợp, cuối bài thêm CTA ngắn: `Theo dõi Tý Tech trên Facebook để xem bản rút gọn và update nhanh mỗi ngày.`

## Quy tắc bắt buộc
1. Bài viết bằng tiếng Việt, chuẩn SEO, không copy nguyên văn.
2. Chọn **focus keyword ngắn**: 2-4 từ là ưu tiên.
3. **Slug tối đa 5 từ**, không nhồi nhét năm nếu không cần.
4. Dùng **ít nhất 3 ảnh** cho mỗi bài:
   - 1 ảnh featured/hero
   - 2 ảnh minh họa trong bài
5. Ảnh phải là ảnh **không bản quyền / giấy phép mở / dùng lại được**, ưu tiên:
   - Openverse
   - Wikimedia Commons
   - Unsplash
   - Pexels
6. Không dùng ảnh watermark, ảnh mờ, ảnh stock generic quá tệ.
7. Ảnh có thể **crop/resize**, nhưng **không thiết kế mới**.
8. Mỗi ảnh phải có:
   - alt text tiếng Việt mô tả đúng nội dung
   - filename gọn theo slug
9. Mỗi bài phải có tối thiểu:
   - meta description
   - 3 internal links
   - 1 external source uy tín
   - 1 đoạn FAQ ngắn hoặc block Q&A
10. Tránh trùng lặp với bài đã có trên blog.

## Lịch nội dung
- **Thứ 2 — 09:00 GMT+7**: Trend / Nghiên cứu AI / tin công nghệ đang nóng
- **Thứ 4 — 09:00 GMT+7**: Hướng dẫn / how-to / workflow thực hành
- **Thứ 6 — 09:00 GMT+7**: Phân tích / bảo mật / so sánh / góc nhìn chiến lược

## Quy trình mỗi lần chạy
### Bước 1 — Research trend
Nguồn ưu tiên:
- Hacker News
- GitHub Trending / GitHub Search
- TechCrunch / The Verge / Ars Technica
- OpenAI / Google AI / Anthropic blogs
- Reddit kỹ thuật nếu cần

Chọn chủ đề theo tiêu chí:
- Phù hợp audience developer / DevOps / AI / automation
- Có nhu cầu tìm kiếm hoặc có sức hút trend
- Chưa có bài tương tự hoặc quá gần trên blog
- Có thể rút ra keyword ngắn, ví dụ:
  - `mcp`
  - `ai worker`
  - `prompt injection`
  - `vibe coding`
  - `rag`

### Bước 2 — Kiểm tra trùng lặp
- Gọi WordPress REST API search theo keyword và title gần đúng.
- Nếu đã có bài tương tự gần đây, bỏ qua và chọn chủ đề khác.

### Bước 3 — Viết bài
Yêu cầu:
- 1200-2200 từ
- cấu trúc rõ: H1, intro, H2/H3, kết luận, FAQ ngắn
- keyword xuất hiện tự nhiên
- tone: kỹ thuật, thực tế, dễ đọc
- không viết title/slug dài lê thê

### Bước 4 — Ảnh không bản quyền
- Tìm ít nhất 3 ảnh phù hợp chủ đề từ Openverse/Wikimedia/Unsplash/Pexels.
- Download về local tạm thời.
- Crop/resize bằng script/Python nếu cần.
- Featured image ưu tiên 1200x630.
- Ảnh trong bài có thể 1200x630 hoặc 1280x720.
- Ghi source credit cuối bài nếu nguồn yêu cầu/ phù hợp.

### Bước 5 — Upload WordPress
- Upload cả 3 ảnh vào WordPress media.
- Set 1 ảnh làm featured image.
- Chèn 2 ảnh còn lại vào nội dung bài.

### Bước 6 — Internal linking
Mỗi bài cần chèn tối thiểu 3 internal links tới bài liên quan hoặc trang trụ cột:
- https://blog.chaiko.info/posts
- https://blog.chaiko.info/tools
- https://blog.chaiko.info/roadmap
- hoặc các bài WordPress liên quan cùng chủ đề

### Bước 7 — Publish
- Bài cron chạy đúng giờ thì có thể publish luôn.
- Nếu thiếu ảnh hợp lệ hoặc không tìm được nguồn tốt, **không publish**; tạo draft hoặc bỏ qua và báo cáo rõ lý do.

### Bước 8 — Log
Ghi log vào:
- `memory/blog-seo-automation.md`
Mỗi entry gồm:
- thời gian
- chủ đề
- keyword
- slug
- 3 nguồn ảnh
- URL bài viết
- trạng thái publish/draft/skip

## Mapping category
- Trend / AI mới → `Nghiên cứu AI (2)` hoặc `Phân tích (4)`
- Hướng dẫn → `Hướng dẫn (3)`
- Security → `Bảo mật (5)`
- Hạ tầng / phần cứng → `Công nghệ lõi (6)`
- Dự báo dài hạn → `Tương lai (7)`

## Output tối thiểu sau mỗi lần chạy
1. Chủ đề đã chọn
2. Keyword + slug
3. 3 nguồn ảnh đã dùng
4. URL bài viết hoặc lý do skip
