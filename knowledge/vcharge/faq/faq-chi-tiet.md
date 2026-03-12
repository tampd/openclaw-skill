# FAQ – Câu hỏi thường gặp về Sạc & Ắc quy Vcharge

## A. Câu hỏi chung về sạc xe điện

### A1. Sạc AC và sạc DC khác nhau như thế nào?

**Trả lời**:
- **Sạc AC (Alternating Current)**: Trạm cung cấp dòng điện xoay chiều vào xe, bộ sạc trên xe (OBC – On-Board Charger) sẽ chuyển AC thành DC để nạp vào pin. Công suất thường 7kW–22kW, tốc độ chậm hơn, phù hợp sạc qua đêm tại nhà.
- **Sạc DC (Direct Current)**: Trạm chuyển AC thành DC ngay tại trạm, bơm trực tiếp DC vào pin xe (bỏ qua OBC), công suất cao (50kW–350kW), sạc nhanh trong 20–60 phút. Thường dùng tại trạm công cộng.

### A2. Tại sao xe tôi sạc không đạt đủ công suất ghi trên trạm sạc?

**Trả lời**:
Công suất thực tế bị giới hạn bởi yếu tố nhỏ nhất trong chuỗi:

1. **OBC của xe**: Nếu xe chỉ có OBC 7kW, dù dùng trạm 22kW thì xe vẫn chỉ nhận tối đa 7kW.
2. **Số pha xe hỗ trợ**: OBC 11kW/22kW cần xe hỗ trợ sạc AC 3 pha; nếu xe chỉ hỗ trợ 1 pha thì không tận dụng được.
3. **Trạng thái pin**: Khi pin gần đầy (thường >80%), hệ thống BMS xe tự giảm công suất để bảo vệ pin.
4. **Nhiệt độ**: Pin quá nóng hoặc quá lạnh, OBC sẽ giảm công suất để an toàn.

### A3. Tại sao phải có tiếp địa (PE) khi sạc? Không có PE có sạc được không?

**Trả lời**:
- **Lý do bắt buộc PE**: Khi có rò điện (dây hở, vỏ thiết bị bị điện), dòng rò chạy qua PE xuống đất, kích hoạt RCD/Aptomat ngắt nguồn ngay, tránh điện giật chết người.
- **Không có PE**: Một số bộ sạc di động có tùy chọn tắt bảo vệ tiếp địa ("Not grounded protect") để sạc khẩn cấp, nhưng **RẤT NGUY HIỂM** – nếu rò điện, người chạm vào vỏ sạc hoặc thân xe có thể bị điện giật.
- **Khuyến cáo**: Luôn đảm bảo có PE chuẩn, đặc biệt khi sạc công suất cao (≥7kW) hoặc ngoài trời.

### A4. Sạc 1 pha và 3 pha khác nhau thế nào? Nhà tôi có điện 3 pha không?

**Trả lời**:
- **1 pha (220–240V)**: Hệ thống điện sinh hoạt phổ biến, công suất tối đa khoảng 7kW (32A). Nhà dân thường chỉ có 1 pha.
- **3 pha (380–440V)**: Hệ thống công nghiệp/biệt thự cao cấp, 3 dây pha (L1, L2, L3) + 1 trung tính (N) + 1 đất (PE). Cho phép sạc 11kW–22kW. Ít phổ biến ở chung cư/nhà phố.
- **Cách kiểm tra**: Mở tủ điện, nếu thấy 3 dây pha + 1 trung tính vào Aptomat tổng → có 3 pha. Hoặc gọi thợ điện đo.

### A5. Chứng nhận CE, RoHS, TCVN13078 có nghĩa gì?

**Trả lời**:
- **CE (Conformité Européenne)**: Chứng nhận an toàn theo tiêu chuẩn châu Âu (LVD – điện áp thấp, EMC – tương thích điện từ). Sản phẩm Vcharge đạt CE theo EN 61851-1 (chuẩn sạc EV).
- **RoHS (Restriction of Hazardous Substances)**: Giới hạn chất độc hại (chì, thủy ngân, cadmium…) trong vật liệu điện tử, đảm bảo thân thiện môi trường.
- **TCVN13078**: Tiêu chuẩn Việt Nam về bộ sạc có dây cho xe điện, tương đương IEC 61851-1. VinFast yêu cầu sạc phải tuân thủ chuẩn này.

