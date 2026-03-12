---
name: contract-writer
description: Tạo hợp đồng BKNS từ template DOCX gốc. Thay thế thông tin khách hàng trực tiếp vào file, giữ nguyên format.
---

# Contract Writer — Soạn Hợp Đồng BKNS

## Mục đích
Giúp Sếp tạo hợp đồng nhanh bằng cách lấy file mẫu DOCX gốc của BKNS → thay thế thông tin khách hàng → xuất file mới.

**QUAN TRỌNG**: KHÔNG bao giờ sửa file template gốc. Luôn copy ra file mới rồi thay thế.

## Templates có sẵn

| Template | File | Dịch vụ |
|----------|------|---------|
| **Hosting** | `/root/docs/HD_Temp/HD_hosting.docx` | Dịch vụ hosting, email hosting |
| **Tên miền** | `/root/docs/HD_Temp/HD_tenmien.docx` | Đăng ký, duy trì tên miền |
| **SSL** | `/root/docs/HD_Temp/HD_SSL.docx` | Chứng chỉ SSL bảo mật website |
| **Website** | `/root/docs/HD_Temp/HD_website.docx` | Thiết kế, sửa chữa website |
| **Thuê chỗ đặt** | `/root/docs/HD_Temp/HD_thue_cho_dat.docx` | Thuê chỗ đặt server (Colocation) |
| **Đại lý** | `/root/docs/HD_Temp/Mauhopdong_daily.docx` | Hợp đồng đại lý SSL |

## Dịch vụ BKNS.vn

**BKNS** (Công ty Cổ Phần Giải Pháp Mạng Bạch Kim) cung cấp:
- **Hosting**: Shared hosting, VPS, Cloud Server, Email hosting
- **Tên miền**: Đăng ký .vn, .com, .net, quốc tế
- **SSL**: Chứng chỉ bảo mật website (RapidSSL, GeoTrust, DigiCert)
- **Website**: Thiết kế, phát triển, sửa lỗi website
- **Colocation**: Thuê chỗ đặt server tại datacenter
- **Đại lý**: Chương trình đại lý cho reseller

## Quy trình

### Bước 1: Xác định loại hợp đồng

Khi Sếp yêu cầu tạo hợp đồng, xác định dịch vụ phù hợp:
- "Hợp đồng hosting cho..." → Dùng `HD_hosting.docx`
- "Hợp đồng tên miền..." → Dùng `HD_tenmien.docx`
- "Hợp đồng SSL..." → Dùng `HD_SSL.docx`
- "Hợp đồng website..." → Dùng `HD_website.docx`

Nếu không chắc loại nào, **hỏi Sếp**.

### Bước 2: Thu thập thông tin khách hàng

Trích xuất từ mô tả của Sếp (hỏi lại nếu thiếu):

| Thông tin | Bắt buộc? |
|-----------|-----------|
| Tên công ty/cá nhân | ✅ Bắt buộc |
| Địa chỉ | ✅ Bắt buộc |
| Người đại diện | ✅ Bắt buộc |
| Chức vụ | Nếu có |
| Mã số thuế | Nếu là công ty |
| Điện thoại | ✅ Bắt buộc |
| Email | Nếu có |
| Ngày ký hợp đồng | Mặc định: hôm nay |

### Bước 3: Xem nội dung template cần thay

Trước khi thay, đọc template để tìm đúng text khách hàng mẫu:

```bash
python3 -c "
from docx import Document
doc = Document('[TEMPLATE_PATH]')
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    if t and any(kw in t.lower() for kw in ['bên a', 'bên sử dụng', 'đại diện', 'địa chỉ', 'mã số', 'điện thoại', 'email', 'hôm nay', 'ngày']):
        print(f'P[{i}]: {t[:150]}')
for ti, table in enumerate(doc.tables):
    for ri, row in enumerate(table.rows):
        for ci, cell in enumerate(row.cells):
            t = cell.text.strip()
            if t and any(kw in t.lower() for kw in ['bên a', 'bên sử dụng', 'đại diện', 'địa chỉ', 'mã số']):
                print(f'T{ti}R{ri}C{ci}: {t[:150]}')
"
```

### Bước 4: Tạo file hợp đồng

Dùng script `fill_contract.py` để thay thế text:

```bash
python3 /root/openclaw/workspace/contracts/fill_contract.py \
  --template "[TEMPLATE_PATH]" \
  --output "/root/openclaw/workspace/contracts/output/[TEN_FILE].docx" \
  --data '{
    "TEXT CŨ TRONG TEMPLATE": "TEXT MỚI THAY THẾ",
    "TÊN KHÁCH MẪU": "TÊN KHÁCH THỰC",
    "ĐỊA CHỈ MẪU": "ĐỊA CHỈ THỰC"
  }'
```

**Quan trọng**: 
- Key trong JSON phải **ĐÚNG Y CHANG** text trong file DOCX gốc (kể cả khoảng trắng, dấu)
- Đọc template trước (Bước 3) để lấy chính xác text cần thay

### Bước 5: Xác nhận và gửi file

```
✅ Hợp đồng đã tạo xong!
📄 Loại: [Hosting/SSL/Tên miền/...]
👤 Khách hàng: [TÊN]
📁 File: contracts/output/[TEN_FILE].docx
💾 Đang gửi file qua Telegram...
```

## Ví dụ hoàn chỉnh

Sếp nhắn: "Tạo hợp đồng hosting cho công ty TNHH ABC, địa chỉ 456 Trần Phú Q5, đại diện Trần Văn B, MST 0312345678, SĐT 0901111222"

Tôm sẽ:
1. Chọn template: `HD_hosting.docx`
2. Đọc template để tìm text khách mẫu
3. Chạy script thay thế
4. Gửi file DOCX qua Telegram

## Lưu ý AN TOÀN
- **KHÔNG SỬA** file trong `/root/docs/HD_Temp/` — đây là template gốc
- Luôn output ra `/root/openclaw/workspace/contracts/output/`
- Đặt tên file có ý nghĩa: `HD-[LOAI]-[TEN_KHACH]-[NGAY].docx`
- Xóa file output cũ > 30 ngày để tiết kiệm disk
