#!/bin/bash
# Wrapper cho gog CLI để tự động attach env vars từ .env

set -a
source /root/openclaw/workspace/.env
set +a

# Nếu không truyền lệnh gì, in ra account hiện tại
if [ $# -eq 0 ]; then
  /usr/local/bin/gog auth list
  exit 0
fi

# Chạy lệnh
/usr/local/bin/gog "$@"
