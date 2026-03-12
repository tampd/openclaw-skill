import requests
import json
import base64

# Thông tin tài khoản và mật khẩu (thay bằng username và application password)
USERNAME = "admin"
PASSWORD = "tRy5 Bx9U 3sHl 92A7 ayNs ZxfH"

# Đường dẫn API của WordPress
API_ENDPOINT = "https://blog.chaiko.info/wp-json/wp/v2/posts"

# Hàm để tạo header xác thực cơ bản
def get_basic_auth_header(username, password):
    token = base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')
    return f'Basic {token}'

# Hàm để đăng bài viết
def create_wordpress_post(title, content):
    headers = {
        'Authorization': get_basic_auth_header(USERNAME, PASSWORD),
        'Content-Type': 'application/json',
    }
    data = {
        'title': title,
        'content': content,
        'status': 'publish',  # Để đăng bài viết, thay đổi thành 'draft' để lưu черновик
    }
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data, ensure_ascii=False).encode('utf-8'))
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f'Không thể đăng bài viết: {response.status_code} - {response.text}')

# Đọc nội dung từ file Markdown
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

# Tách tiêu đề và nội dung từ Markdown (giả định tiêu đề là dòng đầu tiên)
def split_title_content(markdown_content):
    lines = markdown_content.split('\n', 1)
    title = lines[0].replace('# ', '')  # Loại bỏ dấu # và khoảng trắng
    content = lines[1] if len(lines) > 1 else ''
    return title, content

# Main function
def main():
    try:
        # Đọc nội dung từ file Markdown
        markdown_content = read_markdown_file('agentic_ai_2026.md')

        # Tách tiêu đề và nội dung
        title, content = split_title_content(markdown_content)

        # Tạo bài viết WordPress
        post = create_wordpress_post(title, content)
        print(f'Đăng bài viết thành công! ID: {post['id']}, Link: {post['link']}')

    except Exception as e:
        print(f'Lỗi: {e}')

if __name__ == '__main__':
    main()
