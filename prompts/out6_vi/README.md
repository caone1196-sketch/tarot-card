# 78 prompt Tarot — Bản tiếng Việt của out6

**Ngày biên soạn:** 05/09/2026.

**Nguồn dịch trực tiếp:** 78 file `prompts/out6/*.txt` tại commit `aea4311e1da2ca63b1c14dd6d3b1f133ea5a6e0c`.

**Phạm vi:** dịch sang tiếng Việt, không vẽ lại bài, không sửa ứng dụng, không đồng bộ lại dữ liệu nguồn.

## Mở và sử dụng

- **[Đọc toàn bộ 78 prompt trong một tài liệu](TAT-CA-78-PROMPT.md).**
- Dùng riêng từng lá: mở file `<slug>.txt` trong thư mục này. Tên file trùng hoàn toàn với bản tiếng Anh.
- Sao chép **toàn bộ nội dung một file** cho mỗi lần tạo một ảnh, không chỉ sao chép phần cảnh và không gửi cả tài liệu 78 lá trong một lần tạo ảnh.
- Đính kèm ảnh gốc **[cards/17-the-star.png](../../cards/17-the-star.png)** làm ảnh tham chiếu nếu công cụ tạo ảnh hỗ trợ. Chỉ viết đường dẫn trong prompt không tự tải ảnh vào một dịch vụ bên ngoài.
- Chọn đầu ra PNG dọc **784 × 1360 pixel** theo khóa đầu ra. Prompt giữ yêu cầu chỉ vẽ phần tranh, không khung và không chữ; đọc các điểm mâu thuẫn của nguồn bên dưới trước khi sử dụng.
- Đây là **bản dịch tĩnh**, chưa được nối vào ứng dụng hoặc các script hiện có. Khi `out6` thay đổi, cần đối chiếu và cập nhật bản dịch; các lệnh build cũ không tự cập nhật `out6_vi`.

## Kết quả quét liên quan đến bản dịch

| Thành phần | Vai trò trong dự án |
|---|---|
| `app.py` | Ứng dụng Streamlit: bộ sưu tập, tải lên/thay thế ảnh, rút một lá, kiểm tra khung |
| `tarot prompt/cards.json` | Nguồn dữ liệu chuẩn của 78 lá; chỉ đọc để đối chiếu, không chỉnh sửa |
| `tarot prompt/00-MASTER-PROMPT.md`, `template.md`, `AGENTS.md` | Quy chuẩn và quy tắc làm việc; không dùng để ghi đè nội dung `out6` khi dịch |
| `prompts/out`, `out2`, `out2_safe`, `out4`, `out5`, `out6` | Những phiên bản prompt khác nhau; bản dịch này chỉ lấy nội dung file `out6` hiện có |
| `scripts/build_prompts.py`, `scripts/build_prompts_out6.py` | Pipeline nguồn và bước thêm tham chiếu The Star; không chạy lại để tránh ghi đè prompt |
| `cards/17-the-star.png`, `standards/17-the-star/` | Ảnh tham chiếu và bộ chuẩn khung của dự án; không thay đổi |
| `cards/`, `cards2/`, `cards3/`, `variants/` | Tài sản hình ảnh hiện có; không tạo, sửa hoặc thay thế ảnh |

Bộ `out6` có 22 lá Ẩn Chính và 14 lá cho mỗi nhóm Gậy, Cốc, Kiếm, Tiền.
Không lấy cách viết hoặc giới hạn tuổi 20–23 của `out4` để thay cho `out6`.

## Nguyên tắc Việt hóa

