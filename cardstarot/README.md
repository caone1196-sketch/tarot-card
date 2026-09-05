# cardstarot — Bộ Ẩn Chính từ prompt tiếng Việt

Ngày cập nhật: **05/09/2026**.

## Kết quả hiện tại

**Có 3/22 ảnh trong thư mục chính:** The Fool, The Magician và The Empress. Lượt này đã tạo được **hai ảnh mới**; **The High Priestess vẫn chưa có ảnh**. Lần tạo Priestess không trả về ảnh, sau đó công cụ báo đạt hạn mức nên chưa thể thử tiếp. Không có tác vụ tạo ảnh chạy ngầm.

| Lá | Ảnh | Kích thước | Trạng thái |
|---|---|---|---|
| 00 — THE FOOL | [00-fool.png](00-fool.png) | PNG 784 × 1360 | Giữ nguyên ảnh đã tạo trước |
| 01 — THE MAGICIAN | [01-magician.png](01-magician.png) | PNG 784 × 1360 | Đã tạo; nhìn từ sau, lụa quấn eo; đủ bốn vật trên bàn |
| 02 — THE HIGH PRIESTESS | Chưa có | — | Đã thử tạo; chưa nhận được ảnh |
| 03 — THE EMPRESS | [03-empress.png](03-empress.png) | PNG 784 × 1360 | Bản đã chọn, còn khác biệt về góc máy và độ dài tà lụa |

Các lá 04–21 chưa được tạo trong thư mục này.

## Hai ảnh mới

| The Magician | The Empress |
|---|---|
| [![The Magician](01-magician.png)](01-magician.png) | [![The Empress](03-empress.png)](03-empress.png) |

## Kiểm tra và hậu kỳ

### The Magician

- Bản được chọn ban đầu có kích thước **1776 × 2368**, khác tỷ lệ khổ bài. [Bản gốc đã chọn](references/01-magician-selected-original.png) được giữ riêng để đối chiếu.
- Nếu chỉ cắt ảnh theo khổ bài, đầu gậy trên bàn sẽ bị cắt mất. Hậu kỳ bằng code đã dùng chính đầu gậy trong ảnh gốc để thu ngắn phần xa của gậy, giữ nguyên số lượng và tách biệt các đồ vật; đồng thời làm đầu gậy đang cầm kết thúc bên trong ảnh thay vì chạy ra mép trên.
- Sau đó cắt khung dọc và thu nhỏ bằng Lanczos về **784 × 1360**, không bóp méo thân người để ép từ tỷ lệ 3:4 sang khổ bài.
- Đã kiểm tra bằng mắt: trên bàn có **một cốc, một kiếm, một gậy, một đồng tiền**; gậy trong tay là đạo cụ riêng. Giữ góc nhìn từ sau, tóc đen và lụa ngắn ở eo/hông, không khung hoặc chữ.

### The Empress — ghi rõ khác biệt

- Giữ bản bạn đã chọn, thu nhỏ theo tỷ lệ và cắt giữa nhẹ từ **1440 × 2560** về **784 × 1360**; không chỉnh sửa cơ thể, trang phục hay đạo cụ.
- Ảnh có vòng hoa, ngai nhung đỏ, khiên trái tim, lúa mì, trái cây và phong cảnh sông núi.
- **Góc nhìn thực tế là chếch trước, không phải từ sau như prompt.** Tà lụa cũng dài hơn yêu cầu khăn quấn ngắn. Vì vậy ảnh được ghi là **bản đã chọn có khác biệt**, không tuyên bố đáp ứng toàn bộ ràng buộc góc máy/trang phục.
- [Bản váy dài từ lượt trước](references/03-empress-before-waist-silk.png) vẫn được giữ riêng làm tham chiếu, không tính là ảnh mới của lượt này.

## Prompt và ngữ cảnh góc máy

| Lá | Prompt yêu cầu | Văn bản gửi ở lần tạo chính trong lượt này |
|---|---|---|
| The Magician | [01-magician.next.txt](01-magician.next.txt) | [01-magician.sent.txt](01-magician.sent.txt) |
| The High Priestess | [02-priestess.next.txt](02-priestess.next.txt) | [02-priestess.sent.txt](02-priestess.sent.txt) |
| The Empress | [03-empress.next.txt](03-empress.next.txt) | [03-empress.sent.txt](03-empress.sent.txt) |

- Nội dung ba file `*.next.txt` giữ nguyên so với lần bổ sung góc máy; không viết lại nhân vật, tuổi, trang phục hay đạo cụ để khớp ngược với ảnh.
- Góc máy được yêu cầu: Magician sau chếch trái nhìn rõ bàn; Priestess sau chếch phải nhìn vào lòng; Empress sau chếch phải qua cạnh ngai. Phần trước của thân trên được yêu cầu nằm ngoài góc nhìn, dải lụa eo/hông đủ kín.
- `*.sent.txt` ghi đúng văn bản của lần gọi tạo ảnh chính. Có file prompt không đồng nghĩa đã có ảnh — Priestess vẫn thiếu ảnh.
- Mục tiêu chung vẫn là tranh phủ kín ảnh, không khung, không chữ, PNG **784 × 1360**. Đây là artwork-only nên không áp dụng phép chấm viền vàng của bộ bài gốc.
- Việc dừng theo lựa chọn trước đây đã được mở lại khi người dùng yêu cầu tạo ảnh trong lượt này. Lượt đã kết thúc với hai ảnh mới; phần còn thiếu không tự chạy tiếp.

## Bảo toàn dữ liệu

- [Bộ prompt tiếng Việt gốc](../prompts/out6_vi/README.md) và [bản tổng hợp 78 prompt](../prompts/out6_vi/TAT-CA-78-PROMPT.md) không thay đổi.
- Không sửa `tarot prompt/cards.json`, prompt tiếng Anh, ảnh trong `cards/`, `cards2/`, `cards3/`, bộ chuẩn khung hoặc gallery mặc định.
- The Fool trong thư mục này vẫn trùng byte với `cards_vi/00-fool.png`.
- [manifest.json](manifest.json) ghi trạng thái thực tế, kích thước, hash, thao tác hậu kỳ và các điểm khác biệt đã nhận thấy. Kiểm tra kỹ thuật không phải chứng nhận mọi chi tiết giải phẫu đều hoàn hảo.
