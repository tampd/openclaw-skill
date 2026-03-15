# Audit liên kết Chaiko Blog ↔ Tý Tech

Ngày: 2026-03-15 UTC

## Kết quả kiểm tra thực tế

### 1) Fanpage → Blog
- Fanpage `Tý Tech` đang trỏ website đúng về `https://blog.chaiko.info/`
- `about` và `description` đã đúng định vị AI / DevOps / automation / IT

### 2) Blog → Fanpage
- Đã xác nhận các bài blog sau có link đúng về fanpage Tý Tech:
  - `/mcp-la-gi-ai-coding-agents-2026/`
  - `/clean-room-ai-maluse-open-source-dev-2026/`
  - `/ai-workers-multimodal-ai-2026-doanh-nghiep/`
- Link fanpage dùng URL chuẩn: `https://www.facebook.com/1012410591957125`

## Lỗi còn tồn tại
- Homepage public của `blog.chaiko.info` vẫn hard-code link Facebook cũ:
  - `https://facebook.com/chaikoblog`
- Frontend public là Next.js đứng trước WordPress, không phải giao diện WP thuần.
- Trong môi trường hiện tại chưa thấy repo/source hoặc host config của frontend này để sửa trực tiếp từ VPS/workspace.

## Đánh giá
- Liên kết 2 chiều ở mức nội dung đã hoạt động.
- Liên kết 2 chiều ở mức nhận diện thương hiệu toàn site vẫn CHƯA sạch do footer homepage còn trỏ link cũ.

## Việc đã làm
- Update post ID 139 để thêm CTA về fanpage Tý Tech
- Update post ID 133 để thêm CTA về fanpage Tý Tech
- Verify lại qua WordPress REST API

## Đề xuất bước tiếp theo
1. Sửa frontend footer/header/about của blog để thay `facebook.com/chaikoblog` → `https://www.facebook.com/1012410591957125`
2. Thêm câu bridge brand ở blog:
   - `Tý Tech là kênh social update nhanh của Chaiko Blog`
3. Thêm block cố định ở homepage hoặc about:
   - `Theo dõi Tý Tech để nhận bản ngắn hằng ngày`
4. Chuẩn hoá CTA cuối mọi bài mới:
   - Blog dài → kéo sang fanpage
   - Fanpage ngắn → kéo về blog đọc full

## Khuyến nghị chiến lược vận hành chung
- Blog = long-form SEO + tài sản tìm kiếm lâu dài
- Tý Tech = reach nhanh + tương tác + test hook/content angle
- Mỗi bài blog nên sinh ra ít nhất:
  - 1 post fanpage teaser
  - 1 comment ghim CTA
  - 1 follow-up post rút insight 24-48h sau
