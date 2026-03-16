---
name: content-calendar
description: Quản lý lịch đăng bài 5 lần/ngày cho fanpage Tý Tech — 3 slot cũ + 2 slot share AI/GitHub — tạo, theo dõi, nhắc nhở.
---

# Content Calendar Manager — Tý Tech

## Mục đích
Lên lịch và quản lý nội dung **5 bài/ngày** cho fanpage **Tý Tech** (Facebook): 3 slot theo pillar cũ + 2 slot **share AI/GitHub** từ scan influencer & trending repos. Đảm bảo consistency và đa dạng nội dung.

## Khi nào kích hoạt
- User nói: "lịch đăng bài", "content calendar", "lên lịch", "kế hoạch nội dung"
- User hỏi: "hôm nay đăng gì?", "tuần này có gì?"
- Tự kích hoạt khi gần tới giờ đăng bài (nếu chạy qua cron/reminder)

## Fanpage
- **Tên**: Tý Tech
- **Page ID**: 1012410591957125
- **Credentials**: `/root/openclaw/.openclaw/credentials/fb-credentials.env`
- **Knowledge**: `workspace/knowledge/facebook-tytech.md`
- **Skill đăng bài**: `social-media`

---

## Slot đăng bài hàng ngày (5 lần/ngày, GMT+7)

| Slot | Giờ | Loại nội dung ưu tiên | Mục đích |
|---|---|---|---|
| 🌅 SÁNG | 7h30 - 8h30 | Tech news, AI update, trending | Bắt trend sớm, commute reach |
| 📢 SÁNG SHARE | 9h00 - 10h00 | **Share AI/GitHub** (từ scan) | Chia sẻ repo hay, AI news |
| ☀️ TRƯA | 12h00 - 13h00 | Memes, hài hước, nhẹ nhàng | Giải trí giờ nghỉ, viral shares |
| 📢 CHIỀU SHARE | 15h00 - 16h00 | **Share AI/GitHub** (từ scan) | Chia sẻ tool, learning resources |
| 🌙 TỐI | 19h00 - 21h00 | Insight sâu, career, kinh nghiệm | PEAK engagement, bài quality |

> 📢 Slot SHARE lấy nội dung từ skill `viral-content-hunter` v2.0 — scan sáng 6h30 + tối 18h.

## Content Pillars & Tỷ lệ

| Pillar | Tỷ lệ/tuần | Số bài/tuần (~35 bài) |
|---|---|---|
| 🤖 AI & Tech Trends | 25% | ~9 bài |
| 📢 Share AI/GitHub | 28% | ~10 bài (2/ngày) |
| 😂 IT Memes & Humor | 20% | ~7 bài |
| 💼 Kinh nghiệm & Tips | 15% | ~5 bài |
| 🔥 Đời sống IT & Work-life | 12% | ~4 bài |

---

## Lịch đăng bài tuần (Template)

| Ngày | 🌅 Sáng (7h30) | 📢 Share (9h) | ☀️ Trưa (12h) | 📢 Share (15h) | 🌙 Tối (19-21h) |
|---|---|---|---|---|---|
| **T2** | 🤖 AI News tuần mới | 📢 AI/GitHub | 😂 Monday meme | 📢 AI/GitHub | 💼 Tips/Career |
| **T3** | 🤖 Tech update | 📢 AI/GitHub | 😂 IT Humor | 📢 AI/GitHub | 🔥 Work-life story |
| **T4** | 💼 Tool/Review | 📢 AI/GitHub | 😂 Meme | 📢 AI/GitHub | 🤖 AI Deep dive |
| **T5** | 🤖 Trending tech | 📢 AI/GitHub | 💼 Interview tips | 📢 AI/GitHub | 😂 Hài hước |
| **T6** | 🔥 Cuối tuần vibe | 📢 AI/GitHub | 😂 Friday meme | 📢 AI/GitHub | 💼 Weekend reading |
| **T7** | 🤖 Tổng hợp tuần | 📢 AI/GitHub | 😂 Lighter | 📢 AI/GitHub | 🔥 Tâm sự IT |
| **CN** | 💼 Chuẩn bị tuần | 📢 AI/GitHub | 😂 Sunday chill | 📢 AI/GitHub | 🤖 Preview |

