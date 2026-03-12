---
name: file-organizer
description: Quản lý, tìm kiếm, phân loại và dọn dẹp file trên VPS. Trợ lý lưu trữ số.
---

# File Organizer — Trợ Lý Quản Lý File

## Mục đích
Giúp user quản lý file trên VPS: tìm kiếm nhanh, phân loại, dọn dẹp, và báo cáo tình trạng lưu trữ.

## Các Chức Năng

### 1. Tìm kiếm file
**Trigger**: "Tìm file...", "File X ở đâu?", "Có file nào về..."

```bash
# Tìm theo tên
find /root -name "*keyword*" -type f 2>/dev/null | head -20

# Tìm theo nội dung
grep -rl "keyword" /root/openclaw/workspace/ 2>/dev/null | head -10

# Tìm file lớn
find /root -size +100M -type f 2>/dev/null | head -10

# Tìm file mới chỉnh sửa
find /root -mtime -1 -type f 2>/dev/null | head -20
```

**Format trả lời**:
```
🔍 Kết quả tìm kiếm "[keyword]":
1. 📄 [path/to/file1] — [size] — [last modified]
2. 📄 [path/to/file2] — [size] — [last modified]
Tổng: [N] file tìm thấy
```

### 2. Báo cáo dung lượng
**Trigger**: "Dung lượng VPS", "Còn bao nhiêu ổ cứng?"

```bash
# Tổng quan
df -h /

# Top thư mục nặng nhất
du -sh /root/*/ 2>/dev/null | sort -rh | head -10

# File nặng nhất
find /root -type f -size +50M -exec ls -lh {} \; 2>/dev/null | sort -k5 -rh | head -10
```

**Format trả lời**:
```
💾 **Báo cáo Dung Lượng VPS**

📊 Tổng quan: [Used]/[Total] ([Used%])
📁 Top thư mục:
1. [folder] — [size]
2. [folder] — [size]

🗑️ Đề xuất dọn dẹp:
- [file/folder có thể xóa] — [lý do]
```

### 3. Dọn dẹp file
**Trigger**: "Dọn dẹp VPS", "Xóa file tạm", "Dọn log cũ"

**Quy trình**:
1. Quét file có thể dọn:
   - Log cũ > 30 ngày
   - File `.tmp`, `.bak` rác
   - Cache không cần thiết
2. **LUÔN liệt kê trước**, chờ user xác nhận
3. Dùng `trash` thay `rm` nếu có (nếu không, `mv` sang `/tmp/cleanup/`)
4. Báo cáo sau khi dọn

> ⚠️ **KHÔNG BAO GIỜ** tự ý xóa file mà không hỏi user trước. Luôn liệt kê danh sách và chờ "OK" hoặc "Xóa đi".

```bash
# Tạo thư mục cleanup tạm
mkdir -p /tmp/cleanup

# Di chuyển (KHÔNG xóa) file vào cleanup
mv [file] /tmp/cleanup/
```

### 4. Sắp xếp file
**Trigger**: "Sắp xếp thư mục X", "Phân loại file trong..."

Phân loại file theo:
- **Loại**: Documents (.md, .txt, .pdf), Code (.py, .js, .sh), Data (.json, .csv), Media (.png, .jpg)
- **Thời gian**: Theo tháng/năm
- **Dự án**: Theo nội dung/context

## Phạm vi hoạt động
- **Được phép tự do**: `/root/openclaw/workspace/` và subdirectories
- **Cần hỏi trước**: Các thư mục khác trong `/root/`
- **KHÔNG ĐƯỢC chạm**: `/etc/`, `/usr/`, `/var/`, system files

## Lưu ý an toàn
- **`trash` > `rm`** — luôn ưu tiên di chuyển thay vì xóa vĩnh viễn
- **Backup trước khi sắp xếp** — `cp -r [folder] [folder].bak` trước khi restructure
- **Không đổi tên file config** — `.openclaw/`, `.git/`, `credentials/` là NO-GO
- **Log mọi thao tác** — ghi vào `memory/YYYY-MM-DD.md` để có audit trail
