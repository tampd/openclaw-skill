#!/bin/bash
# ============================================
# OpenClaw Sales Agent Onboarding Script
# Tự động tạo agent mới cho nhân viên Sales
# ============================================
# Sử dụng:
#   ./onboard-sales-agent.sh <agent-id> <nv-name> <telegram-id> <bot-token>
#
# Ví dụ:
#   ./onboard-sales-agent.sh trang-sales Trang 1077372918 "BOT_TOKEN_HERE"
# ============================================

set -euo pipefail

OPENCLAW_HOME="${OPENCLAW_HOME:-/home/openclaw/openclaw}"
WORKSPACE="${OPENCLAW_HOME}/workspace"
SHARED="${WORKSPACE}/shared"

# Validate arguments
if [ $# -lt 4 ]; then
    echo "❌ Sử dụng: $0 <agent-id> <nv-name> <telegram-id> <bot-token>"
    echo "   Ví dụ:  $0 trang-sales Trang 1077372918 'BOT_TOKEN'"
    exit 1
fi

AGENT_ID="$1"
NV_NAME="$2"
TELEGRAM_ID="$3"
BOT_TOKEN="$4"

echo "🦐 OpenClaw Sales Agent Onboarding"
echo "==================================="
echo "Agent ID:     ${AGENT_ID}"
echo "Tên NV:       ${NV_NAME}"
echo "Telegram ID:  ${TELEGRAM_ID}"
echo ""

# Step 1: Create agent workspace
AGENT_WORKSPACE="${WORKSPACE}/staff/${NV_NAME,,}"
echo "📁 [1/5] Tạo workspace: ${AGENT_WORKSPACE}"
mkdir -p "${AGENT_WORKSPACE}/knowledge"
mkdir -p "${AGENT_WORKSPACE}/memory"
mkdir -p "${AGENT_WORKSPACE}/notes"

# Step 2: Create SOUL.md from template
echo "📝 [2/5] Tạo SOUL.md cho ${NV_NAME}"
sed "s/{{NV_NAME}}/${NV_NAME}/g" "${SHARED}/SOUL-sales-template.md" > "${AGENT_WORKSPACE}/SOUL.md"

# Step 3: Symlink shared knowledge (read-only for NV)
echo "🔗 [3/5] Liên kết shared knowledge"
ln -sfn "${SHARED}/bkns" "${AGENT_WORKSPACE}/shared-bkns"
ln -sfn "${SHARED}/vcharge" "${AGENT_WORKSPACE}/shared-vcharge"

# Step 4: Create welcome note
echo "👋 [4/5] Tạo welcome note"
cat > "${AGENT_WORKSPACE}/knowledge/welcome.md" << WELCOME
# Chào mừng ${NV_NAME} đến với Tôm 🦞

Tôm là trợ lý AI hỗ trợ ${NV_NAME} trong công việc bán hàng tại BKNS.

## Tôm có thể giúp gì?
- 📋 Tra cứu thông tin sản phẩm, bảng giá
- 💡 Tư vấn gói dịch vụ phù hợp cho khách hàng
- 📝 Ghi chú thông tin khách hàng
- 🔄 So sánh các gói dịch vụ
- 📊 Tạo báo giá

## Cách sử dụng
- Gõ tin nhắn bình thường trong Telegram
- Yêu cầu ghi chú: "Ghi nhớ: [nội dung]"
- Hỏi về sản phẩm: "Thông tin VPS Pro" hoặc "So sánh hosting"

## Lưu ý
- Thông tin bảng giá luôn lấy từ nguồn chính thức
- Ghi chú cá nhân chỉ bạn mới thấy được
- Nếu không chắc → hỏi anh Tâm

Ngày tạo: $(date +%Y-%m-%d)
WELCOME

# Step 5: Set permissions
echo "🔒 [5/5] Set quyền truy cập"
chown -R openclaw:openclaw "${AGENT_WORKSPACE}"
chmod -R 700 "${AGENT_WORKSPACE}"

echo ""
echo "✅ Workspace cho ${NV_NAME} đã sẵn sàng!"
echo ""
echo "📌 BƯỚC TIẾP THEO (thực hiện thủ công):"
echo "   1. Thêm agent vào OpenClaw:"
echo "      OPENCLAW_HOME=${OPENCLAW_HOME} openclaw agents add ${AGENT_ID}"
echo ""
echo "   2. Cấu hình binding trong openclaw.json:"
echo '      Thêm vào "channels.telegram.accounts":'
echo "      \"${NV_NAME,,}\": {"
echo "        \"botToken\": \"${BOT_TOKEN}\","
echo "        \"dmPolicy\": \"allowlist\","
echo "        \"allowFrom\": [\"tg:${TELEGRAM_ID}\"]"
echo "      }"
echo ""
echo "   3. Thêm binding:"
echo "      { \"agentId\": \"${AGENT_ID}\", \"match\": {\"channel\":\"telegram\",\"accountId\":\"${NV_NAME,,}\"} }"
echo ""
echo "   4. Restart gateway:"
echo "      sudo systemctl restart openclaw-gateway"
echo ""
echo "   5. Test: Gửi tin nhắn từ Telegram ${NV_NAME} → Bot phản hồi"
