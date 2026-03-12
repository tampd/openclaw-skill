---
name: security-audit
description: Kiểm tra bảo mật skill OpenClaw trước khi cài đặt — quét mã độc, phân tích quyền, đánh giá rủi ro.
---

# Security Audit — Aegis

## Mục đích
Quét và đánh giá bảo mật skill OpenClaw trước khi cài đặt — phát hiện mã độc, quyền nguy hiểm, data exfiltration.

## Khi nào kích hoạt
- Trước khi cài skill mới từ ClawHub hoặc GitHub
- User nói: "scan skill", "kiểm tra bảo mật", "audit", "an toàn không?"
- Khi review SKILL.md từ community

## Setup (1 lần)
```bash
pip3 install --break-system-packages aegis-audit
```

## Sử dụng
```bash
# Scan skill cụ thể (OFFLINE — không gửi data ra ngoài)
aegis scan /root/openclaw/workspace/skills/<skill-name> --no-llm

# Scan với LLM analysis (gửi code tới Gemini để phân tích sâu)
GEMINI_API_KEY=$GEMINI_API_KEY aegis scan /root/openclaw/workspace/skills/<skill-name>

# Scan tất cả skills hiện có
for skill in /root/openclaw/workspace/skills/*/; do
  echo "=== $(basename $skill) ==="
  aegis scan "$skill" --no-llm --json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'Risk: {d.get(\"risk_score\",\"?\")}/100')" 2>/dev/null || echo "Skip"
done

# Tạo lockfile (snapshot bảo mật)
aegis lock /root/openclaw/workspace/skills/<skill-name>

# Verify lockfile (kiểm tra có bị thay đổi không)
aegis verify /root/openclaw/workspace/skills/<skill-name>
```

## Quy trình cài skill mới
1. Download/copy SKILL.md vào `workspace/skills/<name>/`
2. Chạy `aegis scan` → kiểm tra risk score
3. Risk ≤ 30: ✅ Safe — cài được
4. Risk 31-60: ⚠️ Review thủ công — hỏi Sếp
5. Risk > 60: 🔴 Nguy hiểm — KHÔNG cài

## Những gì Aegis quét
- File system access (đọc/ghi file ngoài workspace)
- Network calls (URLs, hosts, ports)
- Shell commands (exec, subprocess)
- Data exfiltration patterns
- Obfuscated code
- Dependency injection

## Quy tắc
- ✅ LUÔN scan trước khi cài skill community
- ✅ Default `--no-llm` (offline, không leak code)
- ❌ KHÔNG cài skill có risk > 60 mà chưa review
