---
name: wp-publisher
description: A skill to automatically format and publish articles to a WordPress blog (like blog.chaiko.info) via the WordPress REST API.
---

# WordPress Publisher Skill

## Giới thiệu
Bạn là cổng giao tiếp giữa OpenClaw và hệ thống WordPress của trang web `blog.chaiko.info`. Nhiệm vụ của bạn là lấy nội dung đã được viết sẵn (từ Agent `seo-writer` hoặc từ người dùng) và đưa nó lên website một cách chuyên nghiệp.

## Luồng Xử Lý (Publishing Workflow)

Khi được yêu cầu đăng bài, thực hiện các bước sau:

### 0. Kiểm tra trùng lặp (BẮT BUỘC)
```bash
# Kiểm tra blog đã có bài cùng tiêu đề chưa
TITLE="Tiêu đề bài viết"
curl -s "https://blog.chaiko.info/wp-json/wp/v2/posts?search=$(echo "$TITLE" | head -c 50 | sed 's/ /+/g')&_fields=id,title,status" \
  | python3 -c "
import json, sys
posts = json.load(sys.stdin)
dupes = [p for p in posts if p['title']['rendered'].strip().lower() == sys.argv[1].strip().lower()]
if dupes:
    print('⚠️ BÀI TRÙNG! Không đăng.')
    for d in dupes: print(f\"  ID:{d['id']} | {d['title']['rendered']}\")
else:
    print('✅ Không trùng, an toàn để đăng')
" "$TITLE"
```
> ⚠️ Nếu phát hiện bài trùng → **DỪNG LẠI** và thông báo Admin. KHÔNG đăng thêm bài trùng.

1. **Chuẩn bị Dữ liệu (Payload Prep):**
   - Trích xuất tiêu đề (Title) từ nội dung bài viết.
   - Trích xuất Nội dung chính (Content) dưới dạng HTML (chuyển đổi Markdown sang HTML cơ bản nếu cần).
   - Xác định Trạng thái (Status): Mặc định đăng dưới dạng `draft` (Bản nháp), trừ khi Admin yêu cầu `publish` (Đăng công khai luôn).

2. **Gửi API Request:**
   - Bạn BẮT BUỘC phải gọi lệnh `curl` gửi HTTP POST request ĐÚNG ĐẾN ENDPOINT NÀY: `https://blog.chaiko.info/wp-json/wp/v2/posts`. KHÔNG ĐƯỢC DÙNG endpoint nào khác (như `/newpost` hay `/wp-admin`).
   - Cần cấu hình Header Authorization chứa **Application Password** của WordPress. 
   - Mật khẩu WordPress (Application Password) đã được lưu sẵn trong hệ thống của bạn tại file: `/root/openclaw/workspace/wp_credentials.txt`. Hãy dùng công cụ lệnh shell (ví dụ `cat /root/openclaw/workspace/wp_credentials.txt`) để đọc file này lấy password, KHÔNG CẦN CHỜ NGƯỜI DÙNG CUNG CẤP trong khung chat.

3. **Cấu trúc cURL (Ví dụ):**
   ```bash
   curl -X POST "https://blog.chaiko.info/wp-json/wp/v2/posts" \
        -u "admin:application_password" \
        -H "Content-Type: application/json" \
        -d '{
              "title": "Tiêu đề bài viết",
              "content": "<p>Nội dung HTML ở đây</p>",
              "status": "draft"
            }'
   ```

4. **Kiểm tra và Báo cáo:**
   - Dựa trên kết quả trả về của lệnh `curl`, phân tích tín hiệu JSON (HTTP 201 Created).
   - Nếu đăng thành công, gửi đường dẫn chỉnh sửa bài viết (Edit Link) hoặc link preview cho người dùng trên Telegram.
   - Nếu thất bại → xem mục Error Recovery bên dưới.

## Error Recovery (Xử lý lỗi)

| HTTP Code | Nguyên nhân | Xử lý |
|-----------|-------------|-------|
| 401 | Sai credentials | Đọc lại file `wp_credentials.txt`, thử lại 1 lần |
| 403 | Không có quyền | Báo Admin kiểm tra user permissions |
| 500 | Server lỗi | Chờ 30 giây, thử lại tối đa 2 lần |
| Timeout | Mạng chậm | Thử lại với `--connect-timeout 30` |

**Quy tắc retry**: Tối đa 2 lần retry. Nếu vẫn thất bại → báo lỗi chi tiết cho Admin.

## Lưu ý về Bảo mật
**CẢNH BÁO QUAN TRỌNG:** KHÔNG BAO GIỜ hiển thị Application Password của WordPress dưới dạng plain text trong khung chat. Chỉ đọc từ file môi trường hoặc yêu cầu user cung cấp riêng biệt và xóa log lệnh curl.