---

## B. Câu hỏi về Sạc cầm tay di động 7kW (Portable)

### B1. Sạc di động có ưu điểm gì so với sạc treo tường?

**Trả lời**:
- **Ưu điểm**:
  - **Linh hoạt**: Mang theo xe, sạc ở bất kỳ đâu có ổ điện phù hợp (nhà bạn bè, công ty, nhà nghỉ…).
  - **IP65 cao hơn**: Chống nước/bụi tốt hơn Wallbox (IP54), an tâm dùng ngoài trời mưa gió.
  - **Không cần lắp đặt**: Không tốn chi phí thợ, không khoan tường.
- **Nhược điểm**:
  - Cần adapter nếu ổ dân dụng không khớp với phích công nghiệp (Blue CEE…).
  - Không thể điều khiển từ xa qua App như Wallbox (chỉ có màn hình LCD cơ bản).

### B2. Phích cắm Blue CEE là gì? Tại sao không cắm trực tiếp vào ổ thường?

**Trả lời**:
- **Blue CEE (IEC 60309)**: Phích công nghiệp 230V 16A/32A, có khóa xoắn chống rơi, tiếp xúc tốt, chịu được dòng cao liên tục.
- **Ổ dân dụng thường (Schuko/3 chấu)**: Chỉ chịu 10A–16A ngắn hạn, dễ nóng khi sạc 32A liên tục 6–8 tiếng → nguy cơ cháy.
- **Giải pháp**: Lắp ổ Blue CEE riêng cho sạc EV (thợ điện kéo dây từ tủ điện, lắp ổ CEE chuẩn), hoặc dùng adapter (nhưng phải chắc chắn dây adapter chịu được 32A).

### B3. Màn hình hiển thị 2.8 inch trên sạc di động cho xem được gì?

**Trả lời**:
Màn hình LCD 2.8 inch hiển thị:
- Điện áp đầu vào (V).
- Dòng sạc hiện tại (A).
- Công suất (kW).
- Thời gian sạc đã trôi qua.
- Nhiệt độ bộ sạc (°C).
- Trạng thái lỗi (nếu có).

### B4. Đèn đỏ nháy 4 lần liên tục, xe không sạc được – xử lý thế nào?

**Trả lời**:
Đèn đỏ nháy 4 lần = **Lỗi tiếp địa** (không có dây PE hoặc PE kém).

**Cách xử lý**:
1. Kiểm tra ổ điện có 3 chân (L, N, PE) không? Nếu ổ chỉ 2 chân (L, N) → cần lắp PE.
2. Dùng đồng hồ vạn năng đo điện trở từ chân PE của ổ xuống đất thật: phải < 10Ω (tốt nhất < 5Ω). Nếu >100Ω hoặc vô cực → PE giả/hỏng.
3. Kiểm tra dây PE từ tủ điện đến ổ có bị đứt không.
4. Nếu khẩn cấp, một số bộ sạc có tùy chọn "Not grounded protect" (xem HDSD) – tắt bảo vệ PE để sạc, nhưng **không khuyến khích** vì nguy hiểm.

### B5. Sạc di động có chịu được xe cán qua không?

**Trả lời**:
Có, theo thông số kỹ thuật, bộ sạc di động VC-PC32A-B2 chịu được xe tải trọng **2 tấn** cán qua (thử nghiệm trên hộp điều khiển). Tuy nhiên, **không nên cố ý để xe cán** vì:
- Dây cáp có thể bị hư hỏng nội bộ (lõi đồng gãy, cách điện nứt).
- Súng sạc dễ vỡ nếu bị xe cán trúng.

### B6. Tôi có thể điều chỉnh dòng sạc (8A, 16A, 32A…) khi nào?

**Trả lời**:
- **Trước khi cắm súng vào xe**: Dùng nút trên bộ điều khiển để chuyển dòng theo nhu cầu.
- **Trong khi đang sạc**: Nút chuyển dòng bị vô hiệu hóa để đảm bảo an toàn (tránh quá độ đột biến).
- **Khi nào cần giảm dòng**: Khi ổ điện yếu (Aptomat 16A thì chỉ nên sạc ≤13A), hoặc muốn giảm tải cho lưới điện nhà (tránh quá tải khi bật điều hòa + sạc xe cùng lúc).

