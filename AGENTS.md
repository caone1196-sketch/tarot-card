# Quy tắc làm việc — Sensual Gothic Tarot

## 1. Nguyên tắc số 1: CHỈ SỬA KHI ĐƯỢC YÊU CẦU

- **Không** tự ý vẽ lại, chỉnh sửa hay thay thế bất kỳ lá bài nào trong `cards/`.
- Chỉ tạo/sửa đúng những lá mà người dùng nêu tên trong yêu cầu của họ.
- Không tự đồng bộ, "dọn dẹp" hay ghi đè dữ liệu trong `tarot prompt/` khi chưa được yêu cầu —
  kể cả khi phát hiện dữ liệu lệch nhau. Chỉ **báo cáo** phát hiện đó và chờ quyết định.
- Các file dẫn xuất (`cards/deck.json`, `cards/index.html`, `prompts/out/*`, `tarot prompt/01-CARD-TABLE.md`,
  `standards/**`) chỉ regenerate cho đúng lá đang được yêu cầu; không commit thay đổi lan sang các lá khác.
 Ngoại lệ: khi người dùng yêu cầu "đồng bộ theo `cards.json` hiện tại" thì regenerate toàn bộ.

## 2. Nguồn dữ liệu chuẩn

| Nội dung | File |
|---|---|
| **NGUỒN DUY NHẤT** cho mọi prompt + mọi dữ liệu lá (78 lá): `n` · `group` · `title` · `emblem` · `scene` · `count` · `age` · `hair` · `build` · `femme` | `tarot prompt/cards.json` ← **đọc-ghi tay ở đây**; **không script nào được sửa file này, và không file nào được ghi đè lên nó** |
| Bảng tra nhanh 78 lá cho người đọc | `tarot prompt/01-CARD-TABLE.md` ← **file DẪN XUẤT sinh từ `cards.json`** bằng `python3 scripts/generate_card_table.py` (đừng sửa tay, sẽ bị ghi đè) |
| Tài liệu đọc thêm — **KHÔNG** phải nguồn pipeline | `tarot prompt/02-CHARACTER-SPECS.md` (72 nhân vật, thang vóc A–D, 10 tông da, mắt · nét riêng · không khí) |
| Quy chuẩn prompt, 4 lớp chiều sâu, template | `tarot prompt/00-MASTER-PROMPT.md`, `tarot prompt/template.md` |
| **CHUẨN KHUNG VIỀN (đo bằng số)** | `standards/17-the-star/standard.json` + `frame-mask.png` — sinh từ `cards/17-the-star.png` **hiện tại** |

> **2026-09-03 (chốt):** `cards.json` là nguồn **duy nhất**. `build_prompts.py` và
> `generate_card_table.py` **không** đọc `01`/`02` để lấy dữ liệu (bộ gộp
> `scripts/card_specs.py` đã bị xoá khỏi repo, còn trong lịch sử git).
>
> `02-CHARACTER-SPECS.md` giữ nguyên làm tài liệu cho người vẽ, và **lệch** `cards.json`:
> 0 chỗ tuổi · **15 chỗ tóc** (02 ghi tóc tết/búi + mũ giáp; `cards.json` đã làm mềm thành tóc xoã)
> · vóc dáng dùng thang A–D thay chuỗi mô tả tự do · 4 trường mà `cards.json` không có
> (mắt · da · nét riêng · không khí) → **không** đi vào prompt.
> Chỉ **báo cáo** lệch, không tự đồng bộ. Muốn thông tin nào của 02 hiện lên ảnh → ghi vào
> `cards.json` trước, rồi chạy lại `build_prompts.py all` + `generate_card_table.py`.

## 3. Chuẩn kỹ thuật cho mỗi lá bài