- Dịch đầy đủ cảnh, bối cảnh bổ sung, tuổi, tóc, vóc dáng, sắc thái tạo hình, cách bố trí và các điều cấm.
- Giữ nguyên tên tiếng Anh bên trong prompt, mã lá, đường dẫn `cards/17-the-star.png`, nhãn nguồn `cards.json`, kích thước và định dạng PNG. Tên Việt trong mục lục chỉ để tra cứu, không phải chữ cần vẽ lên ảnh.
- Giữ toàn bộ con số, phép cộng kiểm đếm, thứ tự vật thể, yêu cầu không chồng lấp, không cắt mất và các cảnh báo lỗi trước đây.
- Giữ nguyên tuổi riêng của từng khối nhân vật; không tự nâng/hạ tuổi, thay tóc, đổi vóc dáng, trang phục hay cảnh để hòa giải mâu thuẫn.
- Những chỗ khối kiểm đếm dùng đại từ `him/his` nhưng cảnh mô tả nữ được dịch bằng từ quy chiếu trung tính **“nhân vật”**; không đổi nhân vật nữ thành nam.
- Một số thuật ngữ/tên kiểu tóc quen dùng như `ankh`, `caduceus`, `sepia`, `caramel`, `bob`, `pixie` được giữ để không mất định danh. Toàn bộ câu chỉ dẫn đã được dịch.
- Đây là bản dịch nội dung nghệ thuật của nguồn, không phải phiên bản biên tập mới hoặc phiên bản bảo đảm được mọi công cụ tạo ảnh chấp nhận.

### Thuật ngữ thống nhất

| Trong nguồn | Trong bản tiếng Việt |
|---|---|
| REFERENCE STANDARD | CHUẨN THAM CHIẾU |
| SCENE | CẢNH |
| ENVIRONMENT AND SETTING | MÔI TRƯỜNG VÀ BỐI CẢNH |
| CHARACTER SPECIFICATION | THÔNG SỐ NHÂN VẬT |
| COUNT LOCK | KHÓA SỐ LƯỢNG |
| ANATOMY LOCK | KHÓA GIẢI PHẪU |
| OUTPUT LOCK | KHÓA ĐẦU RA |
| STAR-REFERENCE OUTPUT | ĐẦU RA THEO THAM CHIẾU THE STAR |
| wand / staff | cây gậy |
| sword | thanh kiếm |
| cup / chalice | cốc / chén thánh |
| pentacle coin | đồng tiền khắc ngôi sao năm cánh |
| jug | bình rót nước |
| edge-to-edge artwork | tranh phủ kín từ mép này đến mép kia |

## Những điểm cần lưu ý trong nguồn — chưa tự sửa

Đây là các điểm phát hiện khi đối chiếu, không phải yêu cầu mới được thêm vào prompt.

