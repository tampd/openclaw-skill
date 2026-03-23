---
name: context-manager
description: Quản lý context window & tối ưu token — Giám sát sức khỏe context, memory 3 tầng, token budgeting, compaction, tiết kiệm chi phí LLM.
---

# Context Manager — Quản Lý Context & Token

> Giám sát, tối ưu và bảo vệ context window. Tránh hallucination, giảm chi phí token.

## Khi nào kích hoạt
- Context window bắt đầu đầy (≥50%)
- Session kéo dài >30 phút hoặc >20 messages
- Output bắt đầu dài dòng, lặp lại, hoặc bỏ sót instructions
- User nói: "compact", "context đầy", "phiên mới", "tiết kiệm token"

## 1. Context Health Monitor

| Mức | % Window | Hành động |
|-----|----------|-----------|
| 🟢 Fresh | 0–30% | Tiếp tục bình thường |
| 🟡 Loaded | 30–50% | Cân nhắc compact |
| 🟠 Attention | 50–70% | **Compact ngay**, lưu progress |
| 🔴 Heavy | 70–85% | **Stop → save → phiên mới** |
| 💀 Critical | >85% | **Force stop, phiên mới ngay** |

**Rule**: Kiểm tra context health mỗi 10 tool calls hoặc 5 tin nhắn dài.

> ⚠️ Ở 70% context → precision loss. Ở 85% → hallucination rate tăng 3x.

## 2. Memory Architecture (3 Tầng)

### Tầng 1: System Prompt (Luôn Load, ≤500 tokens)
- Rules quan trọng nhất
- Tech stack
- Skill map (tên + trigger, KHÔNG chi tiết)

### Tầng 2: Session Memory (Load khi cần)
- `memory/lessons.md` — Bài học quan trọng (≤10 entries)
- `memory/progress.md` — Task hiện tại
- `memory/state.json` — Phase, blockers

### Tầng 3: Deep Memory (Search khi cần)
- Archive lessons cũ
- Vector DB / semantic search
- **KHÔNG dump toàn bộ vào context** → dùng search

**Rule**: Chỉ load file memory **liên quan task hiện tại**. Giảm 80% input tokens.

## 3. Token Budget

| Thành phần | % Budget |
|-----------|---------|
| System prompt + Rules | 5–8% |
| Memory files | 5–10% |
| Conversation history | 30–40% |
| Tool outputs | 20–30% |
| Response generation | 15–25% |
| **Buffer (safety)** | **10%** |

### Tiết kiệm token
1. Tool output >500 dòng → giữ 50 đầu + 20 cuối
2. Đọc file → chỉ định range (line 1-50), KHÔNG đọc toàn bộ
3. Search → giới hạn 10 kết quả
4. Request structured output (JSON/bullets) thay vì prose dài
5. Error → giữ dòng error chính, bỏ full stack trace

## 4. Compaction

### Khi nào compact
```
≥50% context + task chưa xong → compact (giữ task + decisions, bỏ tool outputs cũ)
≥70% context → save progress → phiên mới → load chỉ progress.md
```

### Template cho phiên mới
```markdown
## Session Summary
**Task**: [mô tả ngắn]
**Progress**: [x/y steps done]
**Key Decisions**: [quyết định đã làm]
**Current Blocker**: [nếu có]
**Next Step**: [step tiếp theo cụ thể]
**Files Changed**: [danh sách file đã sửa]
```

### Kỹ thuật
| Kỹ thuật | Tiết kiệm |
|----------|-----------|
| Head/Tail Preserve | ~60% |
| Structured Summary | ~70% |
| Tool Output Prune | ~40% |
| Conversation Rolling | ~50% |
| Subagent Isolation | ~80% |

## 5. Prompt Optimization

```
❌ BAD: "Tôi muốn bạn giúp tôi tạo một trang web bán hàng online 
với đầy đủ tính năng giỏ hàng, thanh toán, đăng nhập..."

✅ GOOD: "Build ecommerce: Next.js + Tailwind + PostgreSQL
Features: cart, checkout, auth, product CRUD. Reqs: responsive, SEO"
```

**Rules**: Lead with keywords → dùng commands → bullet points > paragraphs → reference by name → 1 task/message

## 6. Cost Control

### Model Routing (tiết kiệm 50-80%)
| Task | Model | Cost |
|------|-------|------|
| Auto-format, lint | Haiku/GPT-4o-mini | 💲 |
| Standard coding | Sonnet/GPT-4o | 💲💲 |
| Architecture, complex | Opus/o1 | 💲💲💲 |

### Session Reset
```
Sau mỗi task độc lập → reset session → tiết kiệm 40-60% tokens/ngày
```

## 7. Anti-Patterns

| ❌ Tránh | ✅ Thay thế |
|---------|------------|
| Dump toàn bộ codebase | Chỉ load files liên quan |
| Chạy 1 phiên cả ngày | Reset mỗi 30-60 phút |
| Paste full error log 500+ dòng | Chỉ error message + top 10 stack |
| System prompt >1000 tokens | ≤500 tokens, skills on-demand |
| Hỏi lại câu đã hỏi | Đọc lại transcript |
| Không dùng subagent | Chia nhỏ, mỗi subagent 1 focus |

## 8. Daily Checklist

```
□ Bắt đầu: Load chỉ lessons + state (Tầng 1-2)
□ Mỗi 10 lượt: Kiểm tra context health  
□ ≥50%: compact với hướng dẫn cụ thể
□ ≥70%: save → phiên mới
□ Task xong: reset session
□ Cuối ngày: save → compact vào progress.md
□ Hàng tuần: review lessons, archive entries cũ
```

## Kết hợp
- `autopilot`: Context manager giám sát context khi autopilot chạy dài
- `daily-reporter`: Context usage stats vào daily report
- `budget-watcher`: Token cost tracking
- `capability-evolver`: Tự tối ưu prompt patterns theo thời gian
