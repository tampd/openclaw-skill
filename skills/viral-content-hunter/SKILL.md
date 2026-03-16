---
name: viral-content-hunter
description: Săn tìm nội dung trending AI & vibe coding 2 lần/ngày — 5 bài/ngày cho fanpage Tý Tech (3 lịch cũ + 2 share).
---

# Viral Content Hunter — Tý Tech (v2.0)

## Mục đích
Chủ động quét các nguồn tin tech quốc tế, **tập trung AI & vibe coding**, chọn nội dung hay nhất để viết lại và chia sẻ trên fanpage Tý Tech. Scan **2 lần/ngày** (sáng + tối), đăng **5 bài/ngày** (3 slot cũ + 2 bài share mới).

## Khi nào kích hoạt
- User nói: "tìm trend", "tin tech hôm nay", "có gì hot", "cập nhật", "săn bài", "scan"
- Tự kích hoạt 2 lần/ngày: sáng 6h30 + tối 18h (GMT+7)
- Khi skill `content-calendar` cần gợi ý chủ đề cho slot share

## Fanpage target
- **Tý Tech** — Page ID: 1012410591957125
- Audience: Dân IT, developer, sysadmin, AI enthusiast Việt Nam
- Tone: Hài hước, gần gũi, insight, Gen Z IT vibes

---

## 📅 Slot đăng bài: 5 BÀI/NGÀY

| Slot | Giờ (GMT+7) | Loại | Nguồn chính |
|---|---|---|---|
| 🌅 Sáng | 7h30-8h30 | Tin tech/AI *(lịch cũ)* | Hacker News, Reddit, blogs |
| 📢 Sáng share | 9h00-10h00 | **Share AI/GitHub** | Influencer scan + GitHub trending |
| ☀️ Trưa | 12h00-13h00 | Memes/Humor *(lịch cũ)* | Meme nguồn IT |
| 📢 Chiều share | 15h00-16h00 | **Share AI/GitHub** | GitHub repos + AI tools mới |
| 🌙 Tối | 19h00-21h00 | Insight sâu *(lịch cũ)* | Deep research |

> **3 slot cũ** (🌅☀️🌙) hoạt động theo `content-calendar` skill.
> **2 slot share mới** (📢) dùng quy trình scan dưới đây.

---

## 🎯 Focus chủ đề (v2.0)

### Ưu tiên CAO:
- **AI/LLM**: ChatGPT, Claude, Gemini, Llama, open-source LLM, agents, RAG, fine-tuning
- **Vibe Coding**: Cursor, Aider, Copilot, Cline, AI code generation, agentic coding
- **GitHub AI repos**: Repos trending liên quan AI, ML, coding assistants

### Ưu tiên TRUNG BÌNH:
- DevOps, automation, cloud
- Security updates
- Developer tools mới

### Ưu tiên THẤP (cho 3 slot cũ):
- Memes IT, humor
- Career tips, work-life
- General tech news

---

## Nguồn tin (Sources)

### 📋 Danh sách curated
- **100 IT Influencers quốc tế**: `workspace/knowledge/tech-influencers-international.md`
- **50 GitHub Repos**: `workspace/knowledge/github-curated-repos.md`

### 🌍 Nguồn quét online (ưu tiên cao → thấp)
1. **GitHub Trending** — Daily repos, filter: Python, TypeScript, Rust
   ```bash
   # Dùng web search hoặc browse trực tiếp
   # URL: https://github.com/trending
   # URL: https://github.com/trending/python
   ```

2. **Hacker News** — Top stories (AI/programming)
   ```bash
   for ID in $(curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | python3 -c "import sys,json; [print(i) for i in json.load(sys.stdin)[:10]]"); do
     curl -s "https://hacker-news.firebaseio.com/v0/item/${ID}.json" | python3 -c "
   import sys,json
   s=json.load(sys.stdin)
   print(f\"- [{s.get('score',0)} pts] {s.get('title','')} | {s.get('url','')}\")"
   done
   ```

3. **Reddit** — r/programming, r/MachineLearning, r/LocalLLaMA
4. **X/Twitter**: @AndrewYNg, @karpathy, @simonw, @levelsio
5. **TechCrunch / The Verge / Ars Technica** — via web search
6. **AI Blogs**: OpenAI, Google AI, Anthropic, Hugging Face
7. **Product Hunt** — AI launches

### 🇻🇳 Việt Nam
1. **Viblo.asia** — Top posts
2. **Facebook groups**: J2 Team, Dạy nhau học IT
3. **blog.chaiko.info** — Bài mới từ Sếp Tâm

