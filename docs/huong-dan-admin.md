# 🔧 Hướng dẫn Quản trị — OpenClaw Multi-tenant Sales

## Dành cho: Admin (Sếp Tâm)

---

## 1. Kiến trúc hệ thống

```
/home/openclaw/openclaw/          ← OPENCLAW_HOME
├── .openclaw/
│   └── openclaw.json             ← Config chính (có token)
├── workspace/
│   ├── shared/                   ← Knowledge dùng chung (read-only cho NV)
│   │   ├── bkns/
│   │   ├── vcharge/
│   │   └── SOUL-sales-template.md
│   ├── staff/                    ← Workspace riêng mỗi NV
│   │   └── [tên-nv]/
│   │       ├── SOUL.md
│   │       ├── knowledge/
│   │       └── memory/
│   ├── scripts/
│   │   └── onboard-sales-agent.sh  ← Script tự động onboard
│   ├── docs/
│   │   ├── huong-dan-nhan-vien.md
│   │   ├── huong-dan-admin.md
│   │   └── openclaw-config-reference.json
│   └── knowledge/                ← Knowledge riêng Admin
└── api/                          ← API credentials
```

---

## 2. Thêm nhân viên mới

### Bước 1: Tạo Telegram Bot
1. Mở Telegram, tìm **@BotFather**
2. Gửi: `/newbot`
3. Đặt tên: `Tôm BKNS [Tên NV]`
4. Đặt username: `TomBKNS_[TenNV]_bot`
5. Lưu **Bot Token** được @BotFather cung cấp

### Bước 2: Lấy Telegram ID của nhân viên
1. Nhờ NV mở @userinfobot trên Telegram
2. Bot sẽ hiển thị Telegram ID (số)
3. Lưu lại số ID

### Bước 3: Chạy script onboarding
```bash
export OPENCLAW_HOME=/home/openclaw/openclaw
cd $OPENCLAW_HOME/workspace/scripts

# Ví dụ: Thêm NV Trang
./onboard-sales-agent.sh trang-sales Trang 1077372918 "BOT_TOKEN_TỪ_BOTFATHER"
```

### Bước 4: Cấu hình OpenClaw
Mở file config:
```bash
nano $OPENCLAW_HOME/.openclaw/openclaw.json
```

Thêm vào phần `channels.telegram` (thêm `accounts` nếu chưa có):
```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "trang": {
          "botToken": "BOT_TOKEN_TỪ_BOTFATHER",
          "dmPolicy": "allowlist",
          "allowFrom": ["tg:1077372918"]
        }
      }
    }
  },
  "bindings": [
    { "agentId": "trang-sales", "match": {"channel":"telegram","accountId":"trang"} }
  ]
}
```

### Bước 5: Restart service
```bash
sudo systemctl restart openclaw-gateway
```

### Bước 6: Kiểm tra
```bash
# Kiểm tra agent list
OPENCLAW_HOME=/home/openclaw/openclaw openclaw agents list

# Kiểm tra security
OPENCLAW_HOME=/home/openclaw/openclaw openclaw security audit
```

---

## 3. Xóa nhân viên (Offboarding)

```bash
export OPENCLAW_HOME=/home/openclaw/openclaw

# 1. Xóa agent
openclaw agents delete trang-sales

# 2. Xóa bot token khỏi openclaw.json
nano $OPENCLAW_HOME/.openclaw/openclaw.json
# → Xóa account và binding tương ứng

# 3. Backup workspace NV trước khi xóa
cp -r $OPENCLAW_HOME/workspace/staff/trang /backup/trang-$(date +%Y%m%d)

# 4. Xóa workspace NV (tùy chọn)
rm -rf $OPENCLAW_HOME/workspace/staff/trang

# 5. Restart
sudo systemctl restart openclaw-gateway

# 6. Disable bot trên @BotFather
# → Mở @BotFather → /deletebot → chọn bot NV
```

---

## 4. Cập nhật bảng giá / knowledge

```bash
# Sửa shared knowledge (tất cả NV sẽ thấy thay đổi)
nano $OPENCLAW_HOME/workspace/shared/bkns/pricing/[file].md

# Sửa thông tin VCharge
nano $OPENCLAW_HOME/workspace/shared/vcharge/[file].md
```

---

## 5. Monitoring & Bảo trì

### Kiểm tra trạng thái service
```bash
systemctl status openclaw-gateway
journalctl -u openclaw-gateway --no-pager -n 20
```

### Security audit
```bash
OPENCLAW_HOME=/home/openclaw/openclaw openclaw security audit --deep
```

### Backup
```bash
# Push lên GitHub
cd $OPENCLAW_HOME/workspace
git add -A && git commit -m "backup: $(date +%Y-%m-%d)" && git push
```

### Khắc phục sự cố

| Lỗi | Cách xử lý |
|---|---|
| Bot không phản hồi | `systemctl restart openclaw-gateway` |
| Config invalid | `OPENCLAW_HOME=... openclaw doctor --fix` |
| Port đã bị chiếm | `fuser -k 18789/tcp && systemctl start openclaw-gateway` |
| NV thấy data người khác | Kiểm tra workspace path + sandbox config |

---

## 6. Restore từ GitHub

```bash
# 1. Clone repo
git clone git@github.com:tampd/openclaw-skill.git /home/openclaw/openclaw/workspace

# 2. Restore config (cần nhập tokens thủ công)
# Tham khảo: workspace/docs/openclaw-config-reference.json
# → Thay REDACTED_BOT_TOKEN bằng token thật
# → Lưu vào /home/openclaw/openclaw/.openclaw/openclaw.json

# 3. Set permissions
chown -R openclaw:openclaw /home/openclaw/openclaw
chmod 700 /home/openclaw/openclaw/.openclaw
chmod 600 /home/openclaw/openclaw/.openclaw/openclaw.json

# 4. Start service
sudo systemctl start openclaw-gateway
```

---

## 7. Bảo mật

### Đã triển khai (4 lớp)
| Lớp | Mô tả |
|---|---|
| **L1: Identity** | Mỗi NV 1 bot + allowlist Telegram ID |
| **L2: Sandbox** | Docker sandbox (mặc định cho NV agents) |
| **L3: OS** | User `openclaw` non-root, systemd hardened |
| **L4: Systemd** | NoNewPrivileges, ProtectSystem, PrivateTmp |

### Lưu ý bảo mật
- ⚠️ Đây là **multi-agent trên single gateway** — phù hợp cho team tin cậy
- ⚠️ Không phải SaaS multi-tenant thực sự
- 📌 Khi NemoClaw GA → cân nhắc migrate để có enterprise-grade security
