#!/bin/bash
# Facebook Token Daily Healthcheck
# Checks token validity daily at 7AM VN (0:00 UTC)
# Cron: 0 0 * * * /root/openclaw/workspace/scripts/fb-healthcheck.sh

set -euo pipefail

CRED_FILE="/root/openclaw/.openclaw/credentials/fb-credentials.env"
LOG_FILE="/root/openclaw/.openclaw/logs/fb-healthcheck.log"
TELEGRAM_BOT_TOKEN="8755389014:AAGSbrdAoPtGetYuAm4xO_Pv6XMB9gkcyI0"
TELEGRAM_CHAT_ID="882968821"

mkdir -p "$(dirname "$LOG_FILE")"
source "$CRED_FILE"

notify() {
    curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
        -d chat_id="$TELEGRAM_CHAT_ID" -d text="$1" -d parse_mode="Markdown" > /dev/null 2>&1
}

# Check Page Token
RESULT=$(curl -s "https://graph.facebook.com/${FB_GRAPH_API_VERSION}/me?access_token=${FB_PAGE_ACCESS_TOKEN}&fields=name,id" 2>&1)
PAGE_NAME=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('name',''))" 2>/dev/null)

if [ "$PAGE_NAME" = "Tý Tech" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] OK: Page token valid" >> "$LOG_FILE"
    
    # Check User Token expiry
    DEBUG=$(curl -s "https://graph.facebook.com/debug_token?input_token=${FB_USER_ACCESS_TOKEN}&access_token=${FB_APP_ID}|${FB_APP_SECRET}" 2>&1)
    EXPIRES=$(echo "$DEBUG" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('expires_at',0))" 2>/dev/null)
    
    if [ "$EXPIRES" != "0" ] && [ -n "$EXPIRES" ]; then
        NOW=$(date +%s)
        DAYS_LEFT=$(( (EXPIRES - NOW) / 86400 ))
        if [ "$DAYS_LEFT" -lt 7 ]; then
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARNING: User token expires in $DAYS_LEFT days, auto-refreshing..." >> "$LOG_FILE"
            /root/openclaw/workspace/scripts/fb-token-refresh.sh
        fi
    fi
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: Page token invalid!" >> "$LOG_FILE"
    notify "🚨 *FB Healthcheck FAILED*
Page token không hoạt động!
Sếp cần tạo token mới qua Graph API Explorer."
fi
