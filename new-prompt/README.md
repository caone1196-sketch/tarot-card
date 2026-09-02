# 🌟 Prompt Mới — Tạo lá bài KHÔNG dùng lá bài cũ

Thư mục này chứa **quy trình tạo lá bài bằng prompt mới**: prompt hoàn toàn tự mô tả
(self-contained), **không tham chiếu bất kỳ ảnh lá bài cũ nào** — chỉ **kế thừa quy trình tạo**
đã có trong repo.

## Vì sao có thư mục này

Yêu cầu: tạo lá bài **The Star** bằng một **prompt mới**, **không sử dụng lá bài cũ**
(không dùng ảnh `cards/17-the-star.png` làm khung chuẩn tham chiếu), chỉ lấy lại **quy trình tạo**.

> Ghi chú: session gắn cố định với nhánh `arena/01a05ffa-tarot-card` nên không tạo nhánh Git
> mới được — mọi thứ được đặt gọn trong thư mục `new-prompt/` để tách biệt với bộ bài cũ.

## Khác gì so với prompt cũ

| | Prompt cũ (`prompts/out/`) | Prompt mới (`new-prompt/`) |
|---|---|---|
| Khung viền | "built inside the reference frame … matching THE STAR" — **trỏ vào ảnh lá cũ** | Mô tả hoàn toàn bằng chữ: *thin golden gothic line-art border + corner flourishes + aged parchment* |
| Nhân vật | chỉ tuổi / tóc / vóc dáng | **bổ sung** mắt, màu da, nét riêng (signature), không khí (aura) từ `tarot prompt/02-CHARACTER-SPECS.md` |
| Quy trình 4 lớp, medallion, ruy băng, count lock, anatomy lock, 7:12 | giữ nguyên | **giữ nguyên** (kế thừa quy trình tạo) |

## Kế thừa từ quy trình tạo cũ

- Cấu trúc 4 lớp chiều sâu (`tarot prompt/00-MASTER-PROMPT.md`): nền giấy da → nội dung
  tràn nhẹ dưới khung → khung vàng đè lên mép nội dung → medallion + ruy băng tên.
- Khoá số lượng (`COUNT LOCK`): đúng 2 bình nước cho The Star.
- Khoá giải phẫu (`ANATOMY LOCK`): đúng 2 tay, 2 chân, 1 đầu, 1 thân.
- Tỷ lệ 7:12 (784×1360), huy hiệu `an eight-pointed star`, tên `THE STAR`.

## Nội dung lá The Star (từ nguồn chuẩn)

- `scene`: từ `tarot prompt/cards.json` → `17-the-star`.
- `CHARACTER` (mắt · da · nét riêng · không khí): từ `tarot prompt/02-CHARACTER-SPECS.md`
  → mắt **starlight grey-blue, wide-set** · da **ivory** · tóc vàng ánh bạc ướt rủ qua vai ·
  **chòm tàn nhang vàng trên hai vai** · không khí *nước đêm – sao – làn da ướt* · vóc dáng **A (thanh mảnh)**.

## File

| File | Ý nghĩa |
|---|---|
| `template.md` | Template prompt mới tái sử dụng (điền `{TITLE}` `{EMBLEM}` `{SCENE}` `{CHARACTER_SPECIFICATION}` `{COUNT_LOCK}`) |
| `17-the-star.txt` | Prompt mới hoàn chỉnh cho lá The Star |
| `17-the-star.png` | Ảnh lá The Star được tạo từ prompt mới |
