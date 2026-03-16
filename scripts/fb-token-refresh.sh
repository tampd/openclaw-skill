#!/bin/bash
# Facebook Token Refresh Script for Tý Tech Fanpage
# Refreshes the Long-Lived User Token (60-day cycle)
# Page Token derived from it is never-expiring
# Cron: 0 9 */50 * * /root/openclaw/workspace/scripts/fb-token-refresh.sh

set -euo pipefail

CRED_FILE="/root/openclaw/.openclaw/credentials/fb-credentials.env"
LOG_FILE="/root/openclaw/.openclaw/logs/fb-token-refresh.log"
TELEGRAM_BOT_TOKEN="8755389014:AAGSbrdAoPtGetYuAm4xO_Pv6XMB9gkcyI0"
TELEGRAM_CHAT_ID="882968821"

mkdir -p "$(dirname "$LOG_FILE")"
source "$CRED_FILE"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"; }
notify() {
    curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
        -d chat_id="$TELEGRAM_CHAT_ID" -d text="$1" -d parse_mode="Markdown" > /dev/null 2>&1
}

log "Starting token refresh..."

# Step 1: Exchange current long-lived user token for a new one
RESPONSE=$(curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/oauth/access_token?\
grant_type=fb_exchange_token&\
client_id=${FB_APP_ID}&\
client_secret=${FB_APP_SECRET}&\
fb_exchange_token=${FB_USER_ACCESS_TOKEN}")

NEW_USER_TOKEN=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('access_token',''))" 2>/dev/null)

if [ -z "$NEW_USER_TOKEN" ]; then
    ERROR_MSG=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('error',{}).get('message','Unknown error'))" 2>/dev/null)
    log "ERROR: Failed to refresh user token: $ERROR_MSG"
    notify "⚠️ *FB Token Refresh FAILED*
Error: $ERROR_MSG
Sếp cần tạo token mới qua Graph API Explorer."
    exit 1
fi

# Step 2: Get new page access token
NEW_PAGE_TOKEN=$(curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/me/accounts?access_token=${NEW_USER_TOKEN}" | \
    python3 -c "
import sys, json
data = json.load(sys.stdin)
for page in data.get('data', []):
    if page.get('id') == '${FB_PAGE_ID}':
        print(page.get('access_token', ''))
        break
" 2>/dev/null)

if [ -z "$NEW_PAGE_TOKEN" ]; then
    log "ERROR: Failed to get page token"
    notify "⚠️ *FB Token Refresh FAILED*
Không lấy được Page token. Sếp kiểm tra quyền truy cập fanpage."
    exit 1
fi

# Step 3: Backup & update
cp "$CRED_FILE" "${CRED_FILE}.bak"
sed -i "s|^FB_USER_ACCESS_TOKEN=.*|FB_USER_ACCESS_TOKEN=${NEW_USER_TOKEN}|" "$CRED_FILE"
sed -i "s|^FB_PAGE_ACCESS_TOKEN=.*|FB_PAGE_ACCESS_TOKEN=${NEW_PAGE_TOKEN}|" "$CRED_FILE"

# Step 4: Verify
PAGE_NAME=$(curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/${FB_PAGE_ID}?access_token=${NEW_PAGE_TOKEN}&fields=name" | \
    python3 -c "import sys,json; print(json.load(sys.stdin).get('name',''))" 2>/dev/null)

if [ "$PAGE_NAME" = "Tý Tech" ]; then
    log "SUCCESS: Tokens refreshed. Page verified: $PAGE_NAME"
    notify "✅ *FB Token Refreshed*
Page: Tý Tech
Next refresh: ~50 days"
else
    log "WARNING: Token refreshed but verification failed"
    notify "⚠️ *FB Token Refreshed* nhưng verify failed. Sếp check nhé."
fi