- Kích thước: **784 × 1360** (tỷ lệ 7:12), PNG.
- **Chuẩn khung = những gì đo được từ `cards/17-the-star.png` hôm nay**, lưu trong
  `standards/17-the-star/standard.json` (không còn con số RMSE tự phong 0.0000 như bản cũ):

  | Chỉ tiêu | Giá trị chuẩn | Ngưỡng đạt |
  |---|---|---|
  | Kiểu viền | `thin-line-art` (nét vàng mảnh, không plate) | — |
  | Độ phủ kim tuyến toàn lá | **11.6 %** | ± 5 % |
  | Nét kẻ đầu tiên | trái `x=18`, trên `y=21` | dải viền ± 6 px |
  | Dải viền (mép trong) | trái 32 · phải 33 · trên 35 · dưới 36 px | ± 6 px |
  | Cửa sổ nội dung | `x0=32 y0=35 x1=751 y1=1324` | — |
  | Đĩa huy hiệu (medallion) | **KHÔNG** | có/không phải khớp |
  | Ruy băng tên lá | **KHÔNG** | có/không phải khớp |
  | **Mực viền chồng khít (IoU)** ← **chỉ số quyết định** | 1.000 | **≥ 0.55** |
  | Vị trí nét kẻ · độ phủ kim tuyến · tương quan cấu trúc · bề rộng dải | (17/20/756/1340 · 11.6 % · 1.000 · 32/33/35/36) | **chỉ tham khảo** — mấy chỉ số này bị màu của bức tranh chi phối (trời ửng vàng → "phủ kim tuyến 63 %"), nên không dùng để phạt |

- **Hiện trạng (2026-09-03, sau batch 1): 4/78 lá ĐẠT chuẩn** (`17-the-star` + `00-fool`, `01-magician`,
  `02-priestess` vừa vẽ lại); 74 lá còn lại vẫn thuộc họ khung cũ và lệch *nhau rất ít*
  (viền gân vàng dày + medallion + ruy băng, phủ kim tuyến 43–92 %).
  Chi tiết: `standards/17-the-star/frame-report.md`. Người dùng đã chốt hướng **vẽ lại theo The Star**,
  3 lá/lượt, bắt đầu từ Ẩn Chính. **Không tự ý sửa ảnh ngoài phạm vi 3 lá được yêu cầu trong lượt.**
- Huy hiệu + tên lá phải khớp `cards.json` (`emblem`, `title`). Với họ khung mới (The Star) thì
  huy hiệu và chữ **vẽ đè lên cảnh**, không đặt trong medallion/ruy băng.
- **Khoá số lượng**: số vật thể (gậy/cốc/kiếm/tiền) trong nội dung *và* trên huy hiệu phải đúng
  con số của lá đó. Không tin AI đếm — ghép bằng code.
  Lưu ý: 16/78 lá **chưa có** `count` trong `cards.json` → prompt của 16 lá này không có `COUNT LOCK`.

## 4. Công cụ có sẵn

| Script | Việc |
|---|---|
| `scripts/build_frame_standard.py` | **Sinh bộ chuẩn khung** từ lá neo (`--anchor`, mặc định 17-the-star) → `standards/<neo>/`; có `--force`, `--copy-anchor` |
| `scripts/check_frame_standard.py` | **QA khung** theo chuẩn: 6 chỉ tiêu/lá, in bảng hoặc `--json`, ghi `frame-report.{json,md}`; exit 1 nếu có lá lệch (dùng được trong CI) |
| `scripts/build_prompts.py` | Sinh prompt **chỉ từ `cards.json`** (`scene`/`count`/`age`/`hair`/`build` nguyên văn) + câu khung theo `standards/17-the-star/standard.json` → `prompts/out/` (`all`, `prompt <slug>`, `check`, `md`) |
| `scripts/build_gallery.py` | Sinh lại `cards/deck.json` + `cards/index.html` từ `cards.json` + ảnh trong `cards/` |
| `scripts/generate_card_table.py` | Sinh lại `tarot prompt/01-CARD-TABLE.md` **từ `cards.json`** |
| `scripts/place_wands.py` | Tách sprite khỏi nền trắng, xoay/scale, ghép **đúng n vật thể** theo hàng |
| `scripts/rebuild_emblem.py` | Vẽ lại huy hiệu medallion với **đúng n vạch** (fit ellipse, inpaint nền plate) |
| `scripts/check_card.py` | Kiểm tra kích thước/tỷ lệ (cần `identify` của ImageMagick) |

