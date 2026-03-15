import json, base64, urllib.request, os, urllib.parse
from pathlib import Path
WP_PASS = os.popen("grep -oP 'WP_APP_PASSWORD=\"\\K[^\"]+' /root/openclaw/workspace/wp_credentials.txt").read().strip()
AUTH = base64.b64encode(f'admin:{WP_PASS}'.encode()).decode()
BASE='https://blog.chaiko.info/wp-json/wp/v2'
JSON_HEADERS={'Authorization':'Basic '+AUTH,'Content-Type':'application/json; charset=utf-8'}
AUTH_HEADERS={'Authorization':'Basic '+AUTH}
POST_ID=153

def req_json(url, data=None, method=None, headers=None):
    req=urllib.request.Request(url,data=data,headers=headers or AUTH_HEADERS,method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

def upload(path, filename, mime, title, alt):
    data=Path(path).read_bytes()
    headers={'Authorization':'Basic '+AUTH,'Content-Disposition':f'attachment; filename="{filename}"','Content-Type':mime}
    obj=req_json(f'{BASE}/media', data=data, method='POST', headers=headers)
    meta={'title':title,'alt_text':alt,'caption':f'Nguồn ảnh riêng cho bài 153: {title}'}
    req_json(f"{BASE}/media/{obj['id']}", data=json.dumps(meta, ensure_ascii=False).encode('utf-8'), method='POST', headers=JSON_HEADERS)
    return obj['id']

hero=upload('/root/openclaw/workspace/tmp/nemoclaw-vs-openclaw-images/humanoid-robot.webp','nemoclaw-vs-openclaw-hero.webp','image/webp','Humanoid Robot (CC0)','Robot hình người minh họa cho chủ đề so sánh NemoClaw và OpenClaw')
img2=upload('/root/openclaw/workspace/tmp/nemoclaw-vs-openclaw-images/robot-wireframe.jpg','nemoclaw-vs-openclaw-wireframe.jpg','image/jpeg','Robot wireframe (CC0)','Mô hình robot wireframe minh họa kiến trúc và framework AI agent')
img3=upload('/root/openclaw/workspace/tmp/nemoclaw-vs-openclaw-images/code-on-monitor.jpg','nemoclaw-vs-openclaw-code.jpg','image/jpeg','Code on computer monitor (CC0)','Màn hình code minh họa cho builder và developer dùng OpenClaw')
media=req_json(f'{BASE}/media?include={hero},{img2},{img3}&_fields=id,source_url')
urls={m['id']:m['source_url'] for m in media}
post=req_json(f'{BASE}/posts/{POST_ID}?context=edit')
content=post['content']['raw']
content=content.replace('https://blog.chaiko.info/wp-content/uploads/2026/03/nvidia-nemoclaw-hero-scaled.webp', urls[hero])
content=content.replace('https://blog.chaiko.info/wp-content/uploads/2026/03/nemoclaw-datacenter.jpg', urls[img2])
content=content.replace('https://blog.chaiko.info/wp-content/uploads/2026/03/nemoclaw-supercomputer-scaled.jpg', urls[img3])
payload={'content':content,'featured_media':hero}
req_json(f'{BASE}/posts/{POST_ID}', data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), method='POST', headers=JSON_HEADERS)
verify=req_json(f'{BASE}/posts/{POST_ID}?_fields=id,featured_media,link,title')
print(json.dumps({'hero':hero,'img2':img2,'img3':img3,'urls':urls,'verify':verify}, ensure_ascii=False))