---

## C. Câu hỏi về Sạc treo tường 7kW, 11kW, 22kW (Wallbox)

### C1. Wallbox có bắt buộc phải lắp bởi thợ điện chuyên nghiệp không?

**Trả lời**:
**Có, bắt buộc**. Lý do:
- Đấu nối sai (L/N đảo, PE không nối, siết lỏng) → cháy nổ, giật điện.
- Cần tính toán tiết diện dây phù hợp với dòng 32A, khoảng cách từ tủ điện đến Wallbox.
- Phải lắp Aptomat/RCBO (bộ bảo vệ rò + quá dòng) phù hợp tại tủ điện.
- Kiểm tra hệ thống tiếp địa chuẩn (điện trở < 10Ω).

Tự lắp sai → mất bảo hành, nguy hiểm tính mạng.

### C2. IP54 của Wallbox có chịu được mưa ngoài trời không?

**Trả lời**:
- **IP54**: Chống bụi mức hạn chế, chống nước bắn từ mọi hướng (mưa tạt nhẹ OK).
- **KHÔNG chịu được**: Ngâm nước, xịt rửa áp lực cao, mưa to kéo dài trực tiếp vào thân sạc.
- **Khuyến cáo**: Lắp dưới mái che, hoặc mua hộp che chống nước chuyên dụng nếu phải lắp ngoài trời hở hoàn toàn.

(Sạc di động IP65 chịu nước tốt hơn, nhưng vẫn nên tránh ngâm nước.)

### C3. Tôi muốn sạc vào ban đêm khi điện rẻ, Wallbox có hẹn giờ được không?

**Trả lời**:
Có, Wallbox Vcharge có chức năng **Time booking (hẹn giờ)**:
- Cài đặt qua nút trên thân sạc hoặc qua App (nếu kết nối Bluetooth/WiFi/4G).
- Ví dụ: Cắm súng vào xe lúc 20h, hẹn bắt đầu sạc lúc 23h (giờ điện thấp điểm), sạc đến 5h sáng.
- Giúp tiết kiệm tiền điện (giá thấp điểm rẻ hơn 30–50% so với cao điểm).

### C4. Thẻ RFID trong Wallbox dùng để làm gì?

**Trả lời**:
Thẻ RFID (Radio-Frequency Identification) dùng để **xác thực người dùng** trước khi sạc:
- **Ứng dụng**: Bãi xe chung cư, công ty, khách sạn – mỗi chủ xe có 1 thẻ riêng, quẹt thẻ mới sạc được.
- **Lợi ích**: Ngăn người lạ dùng trộm điện, quản lý được ai sạc bao nhiêu kWh (nếu kết nối hệ thống giám sát).
- **Chế độ Plug & Play**: Nếu dùng tại nhà riêng, có thể tắt chế độ thẻ, cắm là sạc luôn.

### C5. Wallbox 22kW có tốn điện hơn 7kW không (khi cùng sạc đầy 1 xe)?

**Trả lời**:
**KHÔNG**. Tổng điện năng tiêu thụ (kWh) phụ thuộc vào dung lượng pin xe, không phụ thuộc vào công suất trạm:
- Ví dụ: Pin 60kWh, sạc từ 20% → 80% cần nạp khoảng 36kWh (60 × 60%).
  - Dùng sạc 7kW: mất ~5–6 giờ.
  - Dùng sạc 22kW: mất ~1.5–2 giờ.
  - Cả 2 trường hợp đều tiêu thụ ~36kWh điện, giá tiền như nhau.

**Lưu ý**: Sạc nhanh (22kW) có thể làm pin nóng hơn, BMS xe giảm công suất cuối phiên sạc để bảo vệ → hiệu suất thực tế có thể thấp hơn sạc chậm 1–2%.

### C6. Tôi cần dây điện bao nhiêu tiết diện cho Wallbox 22kW?

**Trả lời**:
Wallbox 22kW, 3 pha, dòng tối đa 32A:

| Khoảng cách (m) | Tiết diện khuyến nghị (mm²) |
|-----------------|------------------------------|
| < 10m | 4 × 6mm² (3L + N + PE) |
| 10–20m | 4 × 10mm² |
| 20–30m | 4 × 16mm² |

