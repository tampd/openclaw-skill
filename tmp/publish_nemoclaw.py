import json, base64, urllib.request, urllib.parse, os
from pathlib import Path

WP_PASS = os.popen("grep -oP 'WP_APP_PASSWORD=\"\\K[^\"]+' /root/openclaw/workspace/wp_credentials.txt").read().strip()
AUTH = base64.b64encode(f'admin:{WP_PASS}'.encode()).decode()
BASE_HEADERS = {'Authorization': 'Basic ' + AUTH}
JSON_HEADERS = {'Authorization': 'Basic ' + AUTH, 'Content-Type': 'application/json; charset=utf-8'}
BASE = 'https://blog.chaiko.info/wp-json/wp/v2'

def get_json(url):
    req = urllib.request.Request(url, headers=BASE_HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

def post_json(url, payload):
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=JSON_HEADERS, method='POST')
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

# duplicate check
existing = get_json(f"{BASE}/posts?search=NemoClaw&_fields=id,title,status,slug,date")
exact_slug = [p for p in existing if p.get('slug') == 'nvidia-nemoclaw-ai-agent']
if exact_slug:
    print(json.dumps({'duplicate': True, 'existing': exact_slug}, ensure_ascii=False))
    raise SystemExit(0)

html = Path('/root/openclaw/workspace/tmp/nemoclaw-post.html').read_text(encoding='utf-8')

tag_specs = [('NVIDIA','nvidia'),('NemoClaw','nemoclaw'),('AI Agent','ai-agent'),('GTC 2026','gtc-2026'),('Open Source','open-source')]
tag_ids=[]
for name, slug in tag_specs:
    found = get_json(f"{BASE}/tags?search={urllib.parse.quote(slug)}&_fields=id,name,slug")
    tag = next((t for t in found if t['slug'] == slug), None)
    if tag is None:
        tag = post_json(f"{BASE}/tags", {'name': name, 'slug': slug})
    tag_ids.append(tag['id'])

payload = {
    'title': 'NVIDIA NemoClaw là gì? Nền tảng AI agent mã nguồn mở mà dev doanh nghiệp nên theo dõi',
    'content': html,
    'status': 'publish',
    'categories': [2],
    'tags': tag_ids,
    'slug': 'nvidia-nemoclaw-ai-agent',
    'excerpt': 'NVIDIA NemoClaw là nền tảng AI agent mã nguồn mở mới cho doanh nghiệp. Bài viết phân tích GTC 2026, Nemotron 3 Super và vì sao dev nên theo dõi ngay.',
    'author': 1
}
post = post_json(f"{BASE}/posts", payload)
verify = get_json(f"{BASE}/posts/{post['id']}?_fields=id,title,status,categories,tags,slug,link,date")
print(json.dumps({'duplicate': False, 'tag_ids': tag_ids, 'post': post, 'verify': verify}, ensure_ascii=False))
