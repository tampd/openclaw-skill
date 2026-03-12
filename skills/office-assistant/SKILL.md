---
name: office-assistant
description: Trợ lý văn phòng tổng hợp — soạn email chuyên nghiệp, ghi chú cuộc họp, quản lý todo/deadline, tạo báo giá, tóm tắt tài liệu, tính toán nghiệp vụ.
---

# Office Assistant — Trợ Lý Văn Phòng Thông Minh

## Mục đích
Giúp Sếp xử lý nhanh các công việc văn phòng hàng ngày bằng AI: soạn email, ghi chú meeting, theo dõi todo, tạo báo giá, tóm tắt tài liệu.

## Khi nào kích hoạt
- User yêu cầu soạn/viết email
- User muốn ghi chú cuộc họp (meeting notes/minutes)
- User cần quản lý danh sách việc (todo, task list)
- User hỏi tạo báo giá (quotation)
- User muốn tóm tắt nội dung file/URL
- User cần tính toán chi phí, thuế, công nợ
- User cần soạn thảo văn bản (thông báo, biên bản, đề xuất)

---

## 1. Soạn Email Chuyên Nghiệp

### Khi user nói: "soạn email", "viết email", "trả lời email", "email cho..."

**Quy trình:**
1. Hỏi rõ: Người nhận, chủ đề, nội dung chính, tone (trang trọng/thân thiện/trung lập)
2. Soạn email theo template

**Template Email tiếng Việt:**
```
Kính gửi [Tên người nhận],

[Nội dung chính — 2-3 đoạn ngắn]

[Call-to-action nếu cần]

Trân trọng,
[Tên Sếp]
[Chức vụ] | [Công ty]
[SĐT] | [Email]
```

**Template Email tiếng Anh:**
```
Dear [Name],

[Body — concise, professional, 2-3 paragraphs]

[CTA if needed]

Best regards,
[Name]
[Title] | [Company]
```

**Nguyên tắc:**
- Ngắn gọn, rõ ràng, chuyên nghiệp
- Không dùng từ lóng, emoji trong email formal
- Nếu email bán hàng → tham khảo `knowledge/bkns/faq/sales-scenarios.md`
- Nếu email gửi KH cũ → kiểm tra `memory/clients.md` trước

---

## 2. Ghi Chú Cuộc Họp (Meeting Minutes)

### Khi user nói: "ghi meeting", "ghi chú cuộc họp", "minutes", "biên bản họp"

**Quy trình:**
1. User cung cấp nội dung cuộc họp (text/voice)
2. Format thành meeting minutes chuẩn

**Template:**
```markdown
# 📋 Meeting Minutes — [Chủ đề]
**Ngày**: [DD/MM/YYYY] | **Thời gian**: [HH:MM - HH:MM]
**Người tham dự**: [Danh sách]
**Người ghi**: Tôm (AI Assistant)

## Tóm tắt
[2-3 câu tổng quan]

## Nội dung thảo luận
1. [Chủ đề 1]
   - [Chi tiết]
   - **Quyết định**: [...]

2. [Chủ đề 2]
   - [Chi tiết]
   - **Quyết định**: [...]

## Action Items
| # | Task | Người phụ trách | Deadline |
|---|------|-----------------|----------|
| 1 | [...] | [...] | [...] |

## Ghi chú thêm
[Nếu có]
```

**Lưu file:** `workspace/reports/meeting-YYYY-MM-DD-[topic].md`

---

## 3. Quản Lý Todo / Task List

### Khi user nói: "thêm việc", "todo", "cần làm", "deadline", "task list"

**File quản lý:** `workspace/memory/todo.md`

**Quy trình:**
- **Thêm**: Ghi task mới vào file, đánh priority (🔴 Urgent / 🟡 Normal / 🟢 Low)
- **Xem**: Đọc file, hiển thị danh sách format gọn
- **Hoàn thành**: Đánh dấu ✅ và di chuyển xuống "Done"
- **Nhắc**: Kết hợp với `smart-reminder` nếu có deadline

**Format todo.md:**
```markdown
# 📝 Todo List

## 🔴 Urgent
- [ ] [Task] — Deadline: [date]

## 🟡 Normal  
- [ ] [Task] — Deadline: [date]

## 🟢 Low Priority
- [ ] [Task]

## ✅ Done (tuần này)
- [x] [Task] — Done: [date]
```

### Xem todo nhanh:
```bash
cat /root/openclaw/workspace/memory/todo.md
```

---

## 4. Tạo Báo Giá (Quotation)

### Khi user nói: "báo giá", "quotation", "quote", "bảng giá cho KH"

**Quy trình:**
1. Xác định dịch vụ cần báo giá
2. Tra giá từ knowledge base BKNS (đọc file)
3. Format thành báo giá chuyên nghiệp

