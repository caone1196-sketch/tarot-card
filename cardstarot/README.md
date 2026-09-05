# cardstarot — Bộ Ẩn Chính từ prompt tiếng Việt

Ngày cập nhật: **06/09/2026**.

## Bản thử mới — The Fool quấn lụa eo/hông

Đã thêm [bản thử The Fool](variants/00-fool-waist-ribbon.png) theo lựa chọn **chỉ quấn eo và hông**, góc nhìn 3/4 từ sau. [Ghi chú và prompt](variants/00-fool-waist-ribbon.md) lưu riêng. **Chưa thay ảnh The Fool chính.**

Mức “95%” trong prompt là hướng dẫn thị giác cho lớp chiffon ngoài, không phải số đo độ xuyên sáng của ảnh; vùng quấn chồng và lớp lót vẫn giữ kín.

## Bản hiện tại: Empress góc 3/4

Bản chính The Empress giữ **góc ngồi 3/4** từ lượt chỉnh trước, theo lựa chọn giữ trang phục hiện tại. Cả thân người và ngai đều có chiều sâu chếch, gương mặt quay nhẹ về người xem. Magician giữ nguyên bản chính diện đã chấp nhận; các lá khác không thay đổi.

**Riêng Magician: người dùng đã chấp nhận bản chính diện có lụa dài xuống chân.** Đây là lựa chọn được xác nhận, không phải tự thay khăn ngắn mà không thông báo.

| Lá | Ảnh hiện tại | Kích thước | Trạng thái |
|---|---|---|---|
| 00 — THE FOOL | [00-fool.png](00-fool.png) | PNG 784 × 1360 | Giữ nguyên |
| 01 — THE MAGICIAN | [01-magician.png](01-magician.png) | PNG 784 × 1360 | Chính diện, đứng; lụa dài đã được chấp nhận |
| 02 — THE HIGH PRIESTESS | Chưa có | — | Không nằm trong lượt sửa này; giữ trạng thái còn thiếu |
| 03 — THE EMPRESS | [03-empress.png](03-empress.png) | PNG 784 × 1360 | Ngồi góc 3/4; giữ lụa quấn và tà bên |

Vẫn có **3/22 ảnh** trong thư mục chính, cùng một bản thử riêng của The Fool. Lượt này không thay ảnh chính nào, không tạo Priestess hoặc các lá 04–21. Không có tác vụ tạo ảnh chạy ngầm.

## Xem ảnh hiện tại

| The Magician | The Empress |
|---|---|
| [![The Magician — chính diện](01-magician.png)](01-magician.png) | [![The Empress — góc ngồi 3/4](03-empress.png)](03-empress.png) |

## Kiểm tra và cách tạo

### The Magician

- Bản cuối được dựng mới từ mô tả sau khi thao tác đổi góc trên ảnh cũ không trả về ảnh; không phải xoay ảnh cũ bằng code.
- Giữ nhân vật trưởng thành 22 tuổi, tóc đen dài, tư thế một tay giơ gậy và tay kia chỉ xuống, vườn hoa hồng đen, bàn tế đá.
- Đã kiểm tra bằng mắt: có đúng **một cốc, một kiếm, một gậy và một đồng tiền** trên bàn; gậy trong tay là đạo cụ riêng. Không có khung hoặc tiêu đề.
- Tấm lụa dài là phiên bản người dùng đã chọn giữ. Prompt render cho riêng lá này được cập nhật theo lựa chọn đó; không áp dụng ngoại lệ lụa dài cho các lá chưa được yêu cầu.
- Ảnh sinh ra ở **952 × 1652**, được thu nhỏ theo tỷ lệ và chuẩn hóa về **784 × 1360**. Không cắt ghép lại cơ thể hoặc sửa đầu gậy trong bản chính diện này.

### The Empress

- Chỉ đổi góc nhìn và hướng ngồi sang **3/4**; vẫn ngồi tự nhiên, hai tay trên tay vịn, chân khép, giữ vòng hoa, tóc vàng, ngai nhung, khiên trái tim, lúa mì và trái cây.
- Giữ kiểu trang phục đang dùng: lụa ngà quấn eo/hông và phủ đùi, có tà buông bên ngai; đầu gối, bắp chân và bàn chân vẫn nhìn thấy. Không đổi thành váy trùm kín chân hoặc thêm áo ở thân trên.
- Tóc dài che phần ngực khi đổi góc. Bố cục được kiểm tra bằng mắt, không chỉ xoay gương mặt trên một thân người còn chính diện.
- Quy trình dùng ảnh góc chếch cũ làm mẫu phối cảnh, bản chính diện hiện tại làm mẫu tóc/trang phục, rồi chỉnh lại lụa theo mẫu đã chọn. `manifest.json` ghi hai bước và các ảnh tham chiếu thực sự được dùng.
- Ảnh cuối là **PNG RGB 784 × 1360**, không khung hoặc chữ; không bóp méo cơ thể bằng phép kéo giãn ảnh.

