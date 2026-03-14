# Google Search Console — Kiến thức chuyên sâu

## Tổng quan

Google Search Console (GSC) là công cụ **miễn phí** của Google giúp:
- Theo dõi hiệu suất website trên Google Search
- Phát hiện và fix lỗi index/crawl
- Submit sitemaps và URLs để index
- Theo dõi Core Web Vitals
- Xem manual actions & security issues

---

## Performance Report (Search Analytics)

### 4 Metrics chính
| Metric | Ý nghĩa | Benchmarks |
|---|---|---|
| **Clicks** | Số lần user click vào kết quả | Càng nhiều càng tốt |
| **Impressions** | Số lần xuất hiện trên SERP | Traffic potential |
| **CTR** | Click / Impressions × 100% | Position 1: 25-35%, Position 2-3: 10-15% |
| **Position** | Thứ hạng trung bình | Target: < 10 (trang 1) |

### CTR Benchmarks theo Position
| Vị trí | CTR trung bình |
|---|---|
| #1 | 27-32% |
| #2 | 15-18% |
| #3 | 10-12% |
| #4-5 | 5-8% |
| #6-10 | 2-5% |
| #11-20 | 1-3% |

### Dimensions phân tích
- **Queries**: keywords nào drive traffic
- **Pages**: trang nào perform tốt nhất
- **Countries**: traffic từ đâu
- **Devices**: mobile vs desktop vs tablet
- **Search Appearance**: rich results, AMP, etc.
- **Dates**: compare periods (MoM, YoY)

### Phân tích chiến lược
1. **Quick wins**: Keywords position 5-15, high impressions, low CTR → optimize title/meta
2. **Content gaps**: Queries có impressions nhưng clicks = 0 → cải thiện content
3. **Cannibalization**: Nhiều pages rank cho cùng keyword → consolidate
4. **Declining pages**: Compare periods → tìm trang đang mất traffic → update content

---

## URL Inspection

### Chức năng
- Kiểm tra URL nào đã được Google index
- Xem cách Googlebot render trang
- Request indexing cho trang mới/updated
- Kiểm tra canonical, mobile usability, structured data

### Troubleshooting
| Status | Ý nghĩa | Fix |
|---|---|---|
| URL is on Google | ✅ Đã index | OK |
| URL is not on Google | ❌ Chưa index | Submit + check robots.txt, canonical |
| Crawled - currently not indexed | ⚠️ Crawled nhưng không index | Improve content quality |
| Discovered - currently not indexed | ⚠️ Biết nhưng chưa crawl | Wait hoặc improve internal linking |
| Page with redirect | Redirect detected | Check redirect chain |
| Soft 404 | Page looks empty | Add real content |

---

## Index Coverage (Pages Report)

### Categories
- **Valid**: Pages đã index bình thường
- **Valid with warnings**: Index nhưng có issues
- **Error**: Không index do lỗi (server error, redirect error, 404)
- **Excluded**: Không index có chủ đích (noindex, canonical, duplicate)

### Common Issues & Fixes
| Issue | Fix |
|---|---|
| Server errors (5xx) | Check server health, fix code bugs |
| Redirect errors | Fix redirect loops, chains |
| Submitted URL has crawl issue | Check robots.txt, server response |
| Duplicate without canonical | Add canonical tag |
| Excluded by noindex tag | Remove noindex nếu muốn index |
| Blocked by robots.txt | Update robots.txt |

---

## Sitemaps

### Submit & Monitor
1. Submit XML sitemap qua GSC → Sitemaps section
2. Monitor: số URLs submitted vs indexed
3. Nếu gap lớn (submitted >> indexed) → quality/crawl issues

### Best practices
- Separate sitemaps: pages, posts, products, images
- Remove URLs trả 404/301 khỏi sitemap
- Auto-update sitemap khi publish/delete content

---

## Core Web Vitals Report

### Trong GSC
- Mobile & Desktop reports riêng
- Categories: Good, Needs Improvement, Poor
- Grouped by type: LCP, INP, CLS
- Click vào group → xem affected URLs

### Fix workflow
1. Identify poor URLs trong GSC
2. Test URL cụ thể qua PageSpeed Insights
3. Fix issues (xem technical-seo.md)
4. Validate fix trong GSC (nút "Validate Fix")
5. Google re-crawl & update (2-4 tuần)

---

## Manual Actions
- Google phạt manual khi vi phạm guidelines
- Common: unnatural links, thin content, user-generated spam, cloaking
- **Check**: GSC → Security & Manual Actions
- **Fix**: Resolve issue → submit Reconsideration Request

---

## GSC API Automation

### Python Script mẫu — Lấy top keywords
```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SERVICE_ACCOUNT_FILE = 'service-account.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('searchconsole', 'v1', credentials=credentials)

request = {
    'startDate': '2026-01-01',
    'endDate': '2026-03-01',
    'dimensions': ['query'],
    'rowLimit': 100
}

response = service.searchanalytics().query(
    siteUrl='https://bkns.vn', body=request).execute()

for row in response.get('rows', []):
    query = row['keys'][0]
    clicks = row['clicks']
    impressions = row['impressions']
    ctr = row['ctr'] * 100
    position = row['position']
    print(f"{query}: clicks={clicks}, imp={impressions}, CTR={ctr:.1f}%, pos={position:.1f}")
```

### GitHub Tools
| Tool | GitHub | Mô tả |
|---|---|---|
| google-searchconsole | `joshcarty/google-searchconsole` | Python wrapper dễ dùng |
| GSC API | `drkwng/google-search-console-api` | Full API: keywords + indexing |
| SerpBear | `nicholasgcoles/SerpBear` | Rank tracker mã nguồn mở |