1. **Tham chiếu khung nhưng đầu ra cấm khung.** Đầu và cuối `out6` vẫn nhắc nét vàng mảnh, khung đã đo của The Star; `OUTPUT LOCK` lại cấm khung, nét vàng, hoa văn góc. Bản dịch giữ cả hai nội dung, không âm thầm viết lại quy chuẩn.
2. **Kích thước và tỷ lệ chưa trùng khít.** `784 × 1360` rút gọn thành `49:85`, không đúng tuyệt đối `7:12`. Cả kích thước pixel và câu “bố cục 7:12” đều có trong nguồn và được giữ lại; bản dịch không tự đổi kích thước.
3. **Cảnh và thông số nhân vật có chỗ khác nhau.** Ví dụ `03-empress` ghi mảnh mai ở cảnh nhưng đầy đặn ở vóc dáng; `wands-04` ghi người thứ hai tóc nâu đỏ ở cảnh nhưng tóc đen xoăn ở thông số; `wands-05` có hai danh sách tóc không khớp; `wands-queen` ghi tóc sẫm ở cảnh nhưng tóc nâu đỏ ở thông số; `pentacles-03` ghi tóc xõa ở cảnh nhưng tóc tết ở thông số. Các khác biệt này vẫn được phản ánh trong bản dịch.
4. **Tư thế giữa các khối cũng có chỗ khác nhau.** `wands-10` nằm nghỉ bên bó gậy ở cảnh nhưng mô tả mang bó gậy ở vóc dáng. `swords-knight` giơ kiếm cao ở cảnh nhưng chĩa kiếm về phía trước trong khóa số lượng. Chưa chọn một cách thay cho cách kia.
5. **Lệnh cấm chữ/biểu tượng/ruy băng rất rộng.** Một số cảnh gốc vẫn cần các chi tiết này, như chữ huyền bí ở `10-wheel`, ruy băng vô cực ở `pentacles-02`, huy hiệu tiền trên tường ở `pentacles-10`. Bản dịch không xóa đồ vật hay thêm ngoại lệ mà nguồn chưa nêu.
6. **Mô tả hình thể và câu giới hạn đầu ra cùng tồn tại.** Nguồn có mô tả khỏa thân/gợi cảm, đồng thời cuối prompt yêu cầu không phô bày chi tiết nhạy cảm. Không tự đổi sang `out4` hay `out2_safe`. Các cảnh `cups-10`, `swords-06`, `pentacles-10` còn nhắc trẻ em; mô tả khỏa thân của người trưởng thành không được diễn giải thành mô tả của trẻ em. Giới hạn tuổi trong khối nhân vật không có nghĩa là mọi nhân vật phụ trong các cảnh này đều trưởng thành.
7. **Không phải lá nào cũng có mọi khối.** Sáu lá không có thông số nhân vật: `cups-ace`, `pentacles-ace`, `swords-03`, `swords-ace`, `wands-08`, `wands-ace`. Có 16 lá không có khóa số lượng riêng. Không tự bổ sung những khối nguồn không có; các con số nằm trong cảnh vẫn được dịch đầy đủ.
8. **The Fool là trường hợp riêng.** `00-fool` không có câu mở đầu nêu tên lá như 77 file còn lại, nhưng có thêm khối môi trường/bối cảnh. Bản dịch giữ cấu trúc này.

Muốn hòa giải các điểm trên, cần quyết định riêng về nội dung gốc hoặc một phiên bản biên tập mới; bản dịch này không thay thế `cards.json` làm nguồn chuẩn.

## Kiểm tra đã thực hiện

| Kiểm tra văn bản | Kết quả |
|---|---|
| Tập mã/tên file trùng với `out6` và danh sách 78 lá | 78/78 |
| Khối cảnh, tham chiếu, giải phẫu và đầu ra | 78/78 |
| Khối thông số nhân vật | 72/72 khối nguồn |
| Khối khóa số lượng | 62/62 khối nguồn |
| Khối môi trường bổ sung của The Fool | 1/1 |
| Chuỗi con số, kể cả tuổi, kích thước và phép cộng | Khớp từng file với nguồn |
| Thứ tự và số lượng đoạn | Khớp từng file với nguồn |
| Các tên tiếng Anh trong câu mở đầu | 77/77; The Fool không có câu này trong nguồn |
| Mã hóa UTF-8, dấu tiếng Việt NFC, không chỗ trống chờ điền | Đạt |
| 78 khối trong bản tổng hợp | Trùng nguyên văn 78 file `.txt` |
| File nguồn tiếng Anh | SHA-256 giữ nguyên |

Đây là kiểm tra **văn bản**, không phải chứng nhận ảnh sinh ra sẽ đúng số vật thể, đúng giải phẫu hay đạt chuẩn khung. Không tạo ảnh mới và không chạy lại công cụ sinh ảnh/chuẩn khung trong công việc dịch này.

## Mục lục từng lá

### Ẩn Chính — 22 lá