---

## Quy trình tạo Content Calendar tuần

### Bước 1: Tạo calendar file
Mỗi tuần tạo/update file: `workspace/memory/content-calendar.md`

Format:
```markdown
# 📅 Content Calendar — Tý Tech

## Tuần [DD/MM - DD/MM/YYYY]

### Thứ 2 - DD/MM
| Slot | Pillar | Chủ đề | Status | Post ID |
|---|---|---|---|---|
| 🌅 7h30 | 🤖 AI | [Chủ đề cụ thể] | 📝 Draft | — |
| ☀️ 12h00 | 😂 Meme | [Chủ đề cụ thể] | ⏳ Scheduled | — |
| 🌙 19h00 | 💼 Tips | [Chủ đề cụ thể] | ✅ Posted | 1012410591957125_xxx |

### Thứ 3 - DD/MM
...

## Thống kê tuần
- Tổng bài đã đăng: X/21
- Pillar balance: 🤖 X | 😂 X | 💼 X | 🔥 X
- Top post: [link] — reach: XXX
```

### Bước 2: Soạn draft cho từng slot
Khi gần tới giờ đăng (hoặc khi Sếp yêu cầu lên lịch):
1. Kiểm tra calendar → slot nào cần soạn
2. Chọn chủ đề phù hợp pillar của slot đó
3. Soạn bài theo tông giọng Tý Tech (xem `facebook-tytech.md`)
4. Gửi preview cho Sếp qua Telegram
5. Sếp duyệt → đăng bài qua skill `social-media`
6. Update status trong calendar: `✅ Posted` + Post ID

### Bước 3: Review cuối ngày
- Kiểm tra 3/3 slots đã đăng chưa
- Nếu thiếu → báo Sếp: "Hôm nay còn thiếu bài [slot]. Đăng bù không Sếp?"
- Ghi chú performance nếu có engagement data

---

## Status codes
| Code | Nghĩa |
|---|---|
| 📝 Draft | Đã soạn, chưa duyệt |
| 👀 Review | Đang chờ Sếp duyệt |
| ⏳ Scheduled | Đã lên lịch đăng |
| ✅ Posted | Đã đăng thành công |
| ❌ Skipped | Bỏ qua slot này |
| 🔄 Rescheduled | Dời sang slot khác |

---

## Autopilot Rules
1. **Nếu Sếp đã duyệt calendar cả tuần** → Tôm tự đăng theo lịch
2. **Nếu chưa duyệt** → Tôm soạn draft, gửi preview, chờ OK
3. **Bài trending urgent** → Soạn nhanh, xin phép Sếp đăng ngoài lịch
4. **LUÔN tuân thủ** luật nội dung trong `facebook-tytech.md`

## Kết hợp skills
- `social-media`: Đăng bài lên Facebook
- `viral-content-hunter` **(v2.0)**: Scan sáng/tối → 2 bài share AI/GitHub/ngày
- `seo-writer`: Soạn bài dài → tóm gọn cho Facebook
- `wp-publisher`: Bài blog → cross-post summary lên Facebook
- `smart-reminder`: Nhắc nhở giờ đăng bài + nhắc scan

## ⚠️ Calendar Verification (BẮT BUỘC)

### Sau khi đánh dấu "✅ Posted":
```bash
# Verify bài thật sự đã đăng trên Facebook
source /root/openclaw/.openclaw/credentials/fb-credentials.env
curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}/feed?fields=message,created_time&limit=5&access_token=${FB_PAGE_ACCESS_TOKEN}" | python3 -m json.tool
```

### Quy tắc:
1. **KHÔNG update status "✅ Posted" nếu chưa verify** bài thật sự xuất hiện trên fanpage
2. Cuối ngày, kiểm tra 3/3 slots → nếu thiếu, báo Sếp ngay (không im lặng)
3. Cuối tuần, so sánh calendar vs thực tế → report chênh lệch nếu có
