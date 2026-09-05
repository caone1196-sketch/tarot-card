# cardstarot — Bộ Ẩn Chính từ prompt tiếng Việt

Ngày cập nhật: **05/09/2026**.

## Yêu cầu trang phục mới

The Magician, The High Priestess và The Empress cần **một dải lụa mỏng màu ngà tối giản, quấn gọn quanh eo và hông, ôm tự nhiên theo cơ thể**, không áo liền thân, không tay áo và không váy dài. Giữ tuổi trưởng thành, tóc, vai trò, bối cảnh và các đạo cụ riêng của từng lá.

**Chưa có ba ảnh đáp ứng yêu cầu mới.** Các lần tạo Magician/Priestess không lưu được ảnh; lần sửa Empress vẫn trả về váy dài và thêm phụ kiện nên đã bị loại khỏi đầu ra chính. Công cụ sau đó báo đạt giới hạn tạo ảnh trong lượt. Không có tác vụ tạo ảnh tự chạy ngầm.

## Tiến độ đầu ra chính

**Có ảnh hoàn tất trong thư mục chính: 1/22 lá Ẩn Chính — The Fool.**

| Lá | Ảnh hoàn tất | Prompt dùng cho lần tạo tiếp theo | Trạng thái |
|---|---|---|---|
| 00 — THE FOOL | [00-fool.png](00-fool.png) | [Prompt đã dùng](00-fool.sent.txt) | PNG 784 × 1360, giữ nguyên |
| 01 — THE MAGICIAN | Chưa có | [01-magician.next.txt](01-magician.next.txt) | Chờ tạo theo yêu cầu lụa quấn eo |
| 02 — THE HIGH PRIESTESS | Chưa có | [02-priestess.next.txt](02-priestess.next.txt) | Chờ tạo theo yêu cầu lụa quấn eo |
| 03 — THE EMPRESS | Chưa có bản trang phục mới | [03-empress.next.txt](03-empress.next.txt) | Chờ tạo lại; bản đã chọn trước được giữ làm tham chiếu |

Các lá 04–21 chưa được tạo trong thư mục này.

## Ảnh hiện có

[![THE FOOL — PNG 784 × 1360](00-fool.png)](00-fool.png)

## Bản Empress đã chọn trước

[Bản Empress trước yêu cầu lụa quấn eo](references/03-empress-before-waist-silk.png) được lưu riêng trong `references/`. Đây là ảnh mặc váy dài đã được chọn ở lượt trước, **không phải ảnh đáp ứng yêu cầu trang phục mới** và không được tính vào số ảnh hoàn tất ở trên. Bản tham chiếu được thu nhỏ từ 1568 × 2720 xuống 784 × 1360, giữ nguyên tỷ lệ và không thay trang phục.

## Nguồn và cách sử dụng prompt

- Bộ prompt tiếng Việt gốc: [prompts/out6_vi](../prompts/out6_vi/README.md).
- [Bản tổng hợp 78 prompt](../prompts/out6_vi/TAT-CA-78-PROMPT.md).
- Mục tiêu: PNG dọc **784 × 1360**, tranh phủ kín ảnh, **không khung và không chữ**.
- `*.next.txt` là mô tả render mới nhất cho ba lá cần tạo lại. Đây là bản rút gọn theo yêu cầu trang phục mới, dự kiến dùng để tạo ảnh từ văn bản; chưa tạo được ảnh thành công từ các file này.
- `*.sent.txt` lưu mô tả của các lượt trước, không tự động thay bằng `*.next.txt`. Không dùng các câu yêu cầu áo/váy dài trong prompt cũ để ghi đè yêu cầu mới.
- Magician: trên bàn tế phải có đúng bốn vật — một cốc, một kiếm, một gậy, một đồng tiền. Gậy đang giơ trên cao là đạo cụ riêng trong tay. Cần kiểm tra số lượng trực tiếp khi có ảnh.
- Priestess: giữ hai cột đá, voan trên đầu, cuộn thư trong lòng và trăng bạc dưới chân; voan không được biến thành áo choàng dài.
- Empress: giữ vòng hoa, ngai nhung, lúa mì, trái cây và khiên trái tim; không thêm quyền trượng hay vương miện ngôi sao.

## Bảo toàn dữ liệu

- Không thay thế ảnh trong `cards/`, `cards2/`, `cards3/`.
- The Fool trong thư mục này vẫn trùng byte với `cards_vi/00-fool.png`.
- Không sửa `cards.json`, bộ prompt tiếng Việt gốc, prompt tiếng Anh, chuẩn khung hoặc gallery mặc định.
- [manifest.json](manifest.json) ghi trạng thái thực tế, prompt đang chờ và mã SHA-256 của các file liên quan.