| Tên gốc | Tên Việt để tra cứu | File prompt |
|---|---|---|
| THE FOOL | Kẻ Khờ | [00-fool.txt](00-fool.txt) |
| THE MAGICIAN | Nhà Ảo Thuật | [01-magician.txt](01-magician.txt) |
| THE HIGH PRIESTESS | Nữ Tư Tế | [02-priestess.txt](02-priestess.txt) |
| THE EMPRESS | Nữ Hoàng | [03-empress.txt](03-empress.txt) |
| THE EMPEROR | Hoàng Đế | [04-emperor.txt](04-emperor.txt) |
| THE HIEROPHANT | Giáo Hoàng | [05-hierophant.txt](05-hierophant.txt) |
| THE LOVERS | Tình Nhân | [06-lovers.txt](06-lovers.txt) |
| THE CHARIOT | Cỗ Xe | [07-chariot.txt](07-chariot.txt) |
| STRENGTH | Sức Mạnh | [08-strength.txt](08-strength.txt) |
| THE HERMIT | Ẩn Sĩ | [09-hermit.txt](09-hermit.txt) |
| WHEEL OF FORTUNE | Bánh Xe Số Phận | [10-wheel.txt](10-wheel.txt) |
| JUSTICE | Công Lý | [11-justice.txt](11-justice.txt) |
| THE HANGED | Người Treo Ngược | [12-hanged.txt](12-hanged.txt) |
| DEATH | Cái Chết | [13-death.txt](13-death.txt) |
| TEMPERANCE | Tiết Độ | [14-temperance.txt](14-temperance.txt) |
| THE DEVIL | Ác Quỷ | [15-devil.txt](15-devil.txt) |
| THE TOWER | Tòa Tháp | [16-tower.txt](16-tower.txt) |
| THE STAR | Ngôi Sao | [17-the-star.txt](17-the-star.txt) |
| THE MOON | Mặt Trăng | [18-moon.txt](18-moon.txt) |
| THE SUN | Mặt Trời | [19-sun.txt](19-sun.txt) |
| JUDGEMENT | Phán Xét | [20-judgement.txt](20-judgement.txt) |
| THE WORLD | Thế Giới | [21-world.txt](21-world.txt) |

### Gậy — 14 lá

| Tên gốc | Tên Việt để tra cứu | File prompt |
|---|---|---|
| ACE OF WANDS | Át Gậy | [wands-ace.txt](wands-ace.txt) |
| TWO OF WANDS | Hai Gậy | [wands-02.txt](wands-02.txt) |
| THREE OF WANDS | Ba Gậy | [wands-03.txt](wands-03.txt) |
| FOUR OF WANDS | Bốn Gậy | [wands-04.txt](wands-04.txt) |
| FIVE OF WANDS | Năm Gậy | [wands-05.txt](wands-05.txt) |
| SIX OF WANDS | Sáu Gậy | [wands-06.txt](wands-06.txt) |
| SEVEN OF WANDS | Bảy Gậy | [wands-07.txt](wands-07.txt) |
| EIGHT OF WANDS | Tám Gậy | [wands-08.txt](wands-08.txt) |
| NINE OF WANDS | Chín Gậy | [wands-09.txt](wands-09.txt) |
| TEN OF WANDS | Mười Gậy | [wands-10.txt](wands-10.txt) |
| PAGE OF WANDS | Hầu Cận Gậy | [wands-page.txt](wands-page.txt) |
| KNIGHT OF WANDS | Kỵ Sĩ Gậy | [wands-knight.txt](wands-knight.txt) |
| QUEEN OF WANDS | Hoàng Hậu Gậy | [wands-queen.txt](wands-queen.txt) |
| KING OF WANDS | Vua Gậy | [wands-king.txt](wands-king.txt) |

### Cốc — 14 lá

| Tên gốc | Tên Việt để tra cứu | File prompt |
|---|---|---|
| ACE OF CUPS | Át Cốc | [cups-ace.txt](cups-ace.txt) |
| TWO OF CUPS | Hai Cốc | [cups-02.txt](cups-02.txt) |
| THREE OF CUPS | Ba Cốc | [cups-03.txt](cups-03.txt) |
| FOUR OF CUPS | Bốn Cốc | [cups-04.txt](cups-04.txt) |
| FIVE OF CUPS | Năm Cốc | [cups-05.txt](cups-05.txt) |
| SIX OF CUPS | Sáu Cốc | [cups-06.txt](cups-06.txt) |
| SEVEN OF CUPS | Bảy Cốc | [cups-07.txt](cups-07.txt) |
| EIGHT OF CUPS | Tám Cốc | [cups-08.txt](cups-08.txt) |
| NINE OF CUPS | Chín Cốc | [cups-09.txt](cups-09.txt) |
| TEN OF CUPS | Mười Cốc | [cups-10.txt](cups-10.txt) |
| PAGE OF CUPS | Hầu Cận Cốc | [cups-page.txt](cups-page.txt) |
| KNIGHT OF CUPS | Kỵ Sĩ Cốc | [cups-knight.txt](cups-knight.txt) |
| QUEEN OF CUPS | Hoàng Hậu Cốc | [cups-queen.txt](cups-queen.txt) |
| KING OF CUPS | Vua Cốc | [cups-king.txt](cups-king.txt) |

