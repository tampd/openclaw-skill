# Keyword & SEO Tools — Tổng hợp công cụ

## Keyword Research Tools

### Free
| Tool | URL | Điểm mạnh |
|---|---|---|
| Google Keyword Planner | ads.google.com | Chính xác nhất (data từ Google), volume ranges |
| Google Trends | trends.google.com | Xu hướng theo thời gian, so sánh keywords |
| Google Search Suggest | google.com | Autocomplete = real user queries |
| AnswerThePublic | answerthepublic.com | Câu hỏi xoay quanh keyword |
| AlsoAsked | alsoasked.com | "People Also Ask" clusters |
| Ubersuggest (limited) | neilpatel.com/ubersuggest | Keyword ideas + basic SERP analysis |
| Keyword Surfer | Chrome extension | Volume ngay trên SERP |

### Paid/Premium
| Tool | Giá | Điểm mạnh |
|---|---|---|
| **Ahrefs** | $99+/mo | Keyword Explorer, Content Explorer, Backlink Analysis |
| **SEMrush** | $119+/mo | Keyword Magic Tool, Position Tracking, Site Audit |
| **Moz Pro** | $79+/mo | Keyword Explorer, DA/PA, Link Explorer |
| **Mangools (KWFinder)** | $29+/mo | Dễ dùng, SERPChecker, SERPWatcher |
| **SE Ranking** | $39+/mo | Rank tracking, competitor analysis |

---

## Rank Tracking Tools

### Paid
| Tool | Mô tả |
|---|---|
| Ahrefs Rank Tracker | Track positions, SERP features, competitors |
| SEMrush Position Tracking | Daily updates, local tracking, device-specific |
| SERPWatcher (Mangools) | Simple, visual rank tracking |
| AccuRanker | Fast, accurate, API available |

### Open Source (GitHub)
| Tool | GitHub | Mô tả |
|---|---|---|
| **SerpBear** | `nicholasgcoles/SerpBear` | Self-hosted rank tracker, unlimited keywords, GSC integration, email notifications |
| RankTank | `ranktank/keyword-rank-checker` | Python script check rank on Google |
| Open SEO | `every-app/open-seo` | Open-source SEO suite (WIP) |

### SerpBear Setup (self-hosted)
```bash
# Docker compose
docker pull nicholasgcoles/serpbear
docker run -d -p 3000:3000 \
  -e SERPAPI_KEY=your_key \
  -v serpbear_data:/data \
  nicholasgcoles/serpbear
```
- Tích hợp được Google Search Console
- Email notifications khi keyword thay đổi rank
- API endpoint cho automation

---

## Site Audit & Technical SEO Tools

| Tool | URL | Free? | Chức năng chính |
|---|---|---|---|
| Google Search Console | search.google.com/search-console | ✅ | Index, performance, CWV |
| Google PageSpeed Insights | pagespeed.web.dev | ✅ | Core Web Vitals test |
| Google Lighthouse | Chrome DevTools | ✅ | Full audit (SEO, perf, a11y) |
| GTmetrix | gtmetrix.com | ✅ limited | Page speed analysis |
| Screaming Frog | screamingfrog.co.uk | ✅ ≤500 URLs | Crawl full site, find issues |
| Ahrefs Site Audit | ahrefs.com | Paid | Comprehensive technical audit |
| SEMrush Site Audit | semrush.com | Paid | 130+ checks |
| Sitebulb | sitebulb.com | Paid | Visual crawl maps |

---

## Content & On-Page Tools

| Tool | Chức năng | Free? |
|---|---|---|
| Surfer SEO | Content optimization, NLP terms | Paid |
| Clearscope | Content grading, keyword suggestions | Paid |
| MarketMuse | AI content planning & optimization | Paid |
| Yoast SEO | WordPress on-page optimization | Free/Paid |
| RankMath | WordPress SEO plugin | Free/Paid |
| Hemingway Editor | Readability check | Free |
| Grammarly | Grammar & style | Free/Paid |

---

## Backlink Analysis Tools

| Tool | Chức năng |
|---|---|
| Ahrefs Backlink Checker | Largest backlink database, DR/UR metrics |
| Moz Link Explorer | DA/PA, spam score, link quality |
| Majestic | Trust Flow, Citation Flow |
| SEMrush Backlink Analytics | Competitor backlinks, toxic links |
| Google Search Console | Links report (free, limited) |

---

## Vietnamese SEO Tools & Resources

### Cộng đồng SEO Việt Nam
- **SEO Vietnam (Facebook Group)**: 50K+ members, thảo luận SEO tiếng Việt
- **ThichSEO**: Diễn đàn SEO Việt Nam
- **SEOngon**: Blog SEO tiếng Việt chất lượng

### Tools cho thị trường Việt Nam
- **Google Keyword Planner** (location: Vietnam): Chính xác nhất cho VN
- **SimilarWeb**: Phân tích traffic competitor VN
- **Ahrefs** with VN database: Keyword data cho tiếng Việt

### Đặc thù SEO tiếng Việt
- Dấu vs không dấu: Google hiểu nhưng nên tối ưu cho cả hai
- Unicode: tên file/URL nên dùng không dấu
- Local search behavior: người Việt search khác, dùng nhiều câu hỏi dài
- Backlinks VN: báo điện tử, diễn đàn IT, review sites

---

## GitHub Awesome SEO Resources

### Curated Lists
- `serpapi/awesome-seo-tools` — Tổng hợp SEO tools toàn diện
- `awesomelistsio/awesome-seo` — Resources, blogs, tools
- `nicholasgcoles/SerpBear` — Open-source rank tracker
- `joshcarty/google-searchconsole` — Python GSC API wrapper

### Automation Scripts
- `drkwng/google-search-console-api` — Full GSC API Python
- `toghani/Google-keyword-rank-tracker` — Keyword tracking + Google Sheets
- GSC Streamlit dashboard — Visualize GSC data
