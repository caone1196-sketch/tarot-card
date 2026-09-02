# 🌟 Prompt Mới — Tạo lá bài KHÔNG dùng lá bài cũ (Chuẩn 4 lớp — Bạc & Vàng)

Thư mục này chứa **quy trình tạo lá bài bằng prompt mới**: prompt hoàn toàn tự mô tả
(self-contained), **không tham chiếu bất kỳ ảnh lá bài cũ nào** — chỉ **kế thừa quy trình tạo**
có trong repo. Nhân vật được làm giàu từ `tarot prompt/02-CHARACTER-SPECS.md`.

## Chuẩn 4 lớp mới (theo yêu cầu)

| Lớp | Nội dung | Yêu cầu |
|---|---|---|
| **1. Nền** | Giấy kim loại ánh bạc | metallic silver paper/foil, vân chải nhẹ, phản quang mềm |
| **2. Nội dung** | Cảnh lá bài | phóng to, **tràn viền tới phần họa tiết** (bleed dưới mép khung) |
| **3. Khung họa tiết** | Viền trang trí | **thanh mảnh · sắc nét · ánh vàng kim** (gold-foil filigree + hoa văn góc) |
| **4. Tên lá bài** | Chữ nghệ thuật | kiểu chữ gothic calligraphy vàng — **KHÔNG khung tên, KHÔNG khung ký hiệu** (bỏ ribbon + medallion) |

> Khác chuẩn cũ: bỏ hẳn **oval medallion** (khung ký hiệu) và **ribbon banner** (khung tên).
> Nền đổi từ giấy da cổ (parchment) sang **giấy kim loại ánh bạc**.

## Kế thừa từ quy trình tạo cũ

- Khoá số lượng (`COUNT LOCK`): đúng 2 bình nước cho The Star.
- Khoá giải phẫu (`ANATOMY LOCK`): đúng 2 tay, 2 chân, 1 đầu, 1 thân.
- Tỷ lệ 7:12 (784×1360).
- Nhân vật (`CHARACTER`): tuổi/tóc/vóc dáng từ `01-CARD-TABLE.md` + mắt/da/nét riêng/không khí
  từ `02-CHARACTER-SPECS.md`.

## File

| File | Ý nghĩa |
|---|---|
| `template.md` | Template prompt mới (điền `{TITLE}` `{SCENE}` `{CHARACTER_SPECIFICATION}` `{COUNT_LOCK}`) |
| `17-the-star.txt` | Prompt mới hoàn chỉnh cho lá The Star |
| `frame-template.png` | **Mẫu khung nền + khung họa tiết** (Lớp 1 + Lớp 3), trống ở giữa để ghép nội dung |
| `17-the-star.png` | Ảnh The Star bản cũ (parchment) — sẽ thay bằng bản mới khi cần |

## Ghi chú

Session gắn cố định với nhánh `arena/01a05ffa-tarot-card` nên không tạo nhánh Git mới được;
mọi thứ được đặt gọn trong `new-prompt/` để tách biệt với bộ bài cũ.
