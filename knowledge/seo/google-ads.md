# Google Ads (AdWords) — Kiến thức chuyên sâu

## Cấu trúc tài khoản Google Ads

```
Account
├── Campaign 1 (Search — Brand)
│   ├── Ad Group: Brand Exact
│   └── Ad Group: Brand Broad
├── Campaign 2 (Search — Non-Brand VPS)
│   ├── Ad Group: VPS Giá Rẻ
│   ├── Ad Group: Cloud VPS
│   └── Ad Group: VPS SSD
├── Campaign 3 (Performance Max)
├── Campaign 4 (Display — Remarketing)
└── Campaign 5 (Demand Gen)
```

### Nguyên tắc cấu trúc
1. **Tách Brand vs Non-Brand** campaigns
2. **Nhóm theo sản phẩm/dịch vụ**: VPS, Hosting, Domain, Email, SSL
3. **Ad Group**: 5-20 keywords liên quan chặt, cùng search intent
4. **1 campaign = 1 mục tiêu rõ ràng** (leads, sales, awareness)

---

## Loại Campaign (2025-2026)

### Search Campaigns
- Text ads trên kết quả tìm kiếm Google
- **Responsive Search Ads (RSA)**: cung cấp 15 headlines + 4 descriptions → Google AI mix & match
- Pin headlines quan trọng vào position 1 hoặc 2

### Performance Max (PMax)
- AI-driven, cross-channel (Search, Display, YouTube, Gmail, Maps, Discover)
- Cung cấp: audience signals, creative assets, final URL
- **Tips**: thêm negative keywords (brand exclusions), chia asset groups theo product
- Cần ≥ 15 conversions/30 ngày để AI learn tốt

### AI Max for Search
- Layer AI trên Search campaigns — tự mở rộng keyword reach
- Tự động viết ad copy từ landing page
- **Quan trọng**: review search terms report thường xuyên, thêm negative keywords

### Demand Gen
- Reach users trên YouTube, Gmail, Discover
- Tốt cho awareness & consideration stage
- Creative-heavy: cần video + image assets chất lượng

---

## Bidding Strategies

### Smart Bidding (AI-powered)

| Strategy | Khi nào dùng | Yêu cầu |
|---|---|---|
| **Maximize Conversions** | Muốn nhiều leads/sales nhất | ≥ 15 conversions/30d |
| **Target CPA** | Kiểm soát cost per lead | Set CPA mục tiêu |
| **Maximize Conv. Value** | Sản phẩm giá trị khác nhau | Conversion value tracking |
| **Target ROAS** | ROI-focused campaigns | ≥ 15 conversions + value |

### Manual Bidding
- **Manual CPC**: kiểm soát từng keyword bid — dùng khi mới bắt đầu
- **Enhanced CPC (eCPC)**: manual + AI điều chỉnh ±30%

### Tips
- Bắt đầu Maximize Conversions → khi có data → chuyển Target CPA
- Không thay đổi bid strategy quá thường xuyên (AI cần 2 tuần learning)
- Set cap bid khi dùng Maximize strategies

---

## Quality Score

### 3 Components
1. **Expected CTR**: Google dự đoán ad có được click không
2. **Ad Relevance**: Ad copy khớp với keyword search không
3. **Landing Page Experience**: Trang đích có phù hợp, nhanh, dễ dùng không

### Bảng điểm
| Score | Đánh giá | Hành động |
|---|---|---|
| 1-3 | Kém | Tạm dừng keyword, viết lại ad + LP |
| 4-5 | Dưới trung bình | Cải thiện ad relevance + LP |
| 6 | Trung bình | Tối ưu thêm |
| 7-8 | Tốt | Maintain & scale |
| 9-10 | Xuất sắc | Tăng budget |

### Cách cải thiện
- **Ad Relevance**: keyword trong headline, Dynamic Keyword Insertion
- **CTR**: RSA với nhiều variants, ad extensions, compelling CTA
- **Landing Page**: load < 3s, mobile-friendly, CTA rõ ràng, relevant content
- Tổ chức ad groups thematic (5-15 related keywords)

---

## Ad Extensions (Assets)

| Extension | Mô tả | Bắt buộc? |
|---|---|---|
| **Sitelinks** | Links đến các trang khác | ✅ Rất khuyên |
| **Callouts** | Highlight USPs (Miễn phí SSL, Hỗ trợ 24/7) | ✅ Rất khuyên |
| **Structured Snippets** | Danh sách features | Khuyên dùng |
| **Call** | Số điện thoại click-to-call | Khuyên cho B2C |
| **Location** | Địa chỉ từ GBP | Cho local business |
| **Price** | Bảng giá dịch vụ | Cho E-commerce |
| **Promotion** | Khuyến mãi đang chạy | Khi có promo |
| **Image** | Ảnh sản phẩm | Khuyên dùng |

---

## Conversion Tracking

### Setup bắt buộc
1. Google Ads conversion tag (hoặc GA4 import)
2. Enhanced Conversions: gửi hashed user data → attribution chính xác hơn
3. Offline conversion tracking: import CRM data
4. Google Tag Manager (GTM) cho quản lý tags

### Attribution Models
- **Data-driven** (default, khuyên dùng): Google AI phân bổ credit
- Last click: 100% credit cho click cuối
- First click, Linear, Position-based: legacy — sẽ bị phase out

---

## Negative Keywords

### Mandatory negative keyword list
```
miễn phí, free, crack, torrent, download
tuyển dụng, việc làm, salary
review, reddit, quora (nếu target transactional)
học, tutorial, hướng dẫn (nếu target commercial)
```

### Best practices
- Review Search Terms report hàng tuần
- Shared negative keyword lists cho nhiều campaigns
- Match type: phrase match negative thường đủ

---

## Budget & Optimization

### Budget allocation
- 70% budget → top-performing campaigns
- 20% → testing/new campaigns
- 10% → brand campaigns (bảo vệ thương hiệu)

### Optimization cycle
1. **Daily**: check anomalies (spend spike, CTR drop)
2. **Weekly**: search terms → negative keywords, bid adjustments
3. **Monthly**: creative refresh, budget reallocation, performance review
4. **Quarterly**: strategy review, new campaign ideation
