# Quy tắc làm việc — Sensual Gothic Tarot

## 1. Nguyên tắc số 1: CHỈ SỬA KHI ĐƯỢC YÊU CẦU

- **Không** tự ý vẽ lại, chỉnh sửa hay thay thế bất kỳ lá bài nào trong `cards/`.
- Chỉ tạo/sửa đúng những lá mà người dùng nêu tên trong yêu cầu của họ.
- Không tự đồng bộ, "dọn dẹp" hay ghi đè dữ liệu trong `tarot prompt/` khi chưa được yêu cầu —
  kể cả khi phát hiện dữ liệu lệch nhau. Chỉ **báo cáo** phát hiện đó và chờ quyết định.
- Các file dẫn xuất (`cards/deck.json`, `cards/index.html`, `prompts/out/*`) chỉ regenerate cho
  đúng lá đang được yêu cầu; không commit thay đổi lan sang các lá khác.

## 2. Nguồn dữ liệu chuẩn

| Nội dung | File |
|---|---|
| Độ tuổi, mái tóc, thân hình, huy hiệu, tên lá của 78 lá | `tarot prompt/01-CARD-TABLE.md` ← **bảng chuẩn người dùng chỉ định** |
| Khung nhân vật 72 lá: mắt · tóc · vóc dáng A–D · da · nét riêng · không khí | `tarot prompt/02-CHARACTER-SPECS.md` ← **nguồn chuẩn nhân vật** |
| Mô tả cảnh (`scene`) + khoá số lượng (`count`) | `tarot prompt/cards.json` |
| Quy chuẩn khung **4 lớp — KHÔNG huy hiệu**, template prompt | `tarot prompt/00-MASTER-PROMPT.md`, `tarot prompt/template.md` |
| Chuẩn khung, ánh sáng & bố cục | `cards/17-the-star.png` (Visual Anchor, khung mới) |
| Mẫu khung trống (4 lớp, chưa có nội dung/tên) | `cards/card-blank.png` |

> Ghi chú: `01-CARD-TABLE.md` và `cards.json` hiện lệch nhau ở 33 chỗ (tóc/thân hình của
> `04-emperor`, `05-hierophant`, `09-hermit`, `10-wheel`, `13-death`, `20-judgement`, `21-world`,
> `wands-02`, `wands-04`→`wands-10`, `wands-page`→`wands-king`). **Không tự đồng bộ.**

## 3. Chuẩn kỹ thuật cho mỗi lá bài — KHUNG 4 LỚP, KHÔNG HUY HIỆU

- Kích thước: **784 × 1360** (tỷ lệ 7:12), PNG.
- **4 lớp** (dưới → trên): ① nền giấy da cổ phủ kín lá · ② nội dung **TRÀN VIỀN**
  (mép cảnh chui xuống dưới khung vàng) · ③ khung hoạ tiết **vàng kim metallic, mảnh, sát lề**
  (viền tối + lõi sáng + quầng ấm mảnh — nổi bật nhưng giữ nét mảnh) đè lên nội dung ·
  ④ khung tên: dải băng vàng kim + tên lá chữ Gothic.
- **KHÔNG còn oval medallion / huy hiệu / biểu tượng ở đỉnh** (khung biểu tượng đã bỏ).
- **GỢN MỜ GẦN VẬT THỂ (mọi prompt)**: giữ halo/quầng mềm quanh vật thể (gợn nước quanh bình,
  quầng sáng quanh đèn/nến/vàng, bloom gần sao/lửa) — mượt, khu trú, KHÔNG phải nhiễu/grain.
- **CÁCH DIỄN ĐẠT AN TOÀN (TOÀN BỘ 78 LÁ — chuẩn chính)**: dùng `SAFE_ART_STYLE`
  (OLD-MASTER ALLEGORICAL PAINTING, serene/dignified/museum-quality, non-sexual artistic
  composition, figures wear no cloth — natural elements are their only garment). Không dùng
  "adult classical figure study / unclothed human form / bare skin only" — các cụm này bị
  content-moderation chặn.
- **CÁCH DIỄN ĐẠT THÀNH CÔNG (The Star)**: `STAR_SCENE_LOCK` + `STAR_SKY_RIPPLE_LOCK` trong
  `scripts/build_prompts.py` là nguyên văn đã sinh ra các phương án được chấp nhận (S-curve,
  rót lên cổ, nước trượt da, bình sau lưng khô nghiêng; SKY LOCK 1+7 sao không trăng; RIPPLE
  RULE 2 vùng chỉ ở thân-nước và dòng nước-nước). Không thay đổi lời lẽ khi render lại.
- **THÔNG SỐ CHẤT LƯỢNG (mọi prompt)**: GLOSSY (da bóng dầu vẽ, specular ướt),
  DETAIL siêu chi tiết, **không film grain / noise / speckle / jpeg artifact**,
  SHARPNESS mép sắc, focus tuyệt đối — xem `QUALITY_LOCK` trong `scripts/build_prompts.py`.
- So khung: neo theo `cards/17-the-star.png` — RMSE trên **mask khung dùng chung**
  (`variants/frame-kit/03-frame-thin-clean.png`) ≤ 0.04.
- **Khoá số lượng**: số vật thể (gậy/cốc/kiếm/tiền) trong nội dung phải đúng con số của lá đó.
  Không tin AI đếm — ghép bằng code.

## 4. Công cụ có sẵn

| Script | Việc |
|---|---|
| `scripts/apply_new_frame.py` | Dựng kit 4 lớp (`kit`), mẫu trống (`blank`), mốc The Star (`star`), ghép lá mới (`card`) |
| `scripts/compose_card.py` | Ghép raw art vào khung mới (cover full-bleed, tự vẽ tên) + `--check` RMSE khung |
| `scripts/build_prompts.py` | Sinh prompt từ `cards.json` + `02-CHARACTER-SPECS.md` sang `prompts/out/` |
| `scripts/build_gallery.py` | Sinh lại `cards/deck.json` + `cards/index.html` |
| `scripts/check_card.py` | Kiểm tra kích thước/tỷ lệ |
| `scripts/place_wands.py` | Tách sprite, xoay/scale, ghép **đúng n vật thể** theo hàng |

> `scripts/rebuild_emblem.py`, `set_emblem.py`, `transplant_emblem.py` là công cụ của
> **khung biểu tượng cũ** — không dùng cho khung 4 lớp mới (giữ lại vì lịch sử).

**Quy trình ghép khung mới**: raw art → `compose_card.py` cover-resize 784×1360 →
dán lên nền giấy da cổ → khung hoạ tiết mảnh đè lên → dải băng tên + tên lá Gothic.

## 5. Lịch sử các lá đã sửa

| Lá | Vấn đề | Xử lý |
|---|---|---|
| `wands-03` Three of Wands | Nhân vật ngồi, tóc sai spec | Vẽ lại: đứng, tóc caramel tết dây vàng, đúng 3 gậy |
| `wands-08` Eight of Wands | Nội dung 7 gậy, huy hiệu 9 vạch | Vẽ lại: đúng 8 gậy có chồi lá + huy hiệu đúng 8 vạch |
| Khung toàn bộ | Khung cũ dày, còn medallion biểu tượng | Khung mới 4 lớp: nền tràn viền + khung mảnh sát lề + dải tên; **bỏ khung biểu tượng**; mốc = `17-the-star.png` & `card-blank.png` khung mới |