(Bảng trên giả định dây đồng, sụt áp cho phép <3%. Nếu dùng dây nhôm hoặc yêu cầu cao hơn, cần tính toán chi tiết bởi kỹ sư điện.)

### C7. Tại sao Wallbox báo lỗi "AC Over-voltage" liên tục vào buổi tối?

**Trả lời**:
**Nguyên nhân**: Điện áp lưới tăng cao (>265Vac cho 1 pha, >460Vac cho 3 pha) do:
- Lưới điện nhà yếu, ban đêm ít tải → điện áp tăng.
- Máy biến áp khu vực chưa điều chỉnh tỷ số biến áp phù hợp.

**Xử lý**:
1. Dùng đồng hồ đo điện áp thực tế (pha-trung tính).
2. Nếu thường xuyên >250V (1 pha): gọi điện lực điều chỉnh máy biến áp, hoặc lắp ổn áp (AVR) cho toàn nhà.
3. Tạm thời: Cấu hình lại ngưỡng bảo vệ quá áp qua phần mềm Wallbox (nếu hỗ trợ), nâng lên 270Vac – nhưng chỉ khi chắc chắn thiết bị chịu được.

### C8. App điều khiển Wallbox là gì? Có bắt buộc phải dùng không?

**Trả lời**:
Tài liệu chỉ ghi "APP control" với kết nối **Bluetooth/WiFi/4G/Ethernet (optional)**, không nêu tên ứng dụng cụ thể (có thể là app Vcharge riêng hoặc nền tảng như Tuya, Smart Life – cần xác nhận với nhà cung cấp).

**Không bắt buộc**: Wallbox vẫn hoạt động độc lập (Plug & Play, hẹn giờ bằng nút). App chỉ thêm tiện ích:
- Xem lịch sử sạc, thống kê kWh.
- Hẹn giờ từ xa.
- Nhận cảnh báo lỗi qua điện thoại.

---

## D. Câu hỏi về Ắc quy LFP Lithium Vcharge

### D1. Ắc quy LFP khác ắc quy chì axit như thế nào?

**Trả lời**:

| Tiêu chí | Ắc quy chì axit | Ắc quy LFP |
|----------|------------------|------------|
| **Tuổi thọ** | 300–500 chu kỳ (~1–2 năm) | >4000 chu kỳ (~5–7 năm) |
| **Trọng lượng** | Nặng (15–20kg cho 60Ah) | Nhẹ hơn 40–50% (6.5kg cho 60Ah) |
| **Điện áp ổn định** | Giảm dần khi dung lượng xuống | Ổn định đến khi cạn bình |
| **Tự xả** | 5–10%/tháng | <3%/tháng |
| **An toàn** | Có axit ăn mòn, thoát khí H₂ | Không axit, không khí độc, khó cháy nổ |
| **Giá** | Thấp (~1–2 triệu) | Cao (~6.5–7.9 triệu) |
| **BMS** | Không | Có – giám sát, cân bằng cell, kết nối App |

### D2. Tại sao ắc quy LFP lại có thể reset lỗi xe bằng App?

**Trả lời**:
- **Nguyên lý**: Ắc quy LFP có BMS (Battery Management System) tích hợp relay điều khiển đầu ra (+/-).
- **Cách hoạt động**:
  - Qua App Bluetooth, bạn tắt "Discharge Switch" → BMS ngắt relay → cọc âm (-) mất kết nối điện → xe mất nguồn hoàn toàn (giống tháo cọc).
  - Bật lại "Discharge Switch" → relay đóng lại → xe được cấp nguồn → ECU xe tự reset như khởi động lại máy tính.
- **Lợi ích**: Không cần mở capo, không cần cờ-lê, không bẩn tay – đặc biệt hữu ích cho xe VinFast hay báo lỗi ảo.

### D3. Tôi thấy "Voldiff" trên App hiển thị 0.15V, có nguy hiểm không?

**Trả lời**:
- **Voldiff (Voltage Difference)**: Chênh lệch điện áp giữa cell cao nhất (Volhigh) và cell thấp nhất (Vollow).
- **Ngưỡng an toàn**:
  - <0.05V: Rất tốt, các cell cân bằng hoàn hảo.
  - 0.05–0.15V: Bình thường, chấp nhận được.
  - 0.15–0.3V: Bắt đầu mất cân bằng, nên chạy chức năng "AutoBalance" trên App.
  - >0.3V: Cần kiểm tra – có thể 1 cell yếu hoặc BMS lỗi.