**Template Báo Giá:**
```markdown
# 📄 BÁO GIÁ DỊCH VỤ

**Ngày**: [DD/MM/YYYY]
**Khách hàng**: [Tên]
**Liên hệ**: [SĐT / Email]

---

| # | Dịch vụ | Gói | Thời hạn | Đơn giá | Thành tiền |
|---|---------|-----|----------|---------|------------|
| 1 | [...]   | [...] | [...] | [...] | [...] |
| 2 | [...]   | [...] | [...] | [...] | [...] |

**Tổng cộng**: [VNĐ]
**Chiết khấu** (nếu có): [%]
**Thanh toán**: [VNĐ]

---

💡 **Lưu ý**: Giá trên là giá tham khảo, có thể thay đổi. Vui lòng liên hệ BKNS để xác nhận.
🔗 **Website**: bkns.vn | **Hotline**: 1900.6740
```

**Nguyên tắc:**
- LUÔN đọc file giá từ `knowledge/bkns/pricing/` — KHÔNG bịa
- Gợi ý combo nếu phù hợp → đọc `knowledge/bkns/faq/combo-packages.md`
- Ghi vào `memory/clients.md` sau khi báo giá

---

## 5. Tóm Tắt Tài Liệu

### Khi user nói: "tóm tắt", "summary", "đọc file này", "nội dung chính"

**Quy trình:**
1. Đọc file (txt, md) hoặc URL
2. Tóm tắt theo format: TL;DR + Key Points + Action Items

**Template:**
```
📖 **Tóm tắt: [Tên tài liệu]**

**TL;DR**: [1-2 câu tổng quan]

**Nội dung chính:**
1. [Point 1]
2. [Point 2]
3. [Point 3]

**Cần hành động:**
- [Action item nếu có]
```

---

## 6. Tính Toán Nghiệp Vụ

### Khi user nói: "tính giá", "chi phí", "thuế", "total"

**Khả năng:**
- Tính chi phí dịch vụ theo thời hạn (1 tháng / 12 tháng / 36 tháng)
- Tính chiết khấu dài hạn
- Tính tổng combo nhiều dịch vụ
- So sánh chi phí giữa các gói

**Luôn tra giá từ knowledge base, KHÔNG ước tính.**

---

## 7. Soạn Văn Bản Khác

### Khi user nói: "viết thông báo", "soạn đề xuất", "biên bản", "văn bản"

**Khả năng:**
- Thông báo nội bộ
- Đề xuất dự án / đề xuất chi phí
- Biên bản làm việc
- Thư mời / thư cảm ơn

**Nguyên tắc:** Hỏi rõ mục đích, đối tượng, tone → soạn chuyên nghiệp, ngắn gọn.

---

## 8. Tạo PDF Chuyên Nghiệp

### Khi user nói: "tạo PDF", "xuất PDF", "báo giá PDF", "report PDF"

**Setup (1 lần):**
```bash
npm install -g ai-pdf-builder
```

**Sử dụng:**
```bash
# Tạo PDF từ nội dung markdown
npx ai-pdf-builder generate report ./content.md -o output.pdf --company "BKNS"

# Tạo báo giá PDF
npx ai-pdf-builder generate proposal ./bao-gia.md -o bao-gia.pdf --company "BKNS JSC"

# AI tạo nội dung + PDF
npx ai-pdf-builder ai memo "Báo cáo tháng 3/2026" -o report.pdf --company "BKNS"

# Tóm tắt PDF
npx ai-pdf-builder summarize ./long-doc.pdf -o summary.pdf --pdf
```

**Document types**: `whitepaper`, `memo`, `agreement`, `report`, `proposal`, `nda`

**Kết hợp:**
- Sau khi tạo báo giá Markdown → xuất PDF cho KH
- Meeting minutes → PDF cho archive
- Hợp đồng (contract-writer) → PDF bản chính thức

---

## Self-Learning

Sau mỗi task văn phòng:
1. Nếu Sếp sửa lại → ghi pattern vào `memory/lessons.md`
2. Nếu email/báo giá cho KH → ghi vào `memory/clients.md`
3. Nếu câu hỏi lặp lại → ghi vào `memory/faq-learned.md`

## Nguyên tắc chung
- ✅ Chuyên nghiệp, chính xác, ngắn gọn
- ✅ Dùng tiếng Việt mặc định (trừ khi user yêu cầu tiếng Anh)
- ✅ Output phù hợp Telegram (dưới 30 dòng nếu có thể)
- ✅ Luôn hỏi nếu thiếu thông tin — KHÔNG đoán
- ❌ KHÔNG bịa giá, số liệu, thông tin liên hệ