## Các file prompt

| Lá | Prompt yêu cầu hiện tại | Văn bản dùng tạo bản hiện tại |
|---|---|---|
| The Magician | [01-magician.next.txt](01-magician.next.txt) | [01-magician.sent.txt](01-magician.sent.txt) |
| The High Priestess | [02-priestess.next.txt](02-priestess.next.txt) | [02-priestess.sent.txt](02-priestess.sent.txt) — lượt trước, chưa có ảnh |
| The Empress | [03-empress.next.txt](03-empress.next.txt) | [03-empress.sent.txt](03-empress.sent.txt) |

- Magician giữ nguyên prompt chính diện và lựa chọn lụa dài đã được xác nhận. Ở lượt chỉnh Empress trước đó, prompt render đã được cập nhật với góc ngồi 3/4 và kiểu lụa cần giữ từ ảnh tham chiếu.
- Tuổi, nhân vật, cảnh và đạo cụ của Empress không thay đổi. Phần mô tả trang phục ở file render được làm rõ để tránh tự thêm váy phủ chân; các prompt tiếng Việt gốc và `cards.json` không bị sửa.
- `03-empress.sent.txt` là văn bản chính xác của bước chỉnh lụa cuối cùng; văn bản dựng bố cục nằm ở `references/03-empress-three-quarter-layout.sent.txt`. Magician vẫn dùng prompt tạo từ văn bản đã lưu trước; file `.sent.txt` của Priestess vẫn ghi lượt trước chưa có ảnh. `*.next.txt` là mô tả yêu cầu, không phải hàng đợi tự chạy.
- [manifest.json](manifest.json) ghi trạng thái, kích thước, hash, ảnh tham chiếu, cách hậu kỳ và lựa chọn lụa dài được xác nhận. Kiểm tra kỹ thuật không phải chứng nhận mọi chi tiết giải phẫu đều hoàn hảo.

## Các bản trước và tệp tham chiếu

- [Empress chính diện trước khi đổi sang góc 3/4](references/03-empress-before-three-quarter.png) · [prompt của bản chính diện](references/03-empress-before-three-quarter.sent.txt).
- [Ảnh bố cục dùng trong bước chỉnh cuối](references/03-empress-three-quarter-layout.png) · [prompt dựng bố cục](references/03-empress-three-quarter-layout.sent.txt). Đây chỉ là tệp tham chiếu của quy trình, **không phải bản cuối**.
- [Magician trước khi đổi sang chính diện](references/01-magician-before-front.png) · [prompt của bản cũ](references/01-magician-before-front.sent.txt).
- [Empress trước khi đổi sang chính diện](references/03-empress-before-front.png) · [prompt của bản cũ](references/03-empress-before-front.sent.txt).
- [Magician nguyên gốc đã chọn ở lượt trước](references/01-magician-selected-original.png), trước bước hậu kỳ khổ bài của bản nhìn từ sau.
- [Empress váy dài của lượt trước nữa](references/03-empress-before-waist-silk.png).

Các bản trong `references/` không được tính thành lá mới.

## Bảo toàn nguồn

- [Bộ prompt tiếng Việt gốc](../prompts/out6_vi/README.md) và [bản tổng hợp 78 prompt](../prompts/out6_vi/TAT-CA-78-PROMPT.md) không thay đổi.
- Không sửa `tarot prompt/cards.json`, prompt tiếng Anh, ảnh trong `cards/`, `cards2/`, `cards3/`, chuẩn khung hoặc gallery mặc định.
- The Fool vẫn trùng byte với `cards_vi/00-fool.png`. Ảnh, prompt và metadata của Magician/Priestess/Empress không bị sửa trong lượt này. Ảnh chính và prompt chính của The Fool giữ nguyên; chỉ thêm mục bản thử vào metadata của The Fool.
- Tất cả ảnh chính giữ khổ **784 × 1360**, tranh phủ kín ảnh, không khung và không chữ; không áp dụng phép chấm viền vàng của bộ bài gốc.