---

## Quy trình scan (2 lần/ngày)

### ⏰ Scan Sáng — 6h30 GMT+7

```
Bước 1: QUÉT GITHUB
├── Browse GitHub Trending (All, Python, TypeScript)
├── Lọc repos liên quan AI, LLM, vibe coding, dev tools
├── Check danh sách 50 repos → có release/update mới nào?
└── Thu thập 5-8 repos tiềm năng

Bước 2: QUÉT INFLUENCER + NEWS
├── Web search: "[influencer name] AI" hoặc "AI news today"
├── Quét Hacker News top stories (lọc AI/programming)
├── Check Reddit r/LocalLLaMA, r/MachineLearning
└── Thu thập 5-8 tin tiềm năng

Bước 3: LỌC & ĐÁNH GIÁ
├── Score từng bài theo bảng scoring (xem bên dưới)
├── Ưu tiên: AI + vibe coding content
├── Freshness: < 24h
└── Chọn TOP 3 bài điểm cao nhất

Bước 4: SOẠN 2 BÀI SHARE
├── Bài 1: Cho slot 📢 Sáng share (9h-10h)
├── Bài 2: Cho slot 📢 Chiều share (15h-16h)
├── Dùng template phù hợp (xem github-share-template.md)
├── GitHub repos → dùng format "Ai đó đã chia sẻ..."
├── Influencer insights → viết lại ý, đổi cách trình bày
└── Gửi duyệt Sếp qua Telegram

Bước 5: LOG
└── Ghi vào memory/influencer-scan-log.md
```

### ⏰ Scan Tối — 18h00 GMT+7

```
Quy trình tương tự scan sáng, nhưng:
├── Focus: repos/tin mới xuất hiện trong ngày
├── Output: Tích lũy cho bài share sáng hôm sau
├── Nếu có tin NÓNG → soạn draft bổ sung luôn
└── Cuối tuần: tổng hợp top trends tuần cho content calendar
```

---

## 🖼️ Hình ảnh — BẮT BUỘC MỌI BÀI

> **Mỗi bài Facebook PHẢI có ít nhất 1 hình ảnh đính kèm.** Bài có ảnh reach gấp 2-3x bài text.

### Nguồn ảnh (ưu tiên):
1. **Screenshot/demo** từ repo/tool đang chia sẻ (crop gọn, highlight phần hay)
2. **Ảnh minh họa AI-generated** — dùng tool generate_image tạo banner
3. **Ảnh free** từ Unsplash, Pexels, Openverse — search theo keyword bài viết
4. **Meme template** tự tạo nội dung gốc cho bài humor
5. **Infographic đơn giản** — tóm tắt danh sách/so sánh bằng hình

### Quy tắc ảnh:
- Kích thước: **1200×630** (landscape) hoặc **1080×1080** (square)
- Mỗi ảnh PHẢI có alt text mô tả
- KHÔNG dùng ảnh watermark, ảnh mờ, ảnh stock quá generic
- Ưu tiên ảnh có **text overlay ngắn** — tạo điểm dừng khi scroll
- Nếu share repo → chụp screenshot README hoặc demo GIF

### Ý tưởng ảnh theo loại bài:
| Loại bài | Ảnh gợi ý |
|---|---|
| GitHub repo | Screenshot README, demo UI, architecture diagram |
| AI news | Logo/banner công ty, screenshot sản phẩm, comparison chart |
| Vibe coding | Screenshot editor + AI suggestion, before/after code |
| Learning resource | Infographic tóm tắt, roadmap visual |
| Meme | Template meme IT + nội dung gốc |

---

## 😜 Icon & Emoji — Tạo cảm xúc tự nhiên

### Bảng icon gợi ý theo cảm xúc:
| Cảm xúc | Icons |
|---|---|
| 🤩 Ngạc nhiên/wow | 🤯 😱 🔥 💥 ⚡ 🚀 |
| 😂 Hài hước | 😅 🤣 💀 🫠 🤡 😎 |
| 🤔 Tò mò/suy nghĩ | 🧐 🤓 💭 👀 ❓ 🔍 |
| 💪 Truyền động lực | 🫡 ✊ 🎯 🏆 🌟 💡 |
| ❤️ Yêu thích/cảm ơn | 🥰 😍 💖 🙏 👏 🤝 |
| ⚠️ Cảnh báo/quan trọng | 🚨 ⚠️ 📢 🔴 ❗ 🛑 |
| 📦 Chia sẻ tài nguyên | 🔗 📚 🧰 📌 🗂️ 💾 |
| 💻 Coding/tech | 🖥️ ⌨️ 🧠 🤖 🛠️ ⚙️ |

