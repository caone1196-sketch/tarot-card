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
| **DỮ LIỆU GỐC của prompt**: `title` · `emblem` · `scene` · `count` (78 lá) | `tarot prompt/cards.json` ← **đọc-ghi tay ở đây**; **không script nào được sửa file này** |
| **CHUẨN THÔNG SỐ NHÂN VẬT** (tuổi · mắt · tóc · vóc A–D · da · nét riêng · không khí) | `tarot prompt/02-CHARACTER-SPECS.md` ← **đọc-ghi tay ở đây**; 72/78 lá (6 lá thuần vật thể không có người) |
| Bảng tra nhanh 78 lá cho người đọc | `tarot prompt/01-CARD-TABLE.md` ← **file DẪN XUẤT** = `cards.json` + `02`, sinh bằng `python3 scripts/generate_card_table.py` (đừng sửa tay, sẽ bị ghi đè) |
| Quy chuẩn prompt, 4 lớp chiều sâu, template | `tarot prompt/00-MASTER-PROMPT.md`, `tarot prompt/template.md` |
| **CHUẨN KHUNG VIỀN (đo bằng số)** | `standards/17-the-star/standard.json` + `frame-mask.png` — sinh từ `cards/17-the-star.png` **hiện tại** |

> **2026-09-03 (lần 2):** nguồn thông số nhân vật chuyển từ `01-CARD-TABLE.md` sang
> **`02-CHARACTER-SPECS.md`**. `01` chỉ còn là bảng tra dẫn xuất (sinh từ `cards.json` + `02`),
> không còn là chuẩn. **`cards.json` giữ nguyên 100 %** — `scene`/`count`/`title`/`emblem`
> trong prompt là nguyên văn từ đó; 02 chỉ được phép định hình khối CHARACTER SPECIFICATION.
>
> Quy tắc gộp (định nghĩa trong `scripts/card_specs.py`, chạy `check` để xem lệch):
> - 02 thắng ở 4 trường: `age` · `hair` · `build` (+ cấp A–D) và cung cấp 4 trường mới:
>   `eyes` · `skin` · `signature` · `aura`.
> - 6 lá thuần vật thể (`wands-ace`, `wands-08`, `cups-ace`, `swords-ace`, `swords-03`,
>   `pentacles-ace`) không có trong 02 → giữ theo `cards.json`, không có khối CHARACTER.
> - Lá có nhiều nhân vật mà `cards.json` ghi `distinct per …` (`wands-04`, `wands-05`):
>   **giữ `cards.json`** cho tóc/dáng, vì 02 chỉ mô tả một người.
> - Lệch hiện ghi nhận (chỉ báo cáo, không tự sửa): **0** chỗ tuổi, **15** chỗ tóc
>   (02 dùng tóc búi/tết/áo giáp, `cards.json` đã được làm mềm thành tóc xoã).

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
| `scripts/card_specs.py` | **Đọc `02-CHARACTER-SPECS.md`** + gộp vào `cards.json` (`check` để báo lệch, `show <slug>` để xem một lá) |
| `scripts/build_prompts.py` | Sinh prompt: `scene`/`count` nguyên văn từ `cards.json` + CHARACTER từ `02` + khung theo `standards/17-the-star/standard.json` → `prompts/out/` (`all`, `prompt <slug>`, `check`, `md`) |
| `scripts/build_gallery.py` | Sinh lại `cards/deck.json` + `cards/index.html` từ `cards.json` + ảnh trong `cards/` |
| `scripts/generate_card_table.py` | Sinh lại bảng tra `tarot prompt/01-CARD-TABLE.md` **từ `cards.json` + `02-CHARACTER-SPECS.md`** |
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
python3 scripts/card_specs.py check && \
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
| *Nguồn thông số nhân vật* (2026-09-03, lần 2) | Prompt lấy CHARACTER từ `cards.json`/bảng `01`, bỏ lỡ 4 thuộc tính (mắt · da · nét riêng · không khí) và thang vóc A–D của `02` | Thêm `scripts/card_specs.py` (đọc 02), nối vào `build_prompts.py` + `generate_card_table.py`; `01` giáng cấp thành bảng tra; regenerate 78 file `prompts/out/*` (verify: `scene`/`title`/`emblem`/`count` nguyên văn 78/78) |
| `scripts/count_wands.py` | Hard-code `root = "<repo>/raw"` + 4 slug → chạy trên fresh clone in `MISSING` cả 4 | **Chưa sửa** — cần bạn quyết (đổi sang argv/`--dir` hay xoá) |