- **Xử lý**: Vào Control → bật "AutoBalance", để xe đỗ qua đêm (BMS sẽ cân bằng từ từ), sau đó kiểm tra lại Voldiff.

### D4. Ắc quy LFP có sợ nhiệt độ thấp (mùa đông) không?

**Trả lời**:
LFP hoạt động tốt ở nhiệt độ **-20°C đến 60°C**, nhưng:
- **Dưới 0°C**: Dung lượng khả dụng giảm ~10–20% (tạm thời, khi ấm lên sẽ hồi phục), dòng khởi động giảm nhẹ.
- **So với chì axit**: Chì axit giảm dung lượng ~50% ở -20°C, LFP chỉ giảm ~20% → vẫn tốt hơn.
- **Lưu ý Bắc Bộ**: Mùa đông 5–10°C, LFP gần như không bị ảnh hưởng. Chỉ vùng núi cao (Sapa, Mẫu Sơn <0°C) mới cần chú ý.

### D5. Bình LFP 60Ah có dùng cho xe xăng/dầu được không?

**Trả lời**:
**Được**, với điều kiện:
- Kích thước vừa khay bình (230×175×183mm cho 60Ah Vcharge).
- Điện áp 12V (phổ biến cho xe xăng/dầu).
- CCA 800A đủ để khởi động hầu hết xe con (động cơ <2.5L xăng, <2.0L dầu).

**Lợi ích cho xe xăng/dầu**:
- Tuổi thọ lâu (5–7 năm so với 1–2 năm của bình chì).
- Nhẹ hơn → tiết kiệm nhiên liệu nhẹ.
- Ổn định điện áp → âm thanh/đèn xenon hoạt động tốt hơn.

**Lưu ý**: Xe xăng/dầu có máy phát điện (alternator) sạc lại bình trong khi chạy, cần kiểm tra điện áp sạc (thường 13.8–14.4V) không vượt quá 14.6V (ngưỡng an toàn cho LFP). Nếu alternator lỗi, ra điện áp >15V → có thể hỏng BMS.

### D6. Tôi có thể dùng bộ sạc ắc quy chì (12V/10A) để sạc bình LFP không?

**Trả lời**:
**KHÔNG khuyến khích**. Lý do:
- Bộ sạc chì có 3 giai đoạn (Bulk → Absorption → Float), điện áp Float thường 13.5V, không đủ để sạc đầy LFP (cần 14.4–14.6V).
- Không có thuật toán cân bằng cell → LFP dễ mất cân bằng.
- **Nên dùng**: Bộ sạc chuyên dụng cho LiFePO₄ (chế độ 14.6V, không có Float), hoặc để alternator xe tự sạc khi chạy (an toàn hơn).

### D7. Bình LFP 80Ah có cần phải "kích hoạt" trước khi dùng lần đầu không?

**Trả lời**:
**Không cần**. Bình LFP Vcharge xuất xưởng đã được kích hoạt sẵn, sạc đầy ~60–80%.

**Khuyến nghị lần đầu dùng**:
1. Kết nối App, kiểm tra điện áp (nên ~13.0–13.3V cho bình 12V).
2. Lắp vào xe, kiểm tra hoạt động bình thường.
3. Sau 1 tuần, kiểm tra Voldiff – nếu >0.2V, chạy AutoBalance 1 lần.

### D8. Bình LFP có bị "quá xả" không? Xe đỗ lâu có hỏng bình không?

**Trả lời**:
- **BMS bảo vệ quá xả**: Khi điện áp pin xuống ~10V (sắp cạn), BMS tự ngắt đầu ra → xe không nổ máy được, nhưng bình vẫn còn ~5% dung lượng dự trữ.
- **Xe đỗ lâu**: Nếu đỗ >1 tháng không chạy, dòng tự xả + dòng rò của xe (~50mA) có thể khiến bình xuống ngưỡng quá xả.
  - **Xử lý**: Sạc lại bình bằng alternator (chạy xe 30 phút) hoặc bộ sạc chuyên dụng.
  - Nếu để quá 3 tháng không sạc, BMS có thể vào chế độ "deep sleep" (ngủ sâu), cần bộ sạc đặc biệt để "đánh thức" (liên hệ Vcharge hỗ trợ).

