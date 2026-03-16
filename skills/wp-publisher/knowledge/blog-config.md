# Blog Configuration — blog.chaiko.info

> File này chứa toàn bộ config live của blog. Đọc file này KHI cần biết category/tag/author.

## Thông tin cơ bản

| Key | Value |
|---|---|
| URL | https://blog.chaiko.info |
| Site Name | Chaiko Tech Blog |
| CMS | WordPress |
| SEO Plugin | Yoast SEO v27.0 |
| Locale | vi_VN |
| Author | Chaiko Team (user ID: 1, slug: admin) |
| Credentials | `/root/openclaw/workspace/wp_credentials.txt` |
| API Base | `https://blog.chaiko.info/wp-json/wp/v2` |

## Categories — Bảng Phân Loại

> ⚠️ KHI ĐĂNG BÀI, BẮT BUỘC chọn đúng category ID. KHÔNG đăng vào Uncategorized.

| ID | Name | Slug | Mô tả | Keyword triggers |
|---|---|---|---|---|
| 5 | Bảo mật | bao-mat | An ninh mạng và bảo mật | security, bảo mật, hack, malware, SSL, firewall, CVE |
| 6 | Công nghệ lõi | cong-nghe-loi | Phần cứng, hạ tầng và vi xử lý | chip, CPU, GPU, hardware, server, RAM, SSD, benchmark, phần cứng |
| 3 | Hướng dẫn | huong-dan | Tutorials và hướng dẫn lập trình | tutorial, hướng dẫn, cách làm, step-by-step, how-to, setup |
| 2 | Nghiên cứu AI | nghien-cuu-ai | Bài viết nghiên cứu chuyên sâu về AI | AI, machine learning, LLM, GPT, Claude, Gemini, deep learning, nghiên cứu |
| 4 | Phân tích | phan-tich | Phân tích xu hướng công nghệ | phân tích, so sánh, trend, xu hướng, đánh giá, review, comparison |
| 7 | Tương lai | tuong-lai | Metaverse, VR/AR và công nghệ tương lai | metaverse, VR, AR, future, tương lai, quantum, AGI, dự đoán |
| 1 | Uncategorized | uncategorized | (default — KHÔNG DÙNG) | — |

### Quy tắc chọn category
1. Phân tích tiêu đề + nội dung → match keyword triggers ở trên
2. Nếu bài về AI + tutorial → ưu tiên **Hướng dẫn** (3) thay vì Nghiên cứu AI
3. Nếu bài so sánh sản phẩm → **Phân tích** (4)
4. Nếu bài về bảo mật + hướng dẫn → **Bảo mật** (5)
5. Có thể gán **nhiều categories** nếu bài cross-topic

## Tags — Nhãn

| ID | Name | Slug |
|---|---|---|
| 12 | AI Coding | ai-coding |
| 9 | Clean-room AI | clean-room-ai |
| 10 | Open Source | open-source |
| 11 | Supply Chain Security | supply-chain-security |

### Quy tắc tag
- Tags được tạo **tự do** (không giới hạn danh sách trên)
- Nên tạo tag mới cho mỗi chừng 3-5 bài cùng chủ đề
- **Format**: tiếng Anh, lowercase, dấu gạch ngang (e.g. `ai-agents`, `vps-hosting`)
- **Tối đa 5 tags/bài**

## Bài viết gần nhất (reference)

| ID | Ngày | Tiêu đề | Category |
|---|---|---|---|
| 140 | 2026-03-14 | MCP là gì? Vì sao 2026 là năm bùng nổ AI coding agents | Uncategorized |
| 139 | 2026-03-13 | Clean-room AI đang đe dọa Open Source? | Phân tích |
| 133 | 2026-03-12 | AI Workers và Multimodal AI 2026 | Uncategorized |
| 131 | 2026-03-11 | Agentic AI 2026: Tự Động Hóa Quy Trình Phần Mềm | Uncategorized |
| 123 | 2026-03-08 | Cách Nhận Google Gemini Pro Miễn Phí 4 Tháng | Hướng dẫn |

> ⚠️ Nhiều bài đang ở Uncategorized → cần re-categorize khi audit.
