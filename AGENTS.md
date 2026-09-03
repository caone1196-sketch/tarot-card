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
| Mô tả cảnh (`scene`) + khoá số lượng (`count`) | `tarot prompt/cards.json` |
| Quy chuẩn khung viền, 4 lớp chiều sâu, template prompt | `tarot prompt/00-MASTER-PROMPT.md`, `tarot prompt/template.md` |
| Chuẩn khung viền & ánh sáng | `cards/17-the-star.png` (Visual Anchor) |

> Ghi chú: `01-CARD-TABLE.md` và `cards.json` hiện lệch nhau ở 33 chỗ (tóc/thân hình của
> `04-emperor`, `05-hierophant`, `09-hermit`, `10-wheel`, `13-death`, `20-judgement`, `21-world`,
> `wands-02`, `wands-04`→`wands-10`, `wands-page`→`wands-king`). **Không tự đồng bộ.**

## 3. Chuẩn kỹ thuật cho mỗi lá bài

- Kích thước: **784 × 1360** (tỷ lệ 7:12), PNG.
- Khung viền: neo theo `cards/17-the-star.png` — RMSE dải 60px bên trái phải **≤ 0.04**
  (cách làm hiện tại đạt 0.0000, xem mục 4).
- Huy hiệu ở medallion trên + tên lá trong dải ruy băng dưới phải khớp bảng chuẩn.
- **Khoá số lượng**: số vật thể (gậy/cốc/kiếm/tiền) trong nội dung *và* trên huy hiệu phải đúng
  con số của lá đó. Không tin AI đếm — ghép bằng code.

## 4. Công cụ có sẵn

| Script | Việc |
|---|---|
| `scripts/place_wands.py` | Tách sprite khỏi nền trắng, xoay/scale, ghép **đúng n vật thể** theo hàng |
| `scripts/rebuild_emblem.py` | Vẽ lại huy hiệu medallion với **đúng n vạch** (fit ellipse, inpaint nền plate) |
| `scripts/build_prompts.py` | Sinh prompt từ `cards.json` sang `prompts/out/` |
| `scripts/build_gallery.py` | Sinh lại `cards/deck.json` + `cards/index.html` |
| `scripts/check_card.py` | Kiểm tra kích thước/tỷ lệ |
| `scripts/compose_fullbleed.py` | Ghép lá **full-bleed** theo họ khung The Star: cảnh 784×1360 + **mực viền vàng tách bằng code từ lá neo** (nét kẻ ±1 px + hoa văn 4 góc dính nét kẻ → ink_iou ≈ 1.0) + tên lá (tách từ lá neo nếu trùng tên, nếu không thì vẽ bằng `variants/fonts/CinzelDecorative-*.ttf`). `--dump-layers DIR` để xem 3 lớp rời |

**Quy trình neo khung** (giữ nội dung của lá mới, lấy khung từ chuẩn): dựng mask "khung dùng chung"
bằng phương sai pixel của ~10 lá đã đạt chuẩn, chừa vùng nội dung + huy hiệu + tên lá, rồi blend.

## 5. Lịch sử các lá đã sửa

| Lá | Vấn đề | Xử lý |
|---|---|---|
| `wands-03` Three of Wands | Nhân vật ngồi, tóc sai spec | Vẽ lại: đứng, tóc caramel tết dây vàng, đúng 3 gậy |
| `wands-08` Eight of Wands | Nội dung 7 gậy, huy hiệu 9 vạch | Vẽ lại: đúng 8 gậy có chồi lá + huy hiệu đúng 8 vạch |
| `17-the-star` The Star (2026-09-03) | Người dùng yêu cầu tạo lại lá; bản cũ tay phải đỡ bình bằng 2 tay ở lần vẽ A (loại), lần vẽ B sinh **8 sao nhỏ** thay vì 7 | Vẽ cảnh full-bleed từ `scene`/`hair`/`age`/`build`/`count` **nguyên văn `cards.json`** (chỉ thay `a nude woman` → khoác lụa mỏng ướt, ghi trong `cards/_regen/17-the-star.sent.txt`); **xoá 1 sao thừa bằng `seamlessClone`** → đúng 1 sao lớn 8 cánh + 7 sao nhỏ (đếm bằng code); ghép khung + chữ THE STAR tách từ chính lá neo bằng `compose_fullbleed.py` → `ink_iou` 0.997, đúng 2 bình mỗi tay một bình. Bản cũ: `git show 7825551:cards/17-the-star.png` |