### D9. Tại sao phải tháo cọc âm (-) trước khi tháo cọc dương (+)?

**Trả lời**:
**Để tránh chập mạch**:
- Thân xe (khung sắt) nối với cọc âm (-) → "đất" của hệ thống điện.
- Nếu tháo cọc dương (+) trước:
  - Cờ-lê chạm vào thân xe → tạo đường ngắn mạch (+) → (-) qua cờ-lê → tia lửa, cháy cờ-lê, có thể gây cháy nổ khí H₂ (nếu bình chì) hoặc hỏng BMS (nếu bình LFP).
- Nếu tháo cọc âm (-) trước:
  - Cờ-lê chạm thân xe → không sao (vì cả 2 đều là âm).

**Quy tắc an toàn**:
- **Tháo**: Âm (-) trước → Dương (+) sau.
- **Lắp**: Dương (+) trước → Âm (-) sau.

### D10. App Xiaoxiang Electric có phiên bản tiếng Việt không? Có App nào khác thay thế?

**Trả lời**:
- **Xiaoxiang Electric**: App chính thức của BMS JBD, hỗ trợ tiếng Anh (không có tiếng Việt), nhưng giao diện đơn giản, dễ dùng.
- **App thay thế**: Một số BMS JBD tương thích với app khác như "JBD Tools", "Battery Monitor"… (cần kiểm tra compatibility).
- **Hướng dẫn cài đặt**: Quét mã QR trên tem bình hoặc liên hệ Vcharge để được hỗ trợ link tải.

### D11. Xe tôi VF3/VFe34/VF5/VF6/VF7 có dùng được ắc quy 80Ah không?

**Trả lời**:
Không được. Do giới hạn bởi khoang động cơ, các loại xe nhỏ (VF3, VFe34, VF5, VF6, VF7) không có đủ không gian lắp đặt bình 80Ah (kích thước 260 × 175 × 221 mm). Bình 80Ah chỉ phù hợp với VF8, VF9 và các loại xe sang có khoang chứa ắc quy riêng.

### D12. VF3, VF5 lắp bình 60Ah tiêu chuẩn được không?

**Trả lời**:
Được nhưng không nên. Đặc điểm của khoang chứa bình VF3, VF5 có ngàm giữ bình dưới chân, nên lắp đúng loại bình chuyên biệt (60Ah dành riêng cho VF3/VF5) để bình được giữ cố định chắc chắn, đem lại sự an toàn đảm bảo cho xe. Phần dung lượng điện 60Ah thì như nhau, giá như nhau.

---

## E. Câu hỏi chuyên sâu (Kỹ thuật & Xử lý sự cố nâng cao)

### E1. Công thức tính công suất sạc AC 1 pha và 3 pha?

**Trả lời**:
- **1 pha**: P = U × I × cosφ
  - U = 220V (điện áp pha-trung tính), I = dòng (A), cosφ ≈ 0.95–1.0 (hệ số công suất).
  - Ví dụ: 220V × 32A × 0.98 ≈ **6.9kW** (làm tròn 7kW).

- **3 pha**: P = √3 × U × I × cosφ
  - U = 380V (điện áp pha-pha), I = dòng mỗi pha (A).
  - Ví dụ: √3 × 380V × 32A × 0.98 ≈ **20.6kW** (làm tròn 22kW – có loss trên dây).

### E2. Tại sao Wallbox cần Aptomat riêng? Có dùng chung với nhà được không?

**Trả lời**:
**Nên có Aptomat riêng**:
- **Lý do**:
  - Sạc 7kW (32A) chiếm hầu hết dung lượng Aptomat tổng nhà (thường 40A–50A).
  - Nếu cùng lúc bật điều hòa, bếp từ, nước nóng → quá tải → Aptomat nhà nhảy → cả nhà mất điện.
- **Giải pháp**: Kéo dây từ công tơ điện (trước Aptomat tổng nhà) → Aptomat riêng 40A cho Wallbox → Wallbox. Vậy nhà vẫn dùng điện bình thường, Wallbox độc lập.

### E3. RCD Type A và Type B khác nhau gì? Loại nào phù hợp cho sạc EV?

