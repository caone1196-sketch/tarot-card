# cardstarot — Bộ Ẩn Chính từ prompt tiếng Việt

Ngày cập nhật: **05/09/2026**.

## Tiến độ thực tế

**Có ảnh: 1/22 lá Ẩn Chính.** The Fool đã được tạo ở lượt trước và sao chép nguyên vẹn vào thư mục này. Ba lá tiếp theo đã chuẩn bị prompt render nhưng **chưa có ảnh mới**: các lần tạo ảnh báo lỗi, sau đó công cụ báo đã hết hạn mức tạo ảnh trong lượt.

| Lá | Ảnh | Prompt render | Trạng thái |
|---|---|---|---|
| 00 — THE FOOL | [00-fool.png](00-fool.png) | [00-fool.sent.txt](00-fool.sent.txt) | Đã có ảnh PNG 784 × 1360 |
| 01 — THE MAGICIAN | Chưa có | [01-magician.sent.txt](01-magician.sent.txt) | Đã chuẩn bị prompt; chưa tạo được ảnh |
| 02 — THE HIGH PRIESTESS | Chưa có | [02-priestess.sent.txt](02-priestess.sent.txt) | Đã chuẩn bị prompt; chưa tạo được ảnh |
| 03 — THE EMPRESS | Chưa có | [03-empress.sent.txt](03-empress.sent.txt) | Đã chuẩn bị prompt; chưa tạo được ảnh |

Các lá 04–21 chưa được tạo trong thư mục này. Không có tác vụ tạo ảnh tự chạy ngầm; cần tiếp tục trong lượt mới.

## Ảnh hiện có

[![THE FOOL — PNG 784 × 1360](00-fool.png)](00-fool.png)

## Nguồn và cách render

- Bộ prompt tiếng Việt gốc: [prompts/out6_vi](../prompts/out6_vi/README.md).
- [Bản tổng hợp đủ 78 prompt](../prompts/out6_vi/TAT-CA-78-PROMPT.md).
- Ảnh tham chiếu phong cách: [cards/17-the-star.png](../cards/17-the-star.png).
- Mục tiêu đầu ra: PNG dọc **784 × 1360**, tranh phủ kín ảnh, **không khung và không chữ**. Đây là phiên bản artwork-only, không áp dụng phép chấm viền vàng của bộ bài gốc.
- File `.sent.txt` của The Fool lưu văn bản đã dùng khi tạo ảnh thành công. Ba file `.sent.txt` còn lại lưu bản mô tả render đã chuẩn bị và truyền cho công cụ ở lần thử cuối, **không chứng minh rằng đã tạo được ảnh**.
- Sau khi lần thử đầu bị lỗi, ba prompt render mới được rút gọn sang trang phục lụa cổ điển che kín ngực và vùng hạ thân. Đây là điều chỉnh ở bước render, không phải bản dịch nguyên văn và không ghi đè `prompts/out6_vi` hoặc `tarot prompt/cards.json`.
- Magician vẫn yêu cầu đúng bốn vật trên bàn tế: một cốc, một kiếm, một gậy, một đồng tiền; gậy đang giơ cao là đạo cụ riêng trong tay. Khi tạo được ảnh cần kiểm tra trực tiếp số vật trước khi nhận.
- Empress theo cảnh vòng hoa trong prompt hiện tại, không tự thêm vương miện 12 ngôi sao từ quy chuẩn cũ.

## Bảo toàn dữ liệu

- Không thay thế ảnh trong `cards/`, `cards2/`, `cards3/`.
- Giữ bản The Fool ở `cards_vi/00-fool.png`; bản trong thư mục này trùng byte.
- Không thay đổi `cards.json`, prompt tiếng Anh, bộ chuẩn khung hoặc gallery mặc định.
- [manifest.json](manifest.json) ghi trạng thái từng lá trong lượt này và mã SHA-256 của các file đã có.
