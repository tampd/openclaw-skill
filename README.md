# 🦞 OpenClaw Skills & Knowledge

Bộ skills và knowledge base cho **OpenClaw** — trợ lý AI thông minh chạy trên VPS.

## 📋 Skills (11)

| # | Skill | Mô tả |
|---|---|---|
| 1 | **bkns-advisor** | Tư vấn dịch vụ BKNS: tra bảng giá, so sánh gói, đề xuất phù hợp |
| 2 | **blog-auditor** | Kiểm tra sức khỏe blog — SEO, bài trùng lặp |
| 3 | **budget-watcher** | Theo dõi token/chi phí Vertex AI, cảnh báo ngưỡng |
| 4 | **contract-writer** | Tạo hợp đồng từ template DOCX |
| 5 | **daily-reporter** | Báo cáo cuối ngày tự động |
| 6 | **file-organizer** | Quản lý, tìm kiếm, dọn dẹp file trên VPS |
| 7 | **seo-writer** | Viết bài SEO blog phong cách dev/coder |
| 8 | **smart-reminder** | Nhắc nhở, lịch hẹn, deadline bằng tiếng Việt |
| 9 | **vps-monitor** | Kiểm tra sức khỏe VPS (CPU, RAM, Disk) |
| 10 | **web-researcher** | Tìm kiếm, tóm tắt URL, research chủ đề |
| 11 | **wp-publisher** | Đăng bài lên WordPress qua REST API |

## 📚 Knowledge Base

| Folder | Nội dung |
|---|---|
| `knowledge/bkns/` | Bảng giá & thông tin BKNS.vn (VPS, Hosting, Domain, Email, Software) |

## 🗂️ Cấu Trúc

```
workspace/
├── skills/              # Các skill của OpenClaw
│   └── [skill-name]/
│       └── SKILL.md     # Hướng dẫn skill
├── knowledge/           # Knowledge base
│   └── bkns/            # Dữ liệu BKNS.vn
├── contracts/           # Hợp đồng mẫu
├── IDENTITY.md          # Nhân cách OpenClaw
├── SOUL.md              # Triết lý hoạt động
├── AGENTS.md            # Cấu hình agent
├── TOOLS.md             # Công cụ sẵn có
└── ...
```

## 🚀 Sử Dụng

Clone repo vào thư mục workspace của OpenClaw:
```bash
git clone git@github.com:tampd/openclaw-skill.git /root/openclaw/workspace
```

## 📝 Cập Nhật

Khi thêm/sửa skill hoặc knowledge:
```bash
cd /root/openclaw/workspace
git add -A
git commit -m "feat(skill-name): mô tả thay đổi"
git push
```