**Quy trình neo khung** (giữ nội dung của lá mới, lấy khung từ chuẩn):
`python3 scripts/build_frame_standard.py --force` → `standards/17-the-star/frame-mask.png`
là mask "vùng khung" (trắng = khung, đen = cửa sổ nội dung) — dùng mask này để blend,
không dựng lại mask bằng phương sai mỗi lần.
Muốn đổi lá neo: `python3 scripts/build_frame_standard.py --anchor cards/<slug>.png --out standards/<slug> --force`
rồi `python3 scripts/check_frame_standard.py --standard standards/<slug>/standard.json`.

**Sau khi sửa dữ liệu lá, chạy bộ regenerate:**

```bash
python3 scripts/build_prompts.py all && \
python3 scripts/build_gallery.py && \
python3 scripts/generate_card_table.py && \
python3 scripts/check_frame_standard.py
```

## 5. Lịch sử các lá đã sửa / thay đổi lớn

| Lá / phạm vi | Vấn đề | Xử lý |
|---|---|---|
| `wands-03` Three of Wands | Nhân vật ngồi, tóc sai spec | Vẽ lại: đứng, tóc caramel tết dây vàng, đúng 3 gậy |
| `wands-08` Eight of Wands | Nội dung 7 gậy, huy hiệu 9 vạch | Vẽ lại: đúng 8 gậy có chồi lá + huy hiệu đúng 8 vạch |
| *Chuẩn khung* (2026-09-03) | `AGENTS.md` cũ ghi "RMSE ≤ 0.04, đang đạt 0.0000" nhưng thước đo dải 60px thô khiến **77/78 lá bị báo lỗi** vì nó so cả màu nền | Sinh bộ chuẩn đo được `standards/17-the-star/` + 2 script `build_frame_standard.py` / `check_frame_standard.py`; `app.py` dùng theo; ảnh **không** bị sửa |
| *File dẫn xuất* (2026-09-03) | `prompts/out/*` của 77 lá thiếu `ANATOMY LOCK`; `01-CARD-TABLE.md` là bản diễn giải 72 nhân vật chứ không phải bảng 78 lá | Regenerate `prompts/out/` + `cards/deck.json` + `cards/index.html` + `01-CARD-TABLE.md` theo `cards.json` hiện tại (`deck.json`/`index.html` không đổi byte nào) |
| *Batch 1 — 3 lá Ẩn Chính* (2026-09-03) | Lá cũ dùng khung gân vàng dày + medallion + ruy băng → **lệch chuẩn The Star** (ink_iou 0.49) | Vẽ lại `00-fool`, `01-magician`, `02-priestess` full-bleed theo khung The Star: `ink_iou` 0.645 / 0.912 / 0.925 → **ĐẠT**; `01-magician` đúng COUNT LOCK (cốc · kiếm · 1 gậy · tiền). Bản cũ xem `git show HEAD~1:cards/<slug>.png` |
| *Cảnh mô tả trong `cards.json`* (batch 1) | `scene` của 3 lá trên vẫn ghi khỏa thân (`nude`, `bare`, `draped only`) trong khi ảnh mới vẽ nàng khoác lụa | **ĐÃ CHỐT: giữ nguyên văn bản `cards.json`.** Prompt vẫn emit `scene` nguyên văn; việc khoác lụa/do sáng xử lý ở bước render, không sửa nguồn |
| *Nguồn dữ liệu* (2026-09-03) | Đã thử nối `02-CHARACTER-SPECS.md` làm chuẩn nhân vật → hai nguồn tranh nhau (`02` đè 15 chỗ tóc, `cards.json` là file gốc lại bị ghi đè) | **Thu hồi theo yêu cầu "chỉ sử dụng cards.json"**: xoá `scripts/card_specs.py`, `build_prompts.py` + `generate_card_table.py` đọc đúng một nguồn `cards.json`, regenerate 78 file `prompts/out/*` |
| `scripts/count_wands.py` | Hard-code `root = "<repo>/raw"` + 4 slug → chạy trên fresh clone in `MISSING` cả 4 | **Chưa sửa** — cần bạn quyết (đổi sang argv/`--dir` hay xoá) |