### Kiếm — 14 lá

| Tên gốc | Tên Việt để tra cứu | File prompt |
|---|---|---|
| ACE OF SWORDS | Át Kiếm | [swords-ace.txt](swords-ace.txt) |
| TWO OF SWORDS | Hai Kiếm | [swords-02.txt](swords-02.txt) |
| THREE OF SWORDS | Ba Kiếm | [swords-03.txt](swords-03.txt) |
| FOUR OF SWORDS | Bốn Kiếm | [swords-04.txt](swords-04.txt) |
| FIVE OF SWORDS | Năm Kiếm | [swords-05.txt](swords-05.txt) |
| SIX OF SWORDS | Sáu Kiếm | [swords-06.txt](swords-06.txt) |
| SEVEN OF SWORDS | Bảy Kiếm | [swords-07.txt](swords-07.txt) |
| EIGHT OF SWORDS | Tám Kiếm | [swords-08.txt](swords-08.txt) |
| NINE OF SWORDS | Chín Kiếm | [swords-09.txt](swords-09.txt) |
| TEN OF SWORDS | Mười Kiếm | [swords-10.txt](swords-10.txt) |
| PAGE OF SWORDS | Hầu Cận Kiếm | [swords-page.txt](swords-page.txt) |
| KNIGHT OF SWORDS | Kỵ Sĩ Kiếm | [swords-knight.txt](swords-knight.txt) |
| QUEEN OF SWORDS | Hoàng Hậu Kiếm | [swords-queen.txt](swords-queen.txt) |
| KING OF SWORDS | Vua Kiếm | [swords-king.txt](swords-king.txt) |

### Tiền — 14 lá

| Tên gốc | Tên Việt để tra cứu | File prompt |
|---|---|---|
| ACE OF PENTACLES | Át Tiền | [pentacles-ace.txt](pentacles-ace.txt) |
| TWO OF PENTACLES | Hai Tiền | [pentacles-02.txt](pentacles-02.txt) |
| THREE OF PENTACLES | Ba Tiền | [pentacles-03.txt](pentacles-03.txt) |
| FOUR OF PENTACLES | Bốn Tiền | [pentacles-04.txt](pentacles-04.txt) |
| FIVE OF PENTACLES | Năm Tiền | [pentacles-05.txt](pentacles-05.txt) |
| SIX OF PENTACLES | Sáu Tiền | [pentacles-06.txt](pentacles-06.txt) |
| SEVEN OF PENTACLES | Bảy Tiền | [pentacles-07.txt](pentacles-07.txt) |
| EIGHT OF PENTACLES | Tám Tiền | [pentacles-08.txt](pentacles-08.txt) |
| NINE OF PENTACLES | Chín Tiền | [pentacles-09.txt](pentacles-09.txt) |
| TEN OF PENTACLES | Mười Tiền | [pentacles-10.txt](pentacles-10.txt) |
| PAGE OF PENTACLES | Hầu Cận Tiền | [pentacles-page.txt](pentacles-page.txt) |
| KNIGHT OF PENTACLES | Kỵ Sĩ Tiền | [pentacles-knight.txt](pentacles-knight.txt) |
| QUEEN OF PENTACLES | Hoàng Hậu Tiền | [pentacles-queen.txt](pentacles-queen.txt) |
| KING OF PENTACLES | Vua Tiền | [pentacles-king.txt](pentacles-king.txt) |
