# Influencer & GitHub Scan Automation — Tý Tech

## Mục tiêu
Scan 2 lần/ngày để tìm content AI & vibe coding hay từ 100 influencers + 50 GitHub repos → soạn 2 bài share/ngày.

## Lịch scan

| Scan | Giờ (GMT+7) | UTC | Mục đích |
|---|---|---|---|
| 🌅 Sáng | 6h30 | 23:30 (hôm trước) | Quét trend mới → bài 📢 9h + 📢 15h |
| 🌙 Tối | 18h00 | 11:00 | Quét update cuối ngày → tích lũy cho sáng hôm sau |

## Cron config (nếu OpenClaw hỗ trợ)

```json
{
  "cron_jobs": [
    {
      "id": "influencer-scan-morning",
      "schedule": "30 23 * * * ",
      "timezone": "UTC",
      "task": "Scan sáng: quét GitHub Trending + top influencer AI news + Hacker News. Chọn top 3, soạn 2 bài share theo template trong viral-content-hunter/github-share-template.md. Lưu log vào memory/influencer-scan-log.md.",
      "skill": "viral-content-hunter"
    },
    {
      "id": "influencer-scan-evening",
      "schedule": "0 11 * * *",
      "timezone": "UTC",
      "task": "Scan tối: quét GitHub repos mới + AI news update cuối ngày. Tích lũy content cho bài share sáng hôm sau. Lưu log vào memory/influencer-scan-log.md.",
      "skill": "viral-content-hunter"
    }
  ]
}
```

## Quy trình mỗi lần scan

### Input:
- `workspace/knowledge/tech-influencers-international.md` — 100 influencers
- `workspace/knowledge/github-curated-repos.md` — 50 repos
- GitHub Trending page
- Hacker News API

### Workflow:
```
1. QUÉT GITHUB (5 phút)
   ├── Browse GitHub Trending (All + Python + TypeScript)
   ├── Filter: keyword AI, LLM, agent, vibe, coding
   ├── Check repos trong danh sách 50 → releases mới?
   └── Thu thập 5-8 repos tiềm năng

2. QUÉT TIN TỨC AI (5 phút)
   ├── Web search: "AI news today", "[influencer] AI"
   ├── Hacker News API top 10
   ├── Reddit r/LocalLLaMA, r/MachineLearning
   └── Thu thập 5-8 tin tiềm năng

3. SCORING (2 phút)
   ├── Áp dụng bảng scoring trong SKILL.md
   ├── AI/Vibe Coding: 35% | Virality: 25% | Freshness: 20%
   ├── Practical: 15% | Visual: 5%
   └── Chọn TOP 3

4. SOẠN DRAFT (10 phút)
   ├── Bài 1: GitHub repo hay → template "Ai đó đã chia sẻ..."
   ├── Bài 2: AI insight → viết lại ý, đổi cách trình bày
   ├── Credit nguồn gốc
   └── Thêm hashtags + CTA

5. GỬI DUYỆT (1 phút)
   ├── Push preview qua Telegram cho Sếp
   ├── Format: "📢 Share Alert — [Chủ đề]"
   └── Sếp OK → đăng qua social-media skill

6. LOG
   └── Ghi vào memory/influencer-scan-log.md
```

### Output mẫu:
```markdown
## 📢 Share Alert — Scan Sáng 16/03/2026

### Top 3 trending hôm nay:

**1. [Tên repo/bài]** ⭐ Score: 8.5/10
- Nguồn: GitHub Trending / [Influencer]
- Link: [URL]
- Chủ đề: AI / Vibe Coding
- Tại sao hot: [1 dòng]

**Draft bài share 1 (slot 9h):**
---
🔗 Ai đó đã chia sẻ những tài nguyên hữu ích về...
[Nội dung]
---

**Draft bài share 2 (slot 15h):**
---
[Nội dung bài 2]
---

📌 Sếp duyệt? Reply "OK" hoặc "sửa"
```
