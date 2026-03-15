# Memory — Bài Học Rút Ra

> Mỗi lần mắc lỗi hoặc được Sếp sửa, Tôm ghi lại để không lặp lại.
> Self-learning: pattern lặp ≥3 lần → tạo rule mới trong BOOT.md

---

### 2026-03-12 — Lesson #001
- **Lỗi**: PEP 668 chặn `pip3 install` trên Python 3.12
- **Nguyên nhân**: Ubuntu 24+ dùng externally-managed-environment
- **Cách fix**: Dùng `pip3 install --break-system-packages [pkg]`
- **Quy tắc**: VPS single-purpose → `--break-system-packages` OK. Multi-purpose → dùng venv.

### 2026-03-12 — Lesson #002
- **Lỗi**: Thêm skill mới nhưng Tôm không nhận diện
- **Nguyên nhân**: OpenClaw lưu `skillsSnapshot` trong session, không hot-reload
- **Cách fix**: User gõ `/reset` trên Telegram
- **Quy tắc**: Mỗi khi thêm/sửa skill → nhắc Sếp `/reset`.

### 2026-03-14 — Lesson #003
- **Lỗi**: Nhắn Telegram cho TrangMin bằng username `@TrangMin` thất bại, dù user đã paired và có session trước đó.
- **Nguyên nhân**: `message` tool không phải lúc nào cũng resolve được username sang numeric chat ID.
- **Cách fix**: Tra session/log/BOOT để lấy Telegram ID số của người đó, rồi gửi bằng dạng `telegram:1077372918`.
- **Quy tắc**: Với user Telegram đã biết/đã paired, ưu tiên lưu và dùng **chat ID số**, không mặc định dùng username.

### 2026-03-15 — Lesson #004
- **Lỗi**: Tái dùng ảnh từ bài blog trước sang bài mới cho tiện.
- **Nguyên nhân**: Ưu tiên tốc độ publish hơn tính độc lập của asset cho từng bài.
- **Cách fix**: Mỗi bài phải có bộ ảnh riêng: đi kiếm ảnh khác, copy về bộ mới, hoặc tự thiết kế; không reuse ảnh bài cũ nếu chưa được Sếp duyệt rõ.
- **Quy tắc**: Publish blog = nội dung riêng + ảnh riêng. Thiếu ảnh riêng thì không publish.
