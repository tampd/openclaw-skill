import json, base64, urllib.request, os
from pathlib import Path

WP_PASS = os.popen("grep -oP 'WP_APP_PASSWORD=\"\\K[^\"]+' /root/openclaw/workspace/wp_credentials.txt").read().strip()
AUTH = base64.b64encode(f'admin:{WP_PASS}'.encode()).decode()
BASE = 'https://blog.chaiko.info/wp-json/wp/v2'
JSON_HEADERS = {'Authorization': 'Basic ' + AUTH, 'Content-Type': 'application/json; charset=utf-8'}
AUTH_HEADERS = {'Authorization': 'Basic ' + AUTH}
POST_ID = 148

def req_json(url, data=None, method=None, headers=None):
    h = headers or AUTH_HEADERS
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

def upload_media(path, filename, mime, title, alt):
    data = Path(path).read_bytes()
    headers = {
        'Authorization': 'Basic ' + AUTH,
        'Content-Disposition': f'attachment; filename="{filename}"',
        'Content-Type': mime,
    }
    obj = req_json(f'{BASE}/media', data=data, method='POST', headers=headers)
    meta = {'title': title, 'alt_text': alt, 'caption': f'Nguồn ảnh mở: {title}'}
    req_json(f"{BASE}/media/{obj['id']}", data=json.dumps(meta, ensure_ascii=False).encode('utf-8'), method='POST', headers=JSON_HEADERS)
    return obj['id']

hero_id = upload_media('/root/openclaw/workspace/tmp/nemoclaw-images/nvidia-gpu-workstation.webp', 'nvidia-nemoclaw-hero.webp', 'image/webp', 'NVIDIA GPU workstation (CC0)', 'Máy trạm GPU NVIDIA minh họa cho nền tảng AI agent NemoClaw')
img2_id = upload_media('/root/openclaw/workspace/tmp/nemoclaw-images/datacenter.jpg', 'nemoclaw-datacenter.jpg', 'image/jpeg', 'Datacenter rack (public domain)', 'Tủ máy chủ trong datacenter minh họa cho hạ tầng chạy AI agent doanh nghiệp')
img3_id = upload_media('/root/openclaw/workspace/tmp/nemoclaw-images/supercomputer.jpg', 'nemoclaw-supercomputer.jpg', 'image/jpeg', 'Supercomputer (public domain)', 'Siêu máy tính minh họa cho lớp tính toán phía sau các hệ thống AI agent')

media = req_json(f'{BASE}/media?include={hero_id},{img2_id},{img3_id}&_fields=id,source_url')
url_map = {m['id']: m['source_url'] for m in media}