### Quy tắc icon:
1. **Mỗi bài 4-6 emoji** (tăng từ 2-4 cũ) — đặt tự nhiên trong câu
2. **Icon đầu bài** → tạo điểm nhấn visual khi scroll feed
3. **Icon đầu mỗi bullet** → dễ scan, phong phú hơn
4. **Xen kẽ icon khác nhau** — KHÔNG lặp cùng 1 emoji
5. **Dùng icon phù hợp ngữ cảnh** — vui thì 😂, nghiêm thì 💡
6. **Kaomoji cho bài chill** — đôi khi dùng (╯°□°)╯, ¯\_(ツ)_/¯, (☞ﾟヮﾟ)☞

---

## Scoring System

| Tiêu chí | Trọng số | Mô tả |
|---|---|---|
| AI/Vibe Coding | 30% | Liên quan trực tiếp AI, LLM, vibe coding? |
| Virality | 25% | Potential viral trên Facebook VN? |
| Freshness | 20% | Tin mới < 24h? Chưa ai đăng VN? |
| Visual | 15% | Có ảnh/demo/video đi kèm? Dễ tạo visual? |
| Practical | 10% | Audience IT VN dùng được ngay? |

**Ngưỡng đăng**: Score ≥ 7/10 → soạn bài share
**Score < 5** → bỏ qua

---

## Template bài share

### Cho GitHub repos:
Xem chi tiết: `viral-content-hunter/github-share-template.md`

**Format ngắn:**
```
🔗 Ai đó đã chia sẻ những tài nguyên hữu ích về [CHỦ ĐỀ]...

[Mô tả ngắn gọn 2-3 dòng]

📌 Highlights:
• [Điểm 1]
• [Điểm 2]
• [Điểm 3]

👉 Link GitHub: [URL]

[CTA câu hỏi mở] 👇

#TýTech #GitHub #[hashtag]
```

### Cho Influencer insights / AI news:
```
[Emoji] [Hook 2 dòng — viết lại ý gốc bằng cách khác]

[Nội dung chính 3-5 dòng — cùng ý nghĩa nhưng trình bày khác]

💡 Góc nhìn:
[Thêm nhận xét riêng hoặc so sánh với context VN]

📖 Nguồn: [Credit tác giả/nguồn gốc]

[CTA câu hỏi] 👇

#TýTech #AI #[hashtag chủ đề]
```

---

## Viết lại nội dung — Rules (v2.1)

### PHẢI:
- ✅ Viết tiếng Việt, xen thuật ngữ Anh tự nhiên
- ✅ **Giữ nguyên ý gốc**, nhưng **đổi cách trình bày**
- ✅ **LUÔN đính kèm ≥1 hình ảnh** (screenshot, banner, meme, infographic)
- ✅ Emoji 4-6 cái, xen kẽ tự nhiên trong câu, icon đa dạng
- ✅ Hook 2 dòng đầu phải gây tò mò + icon bắt mắt
- ✅ Mỗi bullet dùng icon khác nhau thay vì dấu •
- ✅ CTA cuối bài (câu hỏi mở) kèm 👇 hoặc kaomoji
- ✅ Credit nguồn gốc (tên tác giả + link)
- ✅ GitHub repos → format "Ai đó đã chia sẻ..."
- ✅ Hashtags: 3-5, luôn có #TýTech

### KHÔNG:
- ❌ KHÔNG đăng bài chỉ có text — phải có ảnh
- ❌ KHÔNG copy nguyên bài
- ❌ KHÔNG dịch máy
- ❌ KHÔNG tin chưa verify
- ❌ KHÔNG lặp cùng 1 emoji liên tục
- ❌ KHÔNG vi phạm luật Tý Tech (xem `facebook-tytech.md`)

---

## Kết hợp skills
- `content-calendar`: Quản lý 5 slot/ngày, gợi ý chủ đề
- `social-media`: Đăng bài sau duyệt
- `seo-writer`: Bài blog dài → tóm cho FB
- `web-researcher`: Research sâu topic
- `smart-reminder`: Nhắc nhở scan sáng/tối

## Tần suất
- **Scan**: 2 lần/ngày (6h30 + 18h00 GMT+7)
- **Bài share**: 2 bài/ngày (9h-10h + 15h-16h GMT+7)
- **Weekly digest**: Cuối tuần tổng hợp top trends tuần