**Trả lời**:
- **RCD Type A**: Phát hiện rò dòng xoay chiều (AC) và dòng một chiều nhấp nháy (pulsating DC).
- **RCD Type B**: Phát hiện thêm dòng một chiều thuần túy (smooth DC) – có thể xuất hiện khi OBC xe bị lỗi.
- **Khuyến nghị**: Dùng **Type B** cho sạc EV (an toàn hơn), nhưng giá cao gấp 3–5 lần Type A.
  - **Giải pháp trung gian**: Dùng Type A kèm thiết bị phát hiện DC (DC fault detector) tích hợp trong Wallbox (Vcharge có tích hợp).

### E4. Làm sao biết OBC xe tôi là bao nhiêu kW?

**Trả lời**:
**Cách 1: Tra catalog xe**:
- VFe34, VF5: OBC 6.6kW (1 pha).
- VF6, VF7: OBC ~6.6–7kW (1 pha).
- VF8, VF9 Eco/Plus: OBC 11kW (3 pha).
- Tesla Model 3 SR+: 11kW; LR/Performance: 11kW (Châu Âu) hoặc 7kW (Mỹ).

**Cách 2: Thực nghiệm**:
- Sạc xe bằng Wallbox 22kW, xem màn hình xe hiển thị công suất thực tế (kW).
- Nếu hiển thị ~6.5–7kW → OBC 7kW.
- Nếu hiển thị ~10.5–11kW → OBC 11kW.

### E5. Hiện tượng "cold gate" (cổng lạnh) trên súng sạc Type 2 là gì?

**Trả lời**:
- **Cold gate**: Chốt khóa cơ trên súng Type 2 bị kẹt do nhiệt độ thấp (<0°C) hoặc bụi bẩn, không rút được súng sau khi sạc xong.
- **Xử lý**:
  - Ấn nút mở khóa trên xe (trong cabin) hoặc súng sạc.
  - Xịt dung dịch bôi trơn (WD-40) vào chốt khóa, đợi 5 phút, thử lại.
  - Nếu vẫn kẹt: gọi Vcharge hỗ trợ (không dùng vũ lực kéo → vỡ súng).

### E6. Sạc ở chung cư, làm sao tính tiền điện riêng cho xe?

**Trả lời**:
**Cách 1: Lắp công tơ con**:
- Kéo dây từ công tơ điện căn hộ → công tơ con (1 pha, 5–40A) → Wallbox.
- Đọc số kWh trên công tơ con mỗi tháng, nhân giá điện → biết xe tiêu thụ bao nhiêu.

**Cách 2: Dùng Wallbox có tính năng đo kWh**:
- Một số Wallbox cao cấp (hoặc kết nối App) ghi log kWh mỗi phiên sạc.
- Export báo cáo cuối tháng.

**Cách 3: Ước tính**:
- Pin xe 60kWh, sạc từ 20% → 80% mỗi tuần: 60 × 60% × 4 tuần = 144kWh/tháng.
- 144kWh × 2.500đ/kWh ≈ 360.000đ/tháng.

### E7. BMS của ắc quy LFP có thể cập nhật firmware không?

**Trả lời**:
- **Phụ thuộc vào BMS**: BMS JBD (dùng trong ắc quy Vcharge) **có hỗ trợ cập nhật firmware** qua App Xiaoxiang Electric (menu Settings → Firmware Update).
- **Khi nào cần cập nhật**:
  - Sửa lỗi BMS (ví dụ: cân bằng cell không chính xác, ngắt quá sớm…).
  - Thêm tính năng mới (ví dụ: tích hợp Bluetooth 5.0, tương thích App mới…).
- **Lưu ý**: Chỉ nên cập nhật khi Vcharge thông báo chính thức (cập nhật lỗi có thể làm "hỏng" BMS).

### E8. Hiện tượng "voltage sag" (sụt áp) khi sạc – nguy hiểm không?

**Trả lời**:
- **Voltage sag**: Khi bật sạc 7kW (32A), điện áp nhà giảm từ 220V xuống ~210V do trở kháng dây dẫn.
- **Ngưỡng an toàn**: Sụt <5% (>209V) là chấp nhận được.
- **Ngưỡng nguy hiểm**: Sụt >10% (<198V) → đèn nhà tối, điều hòa hoạt động yếu, có thể hỏng thiết bị điện tử.
- **Nguyên nhân**: Dây từ tủ điện đến Wallbox quá nhỏ (2.5mm² thay vì 6mm²), hoặc dây quá dài (>30m).
- **Xử lý**: Nâng cấp dây lên 6mm² hoặc 10mm², hoặc giảm dòng sạc xuống 16A–24A.