html = f'''<article>
<h1>NVIDIA NemoClaw là gì? Cách hiểu đơn giản về nền tảng AI agent mới của NVIDIA</h1>
<p><strong>Nói ngắn gọn:</strong> NemoClaw là bộ công cụ để doanh nghiệp tạo ra các AI agent biết làm việc theo nhiều bước, thay vì chỉ trả lời vài câu chat rồi đứng hình.</p>
<figure><img src="{url_map[hero_id]}" alt="Máy trạm GPU NVIDIA minh họa cho nền tảng AI agent NemoClaw" /><figcaption>Ảnh minh họa: GPU workstation dùng để hình dung lớp hạ tầng phía sau các hệ thống AI agent.</figcaption></figure>
<p>Nếu nói theo cách dễ hiểu, <strong>NemoClaw</strong> giống như một “bộ khung làm việc” để công ty tạo ra trợ lý AI nội bộ. Trợ lý này không chỉ biết trả lời, mà còn có thể <strong>đọc thông tin, nhớ ngữ cảnh, dùng công cụ và xử lý một chuỗi việc</strong> như tra cứu tài liệu, tổng hợp báo cáo, hỗ trợ khách hàng hoặc hỗ trợ đội kỹ thuật.</p>
<p>Vì vậy, điều đáng chú ý ở đây không phải là NVIDIA ra thêm một mô hình AI mới. Cái đáng chú ý là họ đang muốn cung cấp <strong>cả nền tảng để biến AI thành người phụ việc thật sự</strong>.</p>

<h2>NemoClaw là gì, hiểu đơn giản nhất?</h2>
<p>Hãy tưởng tượng doanh nghiệp có một nhân viên ảo. Người này có thể:</p>
<ul>
<li>đọc tài liệu nội bộ,</li>
<li>tra cứu thông tin từ nhiều nguồn,</li>
<li>gọi API hoặc dùng công cụ có sẵn,</li>
<li>làm việc theo từng bước thay vì trả lời một lần rồi thôi.</li>
</ul>
<p><strong>NemoClaw</strong> là nền tảng để xây kiểu nhân viên ảo đó. Nó không chỉ là chatbot. Nó hướng tới thứ mà thị trường đang gọi là <strong>AI agent</strong> — tức AI có thể nhận mục tiêu, tự chia nhỏ việc và cố gắng hoàn thành công việc.</p>
<p>Ví dụ dễ hình dung:</p>
<ul>
<li><strong>Chăm sóc khách hàng:</strong> đọc ticket, tìm bài hướng dẫn liên quan, soạn câu trả lời nháp, rồi chuyển cho nhân viên kiểm tra.</li>
<li><strong>Hỗ trợ kỹ thuật:</strong> xem log, gom lỗi giống nhau, đề xuất hướng xử lý ban đầu.</li>
<li><strong>Nghiên cứu nội bộ:</strong> đọc nhiều tài liệu, rút ý chính, tạo báo cáo ngắn cho sếp.</li>
</ul>

<h2>Vì sao NVIDIA lại làm NemoClaw?</h2>
<p>Trước giờ nhiều người nghĩ NVIDIA chỉ mạnh ở GPU. Nhưng làn sóng AI mới khiến hãng này có lý do để đi xa hơn phần cứng. Nếu chỉ bán chip, NVIDIA mới thắng ở lớp dưới. Nếu họ còn có thêm mô hình, công cụ triển khai và nền tảng agent, họ sẽ chen được lên lớp trên của thị trường.</p>
<p>Nói dễ hiểu: <strong>NVIDIA không muốn chỉ bán động cơ, họ muốn bán luôn cả chiếc xe</strong>.</p>
<p>Đó là lý do NemoClaw được nhắc đến như một bước đi chiến lược trong dịp <a href="https://blogs.nvidia.com/blog/gtc-2026-news/" target="_blank" rel="noopener">GTC 2026</a>. Thông điệp khá rõ: AI sắp không còn chỉ là chuyện chat cho vui. Nó đang được đẩy sang giai đoạn “làm việc thật”.</p>

<h2>Điểm hay của NemoClaw nằm ở đâu?</h2>
<h3>1. Không chỉ chat, mà hướng tới làm việc nhiều bước</h3>
<p>Khác với chatbot thông thường, AI agent cần biết giữ mục tiêu lâu hơn, làm từng bước và phối hợp với công cụ. Đây là điểm khiến NemoClaw hấp dẫn với doanh nghiệp.</p>

<h3>2. Quan tâm đến bảo mật và quyền kiểm soát</h3>
<p>Doanh nghiệp rất ngại đưa dữ liệu nội bộ cho AI mà không kiểm soát được. Vì vậy nếu một nền tảng agent có sẵn lớp bảo mật, xác thực và quản trị quyền, nó sẽ dễ được chấp nhận hơn rất nhiều.</p>

<h3>3. Có thể chạy trên nhiều loại hạ tầng</h3>
<p>Theo các thông tin hiện có, NemoClaw được định hướng theo kiểu linh hoạt hơn về hạ tầng. Điều này quan trọng vì công ty nào cũng sợ bị khóa chặt vào một nền tảng duy nhất.</p>

<figure><img src="{url_map[img2_id]}" alt="Tủ máy chủ trong datacenter minh họa cho hạ tầng chạy AI agent doanh nghiệp" /><figcaption>AI agent doanh nghiệp muốn chạy ổn thì vẫn cần hạ tầng, giám sát và kiểm soát vận hành phía sau.</figcaption></figure>

<h2>Nemotron 3 Super liên quan gì tới NemoClaw?</h2>
<p>Đây là chỗ nhiều người dễ rối, nên nói ngắn gọn thế này:</p>
<ul>
<li><strong>NemoClaw</strong> là nền tảng / bộ khung để xây AI agent.</li>
<li><strong>Nemotron 3 Super</strong> là một mô hình AI có thể đóng vai “bộ não” cho agent đó.</li>
</ul>
<p>NVIDIA mô tả <a href="https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/" target="_blank" rel="noopener">Nemotron 3 Super</a> là model mở có 120B tham số tổng, 12B active parameters và context window lên tới 1 triệu token. Nghe kỹ thuật thì hơi nặng, nhưng ý nghĩa thực tế lại khá đơn giản:</p>
<ul>
<li>agent có thể đọc được nhiều dữ liệu hơn trong một lần,</li>
<li>đỡ quên ngữ cảnh khi làm việc dài,</li>
<li>phù hợp hơn với các tác vụ kiểu nghiên cứu, code, phân tích log hoặc xử lý nhiều tài liệu.</li>
</ul>
<p>Nếu ví NemoClaw là “bộ khung công việc”, thì Nemotron 3 Super là “động cơ” mạnh để cái bộ khung đó chạy được mượt hơn.</p>

<figure><img src="{url_map[img3_id]}" alt="Siêu máy tính minh họa cho lớp tính toán phía sau các hệ thống AI agent" /><figcaption>Mô hình mạnh hơn không có nghĩa tự động tốt hơn, nhưng nó giúp AI agent giữ ngữ cảnh và xử lý việc dài hơi tốt hơn.</figcaption></figure>

<h2>Người bình thường nên quan tâm NemoClaw ở điểm nào?</h2>
<p>Không phải ai cũng cần đọc sâu về kiến trúc model. Nhưng anh vẫn nên để ý NemoClaw vì nó cho thấy một xu hướng rất rõ: <strong>AI đang chuyển từ công cụ trả lời sang công cụ làm việc</strong>.</p>
<p>Điều này ảnh hưởng trực tiếp tới:</p>
<ul>
<li><strong>chủ doanh nghiệp nhỏ:</strong> có thể dùng AI để hỗ trợ chăm sóc khách, tổng hợp dữ liệu, hoặc tự động hóa việc lặp lại;</li>
<li><strong>dev và dân IT:</strong> sẽ phải làm quen với việc xây agent, cấp quyền cho agent, giám sát agent;</li>
<li><strong>người làm nội dung / vận hành:</strong> AI sẽ dần xử lý được nhiều phần việc nền hơn trước.</li>
</ul>
<p>Nói dễ hiểu: trước đây AI giống người trả lời tin nhắn. Sắp tới, AI sẽ giống một cộng sự biết cầm checklist và chạy việc.</p>

<h2>NemoClaw có phải thứ sẽ thay đổi cuộc chơi ngay lập tức không?</h2>
<p>Chưa chắc ngay lập tức. Nhiều nền tảng AI công bố rất hoành tráng nhưng khi triển khai thật lại vướng chi phí, bảo mật, tích hợp hệ thống hoặc trải nghiệm chưa mượt.</p>
<p>Tuy nhiên, <strong>NemoClaw đáng theo dõi</strong> vì nó hội tụ 3 thứ quan trọng:</p>
<ul>
<li>NVIDIA có hạ tầng mạnh,</li>
<li>có model mở đi kèm,</li>
<li>và có động lực kéo doanh nghiệp lên một kiểu stack AI mới.</li>
</ul>
<p>Với người làm công nghệ, đây là keyword nên nhớ trong năm 2026. Với người mới tìm hiểu AI, đây là ví dụ rất rõ cho thấy thị trường đang đi theo hướng nào.</p>

<h2>Kết luận</h2>
<p><strong>NVIDIA NemoClaw</strong> có thể hiểu đơn giản là một nền tảng giúp doanh nghiệp tạo ra AI agent biết làm việc theo quy trình, thay vì chỉ chat cho có. Còn <strong>Nemotron 3 Super</strong> là một trong những model phía dưới giúp agent xử lý tác vụ dài và nặng tốt hơn.</p>
<p>Nếu anh chỉ cần nhớ một câu, thì là câu này: <strong>NemoClaw cho thấy AI đang tiến từ “biết nói” sang “biết làm”</strong>.</p>
<p>Xem thêm các bài liên quan trên Chaiko Tech Blog:</p>
<ul>
<li><a href="https://blog.chaiko.info/mcp-la-gi-ai-coding-agents-2026/">MCP là gì? Vì sao 2026 là năm bùng nổ AI coding agents</a></li>
<li><a href="https://blog.chaiko.info/agentic-ai-2026-ky-nguyen-ai-tu-hanh/">Agentic AI 2026: Kỷ nguyên AI tự hành</a></li>
<li><a href="https://blog.chaiko.info/open-source-vs-closed-llm-doanh-nghiep-2026/">Open-source vs. Closed AI 2026</a></li>
</ul>

<h2>FAQ về NemoClaw</h2>
<h3>NemoClaw có phải chatbot không?</h3>
<p>Không hẳn. Nó hướng tới AI agent, tức AI có thể làm việc theo nhiều bước, dùng công cụ và giữ ngữ cảnh lâu hơn chatbot thường.</p>
<h3>Nemotron 3 Super có phải chính là NemoClaw không?</h3>
<p>Không. Nemotron 3 Super là model, còn NemoClaw là nền tảng để xây agent.</p>
<h3>Doanh nghiệp nhỏ có nên quan tâm không?</h3>
<p>Có. Dù chưa cần dùng ngay, việc theo dõi các nền tảng như NemoClaw giúp nhìn rõ AI sẽ đi vào công việc thực tế như thế nào trong 1-2 năm tới.</p>
</article>'''

payload = {
    'title': 'NVIDIA NemoClaw là gì? Cách hiểu đơn giản về nền tảng AI agent mới của NVIDIA',
    'content': html,
    'excerpt': 'NVIDIA NemoClaw là nền tảng giúp doanh nghiệp tạo AI agent biết làm việc nhiều bước. Bài này giải thích đơn giản, dễ hiểu và gần gũi hơn.',
    'featured_media': hero_id,
    'slug': 'nvidia-nemoclaw-ai-agent',
}
update = req_json(f'{BASE}/posts/{POST_ID}', data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), method='POST', headers=JSON_HEADERS)
verify = req_json(f'{BASE}/posts/{POST_ID}?_fields=id,title,status,featured_media,slug,link,excerpt,categories,tags')
print(json.dumps({'hero_id': hero_id, 'img2_id': img2_id, 'img3_id': img3_id, 'update_title': update['title']['rendered'], 'verify': verify, 'media_urls': url_map}, ensure_ascii=False))