---

## F. Câu hỏi về Chính sách & Dịch vụ

### F1. Bảo hành 24 tháng cho sạc, 18 tháng cho ắc quy – tính từ khi nào?

**Trả lời**:
- **Sạc (Wallbox/Portable)**: Bảo hành **24 tháng** kể từ ngày giao hàng (theo hóa đơn/phiếu xuất kho).
- **Ắc quy LFP**: Bảo hành **18 tháng** kể từ ngày mua (theo hóa đơn).
- **Lưu ý**: Cần giữ phiếu bảo hành, tem không rách, hóa đơn chứng từ.

### F2. Trường hợp nào bị từ chối bảo hành?

**Trả lời**:
**Đối với sạc (Wallbox/Portable)**:
- Mất phiếu bảo hành, rách tem.
- Sản phẩm ngập nước, rơi vỡ, cháy nổ do thiên tai.
- Lắp đặt sai (đấu sai dây: pha vào trung tính, không tiếp địa…).
- Điện áp không ổn định (thường xuyên quá áp/thấp áp mà không lắp ổn áp).
- Hao mòn tự nhiên (xước xát dây cáp, súng sạc).
- Tự ý tháo dỡ, sửa chữa.

**Đối với ắc quy LFP**:
- Không có hóa đơn/phiếu bảo hành.
- Dùng sai mục đích (nối song song nhiều bình để tăng dung lượng mà không có BMS chính – gây mất cân bằng).
- Sạc bằng bộ sạc không tương thích (quá áp >15V).
- Tự ý mở vỏ BMS, hàn dây vào cell.

### F3. Hotline hỗ trợ kỹ thuật của Vcharge?

**Trả lời**:
- **Hotline tổng đài**: 028 7303 0868
- **Zalo/Hotline kỹ thuật**: 0903 479 389
- **Website**: https://vcharge.vn

### F4. Vcharge có dịch vụ lắp đặt Wallbox tận nhà không?

**Trả lời**:
Vcharge thường cung cấp gói "Lắp đặt trọn gói":
- **Nội dung gói**: Khảo sát, thi công dây điện, lắp Aptomat, lắp Wallbox, vận hành thử.
- **Chi phí**: Tùy khoảng cách dây, độ phức tạp (liên hệ để được báo giá chi tiết).
- **Khuyến nghị**: Liên hệ Vcharge qua hotline để được tư vấn chi tiết.

---

## G. Ghi chú thuật ngữ kỹ thuật tổng hợp

- **kW (kilowatt)**: Đơn vị công suất, 1kW = 1000W.
- **kWh (kilowatt-hour)**: Đơn vị năng lượng, 1kWh = tiêu thụ 1kW trong 1 giờ.
- **A (Ampere)**: Đơn vị dòng điện.
- **V (Volt)**: Đơn vị điện áp.
- **Hz (Hertz)**: Đơn vị tần số, 50Hz = 50 chu kỳ/giây.
- **AC (Alternating Current)**: Dòng điện xoay chiều.
- **DC (Direct Current)**: Dòng điện một chiều.
- **L (Line/Live)**: Dây pha (dây nóng).
- **N (Neutral)**: Dây trung tính (dây lạnh).
- **PE (Protective Earth)**: Dây tiếp địa bảo vệ.
- **IP (Ingress Protection)**: Chuẩn chống bụi/nước, ví dụ IP54, IP65.
- **RCD (Residual Current Device)**: Thiết bị bảo vệ rò điện.
- **RCBO (Residual Current Breaker with Overload)**: RCD + Aptomat quá tải.
- **OBC (On-Board Charger)**: Bộ sạc AC trên xe.
- **BMS (Battery Management System)**: Hệ thống quản lý pin.
- **CCA (Cold Cranking Amperes)**: Dòng khởi động lạnh.
- **LFP (Lithium Ferrous Phosphate)**: Công nghệ pin lithium sắt phosphat.
- **Ah (Ampere-hour)**: Dung lượng pin.
- **Type 2 (IEC 62196-2)**: Chuẩn súng sạc AC châu Âu.
- **CEE (IEC 60309)**: Chuẩn phích cắm công nghiệp.
