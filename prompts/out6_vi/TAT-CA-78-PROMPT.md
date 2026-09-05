# 78 prompt Tarot — Bản tiếng Việt

**Nguồn:** `prompts/out6/*.txt` · **Ngày:** 05/09/2026

**Bộ bài:** 22 lá Ẩn Chính + 14 Gậy + 14 Cốc + 14 Kiếm + 14 Tiền.

Mỗi khối bên dưới là **một prompt hoàn chỉnh**, trùng nguyên văn file `.txt` cùng tên trong `prompts/out6_vi/`.
Sao chép trọn một khối cho một ảnh; đính kèm ảnh `cards/17-the-star.png` khi công cụ hỗ trợ ảnh tham chiếu. Không yêu cầu tạo cả 78 lá trong một ảnh.

> **Lưu ý:** Đây là bản dịch bám nội dung, không tự sửa các mâu thuẫn sẵn có của nguồn. Đặc biệt, nguồn vừa nhắc khung The Star vừa cấm khung ở đầu ra; kích thước `784 × 1360` cũng không bằng tỷ lệ `7:12` tuyệt đối. Xem [hướng dẫn, kết quả kiểm tra và lưu ý nguồn](README.md) trước khi sử dụng.

Tên Việt trong tiêu đề chỉ giúp tra cứu. Tên tiếng Anh trong prompt được giữ nguyên; khóa đầu ra vẫn cấm vẽ tên và chữ lên ảnh. Không thay đổi ảnh hoặc dữ liệu gốc.

## Mục lục nhóm

- [Ẩn Chính](#nhom-major)
- [Gậy](#nhom-wands)
- [Cốc](#nhom-cups)
- [Kiếm](#nhom-swords)
- [Tiền](#nhom-pentacles)

---

<a id="nhom-major"></a>

## Ẩn Chính — 22 lá

### 01. THE FOOL — Kẻ Khờ

File: [00-fool.txt](00-fool.txt) · Nguồn: `prompts/out6/00-fool.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

CẢNH: một nữ lữ hành 19 tuổi khỏa thân, vô tư, nâng một bông hồng trắng trong một bàn tay và cúi mắt ngắm nó, bước nhẹ về phía mép vực; một chú chó trắng nhỏ nhảy lên sát gót chân nàng; phía xa là những dãy núi dưới ánh mặt trời buổi sớm vàng óng.

MÔI TRƯỜNG VÀ BỐI CẢNH: một thung lũng núi cao rộng lớn mở ra phía bên kia vách đá, những lớp núi xanh xám nhạt dần trong làn sương vàng ấm. Một dòng sông hẹp ánh bạc uốn lượn qua đáy thung lũng xanh, phản chiếu bình minh. Tiền cảnh là đồng cỏ lộng gió, rải rác hoa dại nhỏ màu trắng và vàng, đá nhẵn và những bụi cỏ trổ hạt nghiêng về phía vực. Bầu trời trong gần đường chân trời, có mây nhẹ ở tầng cao, ánh bình minh màu hổ phách, sắc đào nhạt trong không khí và những bóng đổ dài dịu dàng. Gió núi nhẹ lay động cỏ, cành hoa, tóc và lụa, tạo chiều sâu và chuyển động. Giữ môi trường tự nhiên, rộng rãi và có cảm giác đắm mình trong cảnh, mép vực phải rõ ràng, phong cảnh xa tạo phối cảnh khí quyển mạnh. Không thêm công trình, phương tiện, đồ vật hiện đại, nhân vật phụ, văn bản hoặc biểu tượng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 19 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng mật ong gợn sóng, buông xõa đến xương bả vai, tung bay trong gió và bắt nắng, toát vẻ vô tư; Vóc dáng: nhỏ nhắn và mềm dẻo, eo thon, tràn đầy sức sống tuổi trẻ, bước đi nhẹ nhàng và nhún nhảy; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 02. THE MAGICIAN — Nhà Ảo Thuật

File: [01-magician.txt](01-magician.txt) · Nguồn: `prompts/out6/01-magician.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE MAGICIAN" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ pháp sư trẻ khỏa thân, một tay giơ gậy lên trời, tay kia chỉ xuống đất; trên bàn tế trước mặt nàng có một chiếc cốc, một thanh kiếm, một cây gậy và một đồng tiền khắc ngôi sao năm cánh; phía sau là khu vườn hoa hồng đen.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen tuyền thẳng, rẽ ngôi giữa, buông quá eo như một tấm rèm lụa óng mượt; Vóc dáng: cao đẹp như tượng và đầy uy nghi, tỷ lệ cơ thể thanh thoát, dài và cân đối, tư thế đĩnh đạc; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 4 đồ vật đại diện các chất bài trên bàn tế): đúng bốn đồ vật, mỗi loại một món: một chiếc cốc, một thanh kiếm, một cây gậy, một đồng tiền — cả bốn đều đặt trên bàn tế, đều nhìn thấy trọn vẹn, không trùng lặp, không có vật nào khác trên bàn. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 03. THE HIGH PRIESTESS — Nữ Tư Tế

File: [02-priestess.txt](02-priestess.txt) · Nguồn: `prompts/out6/02-priestess.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE HIGH PRIESTESS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ tư tế khỏa thân, thanh thản ngồi giữa hai cột đá; một cuộn thư huyền bí đặt trong lòng nàng; dưới chân là vầng trăng lưỡi liềm màu bạc.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu đỏ đậm gợn sóng tự nhiên, mềm mại buông xuống dưới tấm voan mỏng nhẹ như tơ; Vóc dáng: thanh thản, mảnh mai và duyên dáng, cổ dài, đường cong nữ tính mềm mại theo vẻ đẹp cổ điển; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 04. THE EMPRESS — Nữ Hoàng

File: [03-empress.txt](03-empress.txt) · Nguồn: `prompts/out6/03-empress.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE EMPRESS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng mảnh mai khỏa thân, để lộ một bên ngực, đội vòng hoa trên mái tóc buông lơi, ngả người trên ngai nhung giữa lúa mì chín vàng và trái cây; bên cạnh nàng dựng một chiếc khiên hình trái tim của thần Vệ Nữ.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng óng dày như lúa mì chín, cuộn thành những lọn mềm như dây thừng, tràn xuống hai vai và được kết hoa; Vóc dáng: đầy đặn và nhiều đường cong, ngực và hông nở nang nữ tính, thần thái nữ thần ấm áp và rạng rỡ; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 05. THE EMPEROR — Hoàng Đế

File: [04-emperor.txt](04-emperor.txt) · Nguồn: `prompts/out6/04-emperor.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE EMPEROR" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng đế 25 tuổi khỏa thân, thanh thản ngả người duyên dáng trên ngai đá chạm đầu cừu đực, một tay cầm hờ quyền trượng hình thập tự ankh; phía sau là những dãy núi khô cằn, gồ ghề.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 25 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu đồng sẫm óng mượt, gợn sóng mềm và buông lơi, đội vòng miện vàng hình sừng cừu đực; Vóc dáng: nữ quân vương duyên dáng, mềm mại và thanh nhã, đường cong được tạo khối nhẹ nhàng, phong thái bình thản và dịu dàng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 06. THE HIEROPHANT — Giáo Hoàng

File: [05-hierophant.txt](05-hierophant.txt) · Nguồn: `prompts/out6/05-hierophant.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE HIEROPHANT" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ đại tư tế huyền môn 24 tuổi khỏa thân, thanh thản giơ một tay ban phước; trước mặt nàng là hai nữ phụ lễ trưởng thành khỏa thân đang quỳ; phía sau là các cột của ngôi đền linh thiêng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu cà phê đậm dày, gợn sóng, buông xõa trên vai trần và lưng; Vóc dáng: nữ đại tư tế cao ráo, cao quý và thanh thản, phong thái duyên dáng, trang nghiêm; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 07. THE LOVERS — Tình Nhân

File: [06-lovers.txt](06-lovers.txt) · Nguồn: `prompts/out6/06-lovers.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE LOVERS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: hai phụ nữ trưởng thành khỏa thân đứng nắm tay nhau dưới một thiên thần lớn có cánh; một người xoay ba phần tư cơ thể về phía người xem, người kia đặt một tay ở phần thắt lưng phía sau của người thứ nhất; phía sau họ là cây tri thức có rắn quấn, bên cạnh là cây bốc lửa.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ ấm búi lỏng theo kiểu lãng mạn, những sợi tóc mềm ôm quanh má; Vóc dáng: dáng đồng hồ cát mảnh mai, eo mềm dẻo, đường cong nhẹ nhàng và duyên dáng khi đứng cạnh người bạn đời; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 08. THE CHARIOT — Cỗ Xe

File: [07-chariot.txt](07-chariot.txt) · Nguồn: `prompts/out6/07-chariot.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE CHARIOT" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ xa phu khỏa thân, vai trần, mang vẻ anh hùng, đứng thẳng trên chiến xa bằng đá giữa hai nhân sư dưới mái che đầy sao; phía sau nàng là một thành phố có tường thành.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu chồn sẫm được tết chặt thành một bím dày kiểu chiến binh vắt qua một vai; Vóc dáng: thể thao và săn chắc, vai rõ khối, eo gọn căng, tư thế kiên định và oai hùng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 09. STRENGTH — Sức Mạnh

File: [08-strength.txt](08-strength.txt) · Nguồn: `prompts/out6/08-strength.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "STRENGTH" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ khỏa thân được kết hoa hồng quanh người, nâng một đầu gối và nghiêng sát để bình tĩnh khép hàm của một con sư tử vàng lớn; lưng trần uốn cong, hông bắt ánh mặt trời thấp; một dấu vô cực phát sáng phía trên đầu nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài gợn sóng màu đỏ đồng bóng, buông xuống như bờm sư tử; Vóc dáng: mềm dẻo nhưng mạnh mẽ, cơ lưng rõ nét, đường cong mềm mại và duyên dáng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 10. THE HERMIT — Ẩn Sĩ

File: [09-hermit.txt](09-hermit.txt) · Nguồn: `prompts/out6/09-hermit.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE HERMIT" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ ẩn sĩ khỏa thân đứng trên đỉnh núi trơ trọi dưới bầu trời đêm sâu thẳm đầy sao, giơ cao chiếc đèn lồng đang thắp sáng, ánh vàng ấm tỏa ra từ đèn; ánh đèn vàng làm hiện rõ lưng trần và đường cong một bên ngực nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài màu bạc tro nhẹ như không thực, buông xõa thành những gợn sóng mềm; Vóc dáng: dáng người mảnh mai, bí ẩn và thanh tú, tư thế tĩnh lặng, trầm tư; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 11. WHEEL OF FORTUNE — Bánh Xe Số Phận

File: [10-wheel.txt](10-wheel.txt) · Nguồn: `prompts/out6/10-wheel.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "WHEEL OF FORTUNE" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một bánh xe số phận lớn bằng vàng khắc các chữ cái huyền bí; một nhân sư nữ khỏa thân có cánh, thanh thản ngồi nhẹ nhàng trên đỉnh bánh xe, một tay cầm hờ một thanh kiếm dựng thẳng; một bên có rắn vàng vươn lên, bên kia là vị thần đầu chó rừng; bốn nữ hộ vệ có cánh khỏa thân duyên dáng ngả người mềm mại ở bốn góc.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng hổ phách gợn sóng mềm, buông lơi, đội vòng nguyệt quế thiên giới tinh tế; Vóc dáng: nữ hộ vệ có cánh duyên dáng, mềm mại và thanh thản, đường cong được tạo khối nhẹ nhàng, phong thái dịu dàng và mơ màng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm, được nhân sư trên đỉnh bánh xe cầm dựng thẳng; không có lưỡi kiếm nào khác ở bất kỳ đâu trên lá bài. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 12. JUSTICE — Công Lý

File: [11-justice.txt](11-justice.txt) · Nguồn: `prompts/out6/11-justice.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "JUSTICE" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng khỏa thân cao đẹp như tượng, một tay cầm kiếm dựng thẳng, tay kia cầm chiếc cân thăng bằng, ngồi trên ngai đá giữa các cột.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen như cánh quạ, óng mượt, vuốt gọn ra sau và buộc nửa đầu cao, bóng mịn; Vóc dáng: cao đẹp như tượng và vương giả, xương quai xanh nổi bật, lưng thẳng, tư thế nghiêm nghị và cân bằng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm, được cầm dựng thẳng trong tay trái của nàng; không có lưỡi kiếm nào khác trên lá bài. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 13. THE HANGED — Người Treo Ngược

File: [12-hanged.txt](12-hanged.txt) · Nguồn: `prompts/out6/12-hanged.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE HANGED" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ 21 tuổi khỏa thân, thanh thản bị treo ngược bằng một cổ chân trên một cây sống có hình thập tự, một chân gập duyên dáng; vầng hào quang vàng rực sáng quanh đầu nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: những lọn tóc nâu vàng rối nhẹ đổ xuống theo trọng lực, tỏa sáng trong ánh sáng huyền ảo; Vóc dáng: vóc dáng nữ vũ công trẻ thon gọn, mềm dẻo và linh hoạt, tư thế thanh thản và yên bình; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 14. DEATH — Cái Chết

File: [13-death.txt](13-death.txt) · Nguồn: `prompts/out6/13-death.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "DEATH" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một hình tượng nữ 22 tuổi khỏa thân, da nhợt, nổi bật, cưỡi chiến mã đen điềm tĩnh, cầm lá cờ đen trang trí một bông hồng trắng năm cánh; ánh bình minh vàng rực lên giữa hai tòa tháp song đôi ở xa.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài màu bạch kim trắng ngà như xương, buông xõa tự do; Vóc dáng: dáng nữ cao, mảnh mai và đầy uy lực, được quấn trong lớp lụa đen mỏng xuyên thấu; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 15. TEMPERANCE — Tiết Độ

File: [14-temperance.txt](14-temperance.txt) · Nguồn: `prompts/out6/14-temperance.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TEMPERANCE" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một hình tượng có cánh khỏa thân duyên dáng, tóc dài buông xõa, ngồi thanh nhã trên tảng đá phủ rêu bên hồ, một chân thả xuống nước; bàn tay giơ cao nghiêng một chén thánh bằng vàng để rót, tay còn lại cầm chén thánh vàng thứ hai đặt ngay dưới miệng chén trên sao cho miệng chén dưới hứng được dòng nước; một dòng nước duy nhất, trơn mượt và liền mạch, chảy thẳng xuống từ chén nghiêng phía trên và rơi vào lòng chén phía dưới; hoa diên vĩ nở quanh hồ, ánh sáng nâu sepia và vàng đất ấm áp.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng tro nhạt, mảnh và nhẹ, bay lơ lửng như không trọng lượng trong không trung; Vóc dáng: nhẹ như không thực và thanh mảnh như liễu, tay chân dài thon, cột sống uốn cong mềm dẻo, phong thái thiên thần duyên dáng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 chén thánh): đúng hai chén thánh, mỗi tay cầm một chén, phần bầu của cả hai chén đều nhìn thấy trọn vẹn và không bị che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 16. THE DEVIL — Ác Quỷ

File: [15-devil.txt](15-devil.txt) · Nguồn: `prompts/out6/15-devil.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE DEVIL" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ đại ác quỷ khỏa thân có sừng và cánh đứng trên bệ tối; bên cạnh là hai phụ nữ trẻ khỏa thân quyến rũ, uốn cong người trong những sợi xích vàng, cơ thể họ tỏa sáng trong bóng tối có ánh nến bên trong hang đá thủy tinh núi lửa đen.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen như đêm khuya, gợn sóng với sắc đỏ rượu vang đậm ẩn bên dưới, hoang dại và không thuần phục; Vóc dáng: nồng nàn và nhiều đường cong, lưng uốn cong, hông đầy mềm mại, thần thái cuốn hút đầy mê hoặc; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 17. THE TOWER — Tòa Tháp

File: [16-tower.txt](16-tower.txt) · Nguồn: `prompts/out6/16-tower.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE TOWER" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một tòa tháp đá cao bị tia sét ngoằn ngoèo đánh trúng, vương miện vàng trên đỉnh tháp đổ xuống trong lửa; hai phụ nữ trẻ trưởng thành khỏa thân, duyên dáng, rơi giữa bão tố và tro bụi, cơ thể họ được tia chớp chói lòa chiếu sáng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ tối như giông bão bị luồng gió sấm sét thổi mạnh ra phía sau; Vóc dáng: căng chắc và thể thao, vóc dáng nhào lộn đầy chuyển động, uốn cong giữa lúc rơi; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 18. THE STAR — Ngôi Sao

File: [17-the-star.txt](17-the-star.txt) · Nguồn: `prompts/out6/17-the-star.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE STAR" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ khỏa thân đứng trong hồ nước trong veo vào ban đêm, nước ngập đến eo; cơ thể nàng ngả cong ra sau và xoay ba phần tư về phía người xem, tóc ướt đổ xuống lưng, cả hai tay giơ lên rót nước từ hai chiếc bình, một đầu gối nâng lên; phía trên có một ngôi sao tám cánh lớn và bảy ngôi sao nhỏ hơn.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng nhạt óng ánh rất dài, ướt và mượt như lụa, đổ xuống quá một bên vai trần; Vóc dáng: mảnh mai và mềm dẻo, eo nhỏ, chân dài duyên dáng, tỷ lệ hình thể thiếu nữ trưởng thành rạng rỡ; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 bình rót nước): đúng hai bình rót nước, mỗi tay cầm một bình, cả hai đều nhìn thấy trọn vẹn. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 19. THE MOON — Mặt Trăng

File: [18-moon.txt](18-moon.txt) · Nguồn: `prompts/out6/18-moon.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE MOON" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một vầng trăng nhợt có gương mặt thanh thản đang nhỏ sương, hai tòa tháp và một con đường quanh co; một nữ thần nước khỏa thân trồi lên từ hồ tối, nước chảy qua vai trần; một con sói và một con chó đang tru, một con tôm càng ở trong nước.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen ánh xanh mực với những điểm bắt sáng bạc lạnh, đổ xuống hông như dòng nước; Vóc dáng: dáng nữ thần nước mảnh mai, bí ẩn, eo thanh tú, hông cong mềm mại; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 20. THE SUN — Mặt Trời

File: [19-sun.txt](19-sun.txt) · Nguồn: `prompts/out6/19-sun.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE SUN" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân vui tươi, đội vòng hoa đỏ, cưỡi ngựa trắng điềm tĩnh, thân trên để trần xoay về phía ánh sáng; lá cờ đỏ tung bay, mặt trời rạng rỡ có gương mặt hiền hòa, một bức tường thấp điểm hoa hướng dương.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 19 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng rực như hoa hướng dương, những lọn tóc xõa bồng bềnh được kết hoa đỏ; Vóc dáng: trẻ trung và đầy sức sống, làn da rám nắng, đường cong nữ tính tràn năng lượng và niềm vui; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 21. JUDGEMENT — Phán Xét

File: [20-judgement.txt](20-judgement.txt) · Nguồn: `prompts/out6/20-judgement.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "JUDGEMENT" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ thiên thần có cánh khỏa thân, thanh thản, tỏa ánh sáng ấm, nhẹ nhàng nâng chiếc kèn đồng màu vàng có lá cờ trắng; bên dưới, ba phụ nữ trẻ khỏa thân xinh đẹp trỗi dậy từ mặt nước yên ả, đôi tay mở nhẹ và xoay về ánh sáng thần thánh — một người da sáng với tóc vàng buông dài, một người có tông da ấm với tóc xoăn nâu đỏ đậm, một người da sáng với tóc xoăn sẫm màu lọn nhỏ — mỗi người có gương mặt và vóc dáng riêng biệt.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc màu hổ phách pha mật ong đậm, gợn sóng mềm và sáng, bắt những tia vàng dịu; Vóc dáng: thiên thần có cánh duyên dáng, mềm mại và thanh thản, đường cong được tạo khối nhẹ nhàng, phong thái dịu dàng và khích lệ tinh thần; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 22. THE WORLD — Thế Giới

File: [21-world.txt](21-world.txt) · Nguồn: `prompts/out6/21-world.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THE WORLD" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ vũ công trưởng thành khỏa thân, thanh thản tạo dáng duyên dáng với đường cong nhẹ, một bên hông đưa ra mềm mại và một đầu gối nâng nhẹ; cơ thể thả lỏng, đầu ngả ra sau, mỗi tay cầm nhẹ một cây gậy mảnh, nhảy múa bên trong vòng nguyệt quế lớn hình bầu dục; tại các góc có một thiên thần, một đại bàng, một sư tử và một bò đực.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ pha sô-cô-la sẫm, gợn sóng mềm và buông xõa, trôi nhẹ cùng các dải lụa trắng; Vóc dáng: vóc dáng vũ công duyên dáng, mềm mại và thanh thản, đường cong nhẹ nhàng, tư thế mềm dẻo và dịu dàng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 cây gậy): đúng hai cây gậy, mỗi bàn tay nắm một cây, cả hai thân gậy đều nhìn rõ từ bàn tay đến đầu gậy. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

---

<a id="nhom-wands"></a>

## Gậy — 14 lá

### 23. ACE OF WANDS — Át Gậy

File: [wands-ace.txt](wands-ace.txt) · Nguồn: `prompts/out6/wands-ace.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "ACE OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một bàn tay thần thánh mang nét nữ tính duyên dáng, để trần, vươn ra từ những đám mây mềm, trao một cây gậy sống duy nhất đang nảy mầm; bên dưới là cảnh quan yên bình và một tòa lâu đài xa.

KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 cây gậy): đúng một cây gậy còn sống, đang nảy mầm, được bàn tay thần thánh cầm; không có cây gậy thứ hai ở bất kỳ đâu, kể cả trong cảnh quan. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 24. TWO OF WANDS — Hai Gậy

File: [wands-02.txt](wands-02.txt) · Nguồn: `prompts/out6/wands-02.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TWO OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ quý tộc khỏa thân, thanh thản đứng trên lũy thành, một quả địa cầu đặt trong lòng bàn tay, mắt nàng cúi xuống nhìn nó; tay kia cầm một cây gậy dựng thẳng, cây gậy thứ hai được gắn trên bức tường phía sau.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu đỏ đậm buông thành những lọn xoăn dài, lỏng qua một vai; Vóc dáng: mảnh mai, thanh thản và trầm tư, tư thế đứng nhẹ nhàng, nhìn ra từ lan can thành; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 cây gậy): đúng hai cây gậy: một cây được cầm dựng thẳng trong tay phải của nàng, một cây gắn thẳng đứng trên lũy đá bên trái nàng — 1 + 1 = 2; cả hai thân gậy đều nguyên vẹn từ gốc đến ngọn, không bắt chéo nhau. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 25. THREE OF WANDS — Ba Gậy

File: [wands-03.txt](wands-03.txt) · Nguồn: `prompts/out6/wands-03.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THREE OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ thương nhân khỏa thân, thanh thản, được nhìn từ phía sau trên mũi đất đá cao, đứng thẳng và quay đường lưng dài về phía người xem; một tay đặt cao trên cây gậy bên cạnh, tay kia giơ lên che mắt khi nàng nhìn xa ra biển; ba cây gậy cắm thẳng thành hàng quanh nàng, những thuyền buồm trên mặt biển vàng óng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu caramel ấm được tết lỏng cùng sợi dây vàng; Vóc dáng: cao và đẹp như tượng, đường lưng dài hướng về chân trời; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 3 cây gậy): đúng ba cây gậy cắm thẳng đứng thành một hàng chéo thẳng duy nhất ngang tiền cảnh, cách đều và tách xa nhau; cả ba đầu gậy đều tách rõ khỏi đường chân trời, không cây nào che lấp hay bắt chéo cây khác — đếm từ trái sang phải: 1, 2, 3. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 26. FOUR OF WANDS — Bốn Gậy

File: [wands-04.txt](wands-04.txt) · Nguồn: `prompts/out6/wands-04.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FOUR OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: bốn cây gậy kết hoa tạo thành mái che lễ hội; bên dưới, hai phụ nữ trẻ khỏa thân duyên dáng nhảy múa nhẹ nhàng, cả hai đều có tông da sáng — một người da trắng sứ với tóc vàng mật ong buông dài, một người da trắng ngà ửng hồng với tóc nâu đỏ đậm uốn lọn, mỗi người có gương mặt và vóc dáng riêng — phía xa là một dinh thự.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: riêng biệt cho từng vũ công: một người tóc vàng mật ong buông dài, một người tóc đen xoăn cuộn chặt; Vóc dáng: cả hai đều mềm dẻo và hân hoan, vòng eo vũ công vui tươi, cánh tay giơ lên duyên dáng, gương mặt và vóc dáng riêng biệt; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 4 cây gậy): đúng bốn cây gậy làm bốn cột góc của mái che — hai bên trái, hai bên phải — 2 + 2 = 4; vẽ hai cột phía sau cao hơn một chút so với hai cột phía trước để không cột nào bị che bởi cột khác; cả bốn thân gậy đều nhìn thấy trọn vẹn từ mặt đất đến đầu gậy, các đầu gậy nối với nhau bằng một dây kết hoa. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 27. FIVE OF WANDS — Năm Gậy

File: [wands-05.txt](wands-05.txt) · Nguồn: `prompts/out6/wands-05.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FIVE OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: năm phụ nữ trẻ khỏa thân duyên dáng đứng thành vòng tròn thưa trên đồng cỏ mềm, mỗi người khác biệt và tất cả đều có tông da sáng — một người da trắng sứ với tóc dài vàng bạch kim, một người da trắng ngà ửng hồng với tóc đỏ đồng gợn sóng, một người da trắng ngà ấm với tóc nâu sô-cô-la đậm, một người da sáng với tóc thẳng đen như cánh quạ, một người da vàng nhạt với tóc vàng ánh dâu — mỗi người cầm đúng một cây gậy cắm thẳng bên cạnh.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: riêng biệt cho từng người: một người tóc vàng, một người tóc nâu đỏ đậm uốn lọn, một người tóc đen xoăn cuộn chặt, một người tóc đen thẳng, một người tóc màu đồng gợn sóng; Vóc dáng: tất cả đều mảnh mai, duyên dáng và nhẹ nhàng, gương mặt và vóc dáng riêng biệt, tư thế nhảy múa dịu dàng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 5 cây gậy): tổng cộng đúng năm cây gậy, mỗi người trong năm phụ nữ nắm đúng một cây trong tay — năm phụ nữ, năm cây gậy, mỗi người một cây; không ai cầm hai cây, không có gậy thừa trên mặt đất, không có gậy tựa ở bất kỳ đâu, không có gậy trong hậu cảnh — đếm các cây gậy: 1, 2, 3, 4, 5 và không thêm cây nào. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 28. SIX OF WANDS — Sáu Gậy

File: [wands-06.txt](wands-06.txt) · Nguồn: `prompts/out6/wands-06.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SIX OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ khỏa thân, thanh thản ngồi trên ngựa trắng, trán đội vòng nguyệt quế, nhẹ nhàng giơ một cây gậy gắn vòng nguyệt quế trong tay; phía sau là năm nữ tùy tùng trưởng thành khỏa thân ngưỡng mộ nàng, mỗi người cầm một cây gậy.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng mật ong nhẹ nhàng bay trong gió; Vóc dáng: duyên dáng, đĩnh đạc và thanh thản, tư thế cưỡi ngựa thanh lịch; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 6 cây gậy): đúng sáu cây gậy: một cây gậy gắn vòng nguyệt quế được nữ anh hùng giơ cao trong tay, cộng năm cây do năm người đi theo phía sau cầm — 1 + 5 = 6; mỗi người đi theo cầm gậy thẳng đứng và cao hơn vai rõ rệt để cả năm cây đều có thể đếm riêng trên nền trời, không có gậy tựa trên vai. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 29. SEVEN OF WANDS — Bảy Gậy

File: [wands-07.txt](wands-07.txt) · Nguồn: `prompts/out6/wands-07.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SEVEN OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân, thanh thản đứng trên đỉnh mỏm đá cao, nhẹ nhàng cầm một cây gậy lớn bằng cả hai tay; sáu cây gậy vươn lên từ phía dưới.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu cà phê đậm buông thành những lọn xoăn mềm, lỏng; Vóc dáng: mảnh mai, thanh thản và duyên dáng, tư thế bình tĩnh và điềm đạm; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 7 cây gậy): đúng bảy cây gậy: một cây được người phụ nữ trẻ cầm bằng hai tay, cộng sáu cây vươn lên từ dưới mép vực trước mặt nàng — 1 + 6 = 7; sáu đầu gậy phía dưới cách đều dọc theo đường mép vực, không chồng lấp nhau. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 30. EIGHT OF WANDS — Tám Gậy

File: [wands-08.txt](wands-08.txt) · Nguồn: `prompts/out6/wands-08.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "EIGHT OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: tám cây gậy có chồi lá ở ngọn lướt thành một hàng chéo song song duy nhất qua bầu trời thoáng dịu, hướng về thị trấn ven sông phía dưới.

KHÓA SỐ LƯỢNG (CHÍNH XÁC 8 cây gậy): đúng tám cây gậy trong MỘT hàng chéo song song duy nhất trên bầu trời rộng — 1 hàng gồm 8 cây, cách đều, cả tám cùng hướng, không bắt chéo, không cây nào bị mép tranh cắt mất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 31. NINE OF WANDS — Chín Gậy

File: [wands-09.txt](wands-09.txt) · Nguồn: `prompts/out6/wands-09.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "NINE OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân, thanh thản đặt nhẹ hai tay lên một cây gậy dựng đứng; phía sau nàng, tám cây gậy đứng thẳng như hàng rào cọc.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu sẫm buông xõa thành những gợn sóng mềm; Vóc dáng: mảnh mai, thanh thản và cảnh giác, tư thế nhẹ nhàng, điềm đạm; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 9 cây gậy): đúng chín cây gậy: tám cây cắm thẳng thành một hàng rào cọc thẳng PHÍA SAU nàng, cách đều và không bị cơ thể nàng che, cộng một cây nàng cầm phía trước — 8 + 1 = 9; cả chín cây đều đếm được trên nền trời rộng. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 32. TEN OF WANDS — Mười Gậy

File: [wands-10.txt](wands-10.txt) · Nguồn: `prompts/out6/wands-10.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TEN OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ 23 tuổi khỏa thân, thanh thản ngả người duyên dáng trên cỏ mềm, nghỉ bên một tảng đá lớn; tựa vào tảng đá phía sau nàng là một bó tự nhiên gồm mười cây gậy gỗ dài được buộc lỏng ở giữa bằng sợi dây mảnh, các đầu trên xòe ra tự nhiên như chiếc quạt tay đang mở; mọi cây gậy có cùng chiều dài và độ dày, cách đều với khoảng trời rõ ràng giữa từng thân gậy, cả mười đầu gậy đều tách biệt và đếm được, các đầu dưới chụm lại trong cỏ, không bắt chéo, không bị che khuất; phía xa có một tòa lâu đài ngập nắng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ buông xõa thành những gợn sóng mềm; Vóc dáng: mảnh mai, duyên dáng và thanh thản, phong thái nhẹ nhàng khi mang bó gậy; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 10 cây gậy): đúng mười cây gậy trong một bó tự nhiên buộc ở giữa — đếm mười đầu gậy xòe hình quạt: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10; không phải chín, không phải mười một. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 33. PAGE OF WANDS — Hầu Cận Gậy

File: [wands-page.txt](wands-page.txt) · Nguồn: `prompts/out6/wands-page.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "PAGE OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hầu cận trưởng thành khỏa thân, thanh thản đứng lùi xa hơn trong cảnh quan để toàn thân nàng trông nhỏ hơn trong quang cảnh sa mạc rộng lớn, cầm một cây gậy sống; phía sau là các đụn cát sa mạc và kim tự tháp.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 18 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc ngắn kiểu bob màu nâu đỏ ánh gừng mềm mại, tạo lớp nhẹ nhàng; Vóc dáng: nhỏ nhắn và thanh thản, vóc dáng trẻ trung mềm dẻo, tư thế dịu dàng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 cây gậy): đúng một cây gậy sống; không có cây gậy thứ hai, không có gậy trang trí trong các đụn cát. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 34. KNIGHT OF WANDS — Kỵ Sĩ Gậy

File: [wands-knight.txt](wands-knight.txt) · Nguồn: `prompts/out6/wands-knight.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KNIGHT OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ kỵ sĩ 22 tuổi khỏa thân, thanh thản cưỡi ngựa trắng tinh điềm tĩnh đang chạy nước kiệu về phía trước, đưa một cây gậy sống xanh tốt ra trước mặt; phía sau là đồng cỏ vàng và các ngọn đồi xa.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu vàng uốn lọn mềm, buông lơi dưới vòng miện lông vũ tinh tế; Vóc dáng: nữ kỵ sĩ mảnh mai, duyên dáng và thanh thản trên tuấn mã trắng tinh điềm tĩnh, gần như để trần với chỉ một mảnh lụa mỏng xuyên thấu; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 cây gậy): đúng một cây gậy, được nàng nhẹ nhàng giơ trong tay; không có cây gậy nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 35. QUEEN OF WANDS — Hoàng Hậu Gậy

File: [wands-queen.txt](wands-queen.txt) · Nguồn: `prompts/out6/wands-queen.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "QUEEN OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng khỏa thân, thanh thản, tóc sẫm màu buông xõa, ngồi trên ngai chạm sư tử, nhẹ nhàng cầm một cây gậy hoa hướng dương, một con mèo đen ở dưới chân; ngai đặt bên rìa rừng bạch dương mùa xuân tươi sáng — những thân bạch dương trắng mảnh, tầng cây thấp xanh dịu và thảm hoa dại xen hoa hướng dương, ánh nắng lốm đốm xuyên qua lá non.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: mái tóc bồng bềnh lộng lẫy màu nâu đỏ đậm, gợn sóng mềm mại buông xuống vai; Vóc dáng: đầy đặn, thanh thản và ấm áp, tư thế nhẹ nhàng, đĩnh đạc trên ngai sư tử; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 cây gậy): đúng một cây gậy hoa hướng dương; không có cây gậy nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 36. KING OF WANDS — Vua Gậy

File: [wands-king.txt](wands-king.txt) · Nguồn: `prompts/out6/wands-king.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KING OF WANDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ quân vương 25 tuổi khỏa thân, thanh thản, đội vương miện chạm sư tử và ngồi trên ngai chạm ngọn lửa, nhẹ nhàng cầm một cây gậy đang nở hoa; ngai đặt trong khoảng rừng thưa giữa khu rừng sồi cổ thụ hùng vĩ — những thân sồi tối màu cao vút, ánh nắng vàng ấm xuyên qua tán lá dày, các tia sáng hổ phách và tàn lửa vàng trôi giữa những thân cây.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 25 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc màu đồng sẫm vuốt ra sau, tết thành vòng miện mềm, đan cùng các dải ruy băng cam rực như lửa; Vóc dáng: nữ đại vương duyên dáng, thanh thản và cao quý, phong thái mềm mại, dịu dàng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 cây gậy): đúng một cây gậy xanh còn sống; không có cây gậy nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

---

<a id="nhom-cups"></a>

## Cốc — 14 lá

### 37. ACE OF CUPS — Át Cốc

File: [cups-ace.txt](cups-ace.txt) · Nguồn: `prompts/out6/cups-ace.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "ACE OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một bàn tay thần thánh trao một chén thánh trang trí cầu kỳ, một con chim bồ câu đáp xuống, năm dòng nước tràn ra đổ vào hồ hoa súng.

KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 chén thánh): đúng một chén thánh; năm dòng tràn ra là nước, không phải cốc — không vẽ thêm chén thánh trong hồ. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 38. TWO OF CUPS — Hai Cốc

File: [cups-02.txt](cups-02.txt) · Nguồn: `prompts/out6/cups-02.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TWO OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: hai phụ nữ trẻ trưởng thành khỏa thân đứng đối diện nhau, một người xoay ba phần tư cơ thể về phía người xem với một cánh tay vắt ngang ngực; mỗi người nâng một chén thánh để chúc mừng, phía trên họ là quyền trượng caduceus với đầu sư tử.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu tro mềm được tết đan thấp theo kiểu lãng mạn; Vóc dáng: mảnh mai và duyên dáng, đường nét cong nhẹ nhàng, nghiêng người trong sự gắn kết; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 chén thánh): đúng hai chén thánh, mỗi người yêu nâng một chén trong tay, một chén bên trái và một chén bên phải; phần bầu của cả hai chén đều nhìn thấy trọn vẹn và không chồng lấp — không có chiếc cốc thứ ba. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 39. THREE OF CUPS — Ba Cốc

File: [cups-03.txt](cups-03.txt) · Nguồn: `prompts/out6/cups-03.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THREE OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: ba thiếu nữ trưởng thành khỏa thân đội vòng hoa nhảy múa thành vòng tròn, cơ thể hướng về ánh sáng, mỗi người giơ một chén thánh; trái cây nằm trên mặt đất.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: ba cô gái lần lượt có tóc nâu sô-cô-la đậm, vàng óng và màu đồng; Vóc dáng: hài hòa, nhiều đường cong, cùng nhảy múa với nét duyên dáng nữ tính vui tươi; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 3 chén thánh): đúng ba chén thánh — mỗi người trong ba cô gái giơ một chén, ba vũ công và ba chiếc cốc, mỗi nhân vật một chén; phần bầu của cả ba chén đều được nâng cao hơn vai và có thể đếm được. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 40. FOUR OF CUPS — Bốn Cốc

File: [cups-04.txt](cups-04.txt) · Nguồn: `prompts/out6/cups-04.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FOUR OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân, trầm tư ngồi dưới gốc cây, khoanh tay nhìn ba chiếc cốc trên cỏ, trong khi một bàn tay thiên giới đưa ra chiếc cốc thứ tư từ đám mây.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc sẫm màu gợn sóng buông qua vai trong vẻ trầm tư; Vóc dáng: mảnh mai, tư thế ngồi thư giãn tựa vào một cây đang nở hoa; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 4 chén thánh): đúng bốn chén thánh: ba chén đứng thẳng thành một hàng trên cỏ trước mặt nhân vật, cách đều, cộng một chén được bàn tay từ đám mây đưa ra — 3 + 1 = 4; phần bầu của cả bốn chén đều nhìn thấy rõ. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 41. FIVE OF CUPS — Năm Cốc

File: [cups-05.txt](cups-05.txt) · Nguồn: `prompts/out6/cups-05.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FIVE OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trưởng thành hư cấu trong thế giới kỳ ảo, khỏa thân và duyên dáng, cúi người đứng bên sông, quay lưng về phía ánh sáng; ba chén thánh bị đổ, rỗng và úp ngược nằm ở tiền cảnh dưới chân nàng, hai chén thánh đầy vẫn đứng thẳng trên bờ phía sau nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài màu nâu đỏ gỗ gụ buông xõa; Vóc dáng: dáng người mảnh mai, trầm buồn, cổ thanh tú cúi nhẹ; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 5 chén thánh): đúng năm chén thánh: ba chén đã đổ và rỗng nằm ở tiền cảnh, cộng hai chén vẫn đứng thẳng và đầy trên bờ phía sau nàng — 3 + 2 = 5; phần bầu của cả năm chén đều đếm được, không chén nào bị nhân vật hoặc cảnh quan che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 42. SIX OF CUPS — Sáu Cốc

File: [cups-06.txt](cups-06.txt) · Nguồn: `prompts/out6/cups-06.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SIX OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: hai phụ nữ trẻ trưởng thành hư cấu trong thế giới kỳ ảo, khỏa thân và duyên dáng, ở khu vườn trong sân cổ, trao nhau một chén thánh đầy hoa; năm chén khác đặt dọc bức tường phía sau họ.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 19 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng nhạt búi thành vòng miện thiếu nữ tinh tế; Vóc dáng: nhỏ nhắn, hồn nhiên và thanh tú, tư thế ngọt ngào, dịu dàng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 6 chén thánh): đúng sáu chén thánh, mỗi chén đều đầy hoa: một chén đang được trao giữa hai người, cộng năm chén đứng thành một hàng dọc bức tường sân phía sau họ — 1 + 5 = 6; phần bầu của cả sáu chén đều tách biệt và đếm được. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 43. SEVEN OF CUPS — Bảy Cốc

File: [cups-07.txt](cups-07.txt) · Nguồn: `prompts/out6/cups-07.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SEVEN OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân, mê mẩn, được nhìn từ phía sau, kinh ngạc ngắm bảy chiếc cốc chứa các báu vật huyền bí, lơ lửng giữa những đám mây phát sáng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen như cánh quạ uốn lọn, trôi trong làn sương huyền bí; Vóc dáng: mảnh mai, tư thế mê mẩn với hai tay hơi nâng lên; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 7 chén thánh): đúng bảy chén thánh trên MỘT đám mây phát sáng, xếp thành hai hàng rõ ràng: 4 chén ở hàng dưới và 3 chén ở hàng trên — 4 + 3 = 7; cách đều trên nền trời thoáng, phần bầu mỗi chén đều tách biệt và không bị che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 44. EIGHT OF CUPS — Tám Cốc

File: [cups-08.txt](cups-08.txt) · Nguồn: `prompts/out6/cups-08.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "EIGHT OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân đơn độc cầm gậy bước đi, bỏ lại tám chiếc cốc xếp chồng phía sau để lên đường về những đỉnh núi phủ sương dưới ánh trăng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu đậm được giấu dưới áo choàng du hành; Vóc dáng: dáng lữ khách thon gọn, lưng quay dứt khoát về phía núi; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 8 chén thánh): đúng tám chén thánh xếp chồng trên gờ đá theo bố cục 3 + 3 + 2, có một khoảng trống rõ ràng giữa chén thứ sáu và thứ bảy — 3 + 3 + 2 = 8; phần bầu của cả tám chén đều đếm được, không chén nào bị mép tranh cắt mất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 45. NINE OF CUPS — Chín Cốc

File: [cups-09.txt](cups-09.txt) · Nguồn: `prompts/out6/cups-09.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "NINE OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trưởng thành khỏa thân, mãn nguyện ngồi ở bàn tiệc, trước chín chén thánh vàng được bày đầy tự hào thành ô lưới gọn gàng trên kệ phía sau nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu mật ong ấm búi lỏng, thư thái; Vóc dáng: đường cong nữ tính mềm mại, sang trọng, tư thế ngồi mãn nguyện và mỉm cười; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 9 chén thánh): đúng chín chén thánh trên kệ phía sau nhân vật, xếp thành ô lưới gọn gàng 3 x 3 — ba hàng, mỗi hàng ba chén, 3 + 3 + 3 = 9; cách đều, phần bầu của cả chín chén đều nhìn thấy trọn vẹn. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 46. TEN OF CUPS — Mười Cốc

File: [cups-10.txt](cups-10.txt) · Nguồn: `prompts/out6/cups-10.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TEN OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: hai phụ nữ trưởng thành khỏa thân ôm nhau trên đồng cỏ, một người hướng đường lưng dài về phía ánh sáng, người kia vòng tay ôm eo nàng; mười chén thánh nằm dọc một vòng cung cầu vồng; phía xa có ngôi nhà nhỏ và trẻ em đang nhảy múa.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt phỉ ấm đổ xuống thành những gợn mềm như lụa; Vóc dáng: phong thái người mẹ duyên dáng, dịu dàng, vóc dáng mảnh mai đầy yêu thương; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 10 chén thánh): đúng mười chén thánh dọc theo MỘT vòng cung cầu vồng — 4 chén ở nửa trái, 4 chén ở nửa phải, 2 chén ở đỉnh cung — 4 + 4 + 2 = 10; cách đều trên nền trời thoáng, phần bầu của cả mười chén đều đếm được. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 47. PAGE OF CUPS — Hầu Cận Cốc

File: [cups-page.txt](cups-page.txt) · Nguồn: `prompts/out6/cups-page.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "PAGE OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hầu cận trẻ khỏa thân duyên dáng đứng bên biển, cầm một chén thánh, từ trong chén có một con cá tò mò nhìn ra.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 18 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc sẫm màu bóng mượt, tết thành một bím đuôi cá lệch bên, vắt qua xương quai xanh; Vóc dáng: nhỏ nhắn, tò mò và mơ mộng, tay chân thanh tú, đang cầm chén thánh; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 chén thánh): đúng một chén thánh; không có chiếc cốc nào khác ở bất kỳ đâu trong cảnh. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 48. KNIGHT OF CUPS — Kỵ Sĩ Cốc

File: [cups-knight.txt](cups-knight.txt) · Nguồn: `prompts/out6/cups-knight.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KNIGHT OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ kỵ sĩ 22 tuổi khỏa thân duyên dáng, cưỡi tuấn mã trắng điềm tĩnh bên dòng suối, đưa ra một chén thánh vàng của hòa bình.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng cát nhạt buông thành những gợn sóng mềm, lãng mạn ngang trán; Vóc dáng: nữ kỵ sĩ nên thơ, mảnh mai, cao quý và có vóc dáng thể thao, đang trao chén thánh; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 chén thánh): đúng một chén thánh vàng; không có chiếc cốc nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 49. QUEEN OF CUPS — Hoàng Hậu Cốc

File: [cups-queen.txt](cups-queen.txt) · Nguồn: `prompts/out6/cups-queen.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "QUEEN OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng trưởng thành trẻ trung khỏa thân ngồi trên ngai vỏ sò sát mép nước, đôi vai trần dưới mái tóc vàng bạch kim ướt, cầm một chén thánh vàng có nắp trong lòng; phía sau là bọt biển và những đợt sóng vỡ.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài vàng bạch kim óng ánh, buông thẳng như nước đến đùi; Vóc dáng: mảnh mai và nhẹ như không thực, eo nhỏ, vẻ đẹp nữ hoàng thanh thản và huyền bí; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 chén thánh): đúng một chén thánh vàng có nắp; không có chiếc cốc nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 50. KING OF CUPS — Vua Cốc

File: [cups-king.txt](cups-king.txt) · Nguồn: `prompts/out6/cups-king.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KING OF CUPS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng biển cả 25 tuổi khỏa thân, thanh thản ngồi trên ngai nổi giữa những đợt sóng cuộn, cầm quyền trượng hoa sen và một chiếc cốc vàng; phía xa có cá heo đang nhảy lên.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 25 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu cà phê đậm uốn sóng sâu, đội vương miện vàng biển và ngọc trai; Vóc dáng: nữ quân vương biển cả điềm tĩnh, cao đẹp như tượng, thần thái thanh thản và cao quý; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 chén thánh): đúng một chén thánh; không có chiếc cốc nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

---

<a id="nhom-swords"></a>

## Kiếm — 14 lá

### 51. ACE OF SWORDS — Át Kiếm

File: [swords-ace.txt](swords-ace.txt) · Nguồn: `prompts/out6/swords-ace.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "ACE OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một bàn tay thần thánh nắm một thanh kiếm dựng thẳng, một vương miện nạm đá quý lơ lửng ở mũi kiếm; phía dưới là những đỉnh núi khô cằn.

KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm, dựng thẳng trong bàn tay thần thánh; không có lưỡi kiếm thứ hai ở bất kỳ đâu. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 52. TWO OF SWORDS — Hai Kiếm

File: [swords-02.txt](swords-02.txt) · Nguồn: `prompts/out6/swords-02.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TWO OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trưởng thành khỏa thân bịt mắt, ngồi trên ghế đá bên biển, hai thanh kiếm dài bắt chéo trước ngực; mặt trăng đang mọc phía sau nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen tuyền vuốt gọn ra sau, búi cao mượt mà và hoàn hảo; Vóc dáng: mảnh mai, cân bằng hoàn hảo, vùng thân giữa săn chắc, hai tay bắt chéo cầm hai lưỡi kiếm; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 thanh kiếm): đúng hai lưỡi kiếm dài tạo thành một hình chữ X duy nhất trước ngực nàng, mỗi bên vai có một lưỡi kiếm; không có lưỡi kiếm thứ ba, không có dao găm ở thắt lưng. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 53. THREE OF SWORDS — Ba Kiếm

File: [swords-03.txt](swords-03.txt) · Nguồn: `prompts/out6/swords-03.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THREE OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một trái tim lớn có hình dạng giải phẫu thực, bị ba thanh kiếm đâm xuyên; phía sau là mưa và mây giông.

KHÓA SỐ LƯỢNG (CHÍNH XÁC 3 thanh kiếm): đúng ba thanh kiếm xuyên qua một trái tim — một thanh thẳng đứng từ phía trên, hai thanh nghiêng từ trái và phải; ba chuôi kiếm tách biệt, đếm được rõ ràng trên nền trời giông bão, 1, 2, 3. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 54. FOUR OF SWORDS — Bốn Kiếm

File: [swords-04.txt](swords-04.txt) · Nguồn: `prompts/out6/swords-04.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FOUR OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trưởng thành khỏa thân duyên dáng nằm nghỉ trên mộ đá trong nhà nguyện, hai tay chắp lại; ba thanh kiếm gắn trên tường phía trên nàng và một thanh nằm bên dưới; phía sau là cửa sổ kính màu.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen nâu sẫm trải gọn quanh đầu nàng đang tựa nghỉ trên đá; Vóc dáng: mảnh mai, dáng nằm yên bình như tượng trên mộ trong sự tĩnh lặng linh thiêng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 4 thanh kiếm): đúng bốn thanh kiếm: ba thanh gắn nằm ngang trên tường phía trên nhân vật, xếp chồng thành một dãy gồm 3 thanh, cộng một thanh nằm phẳng trên phiến mộ bên dưới nhân vật — 3 + 1 = 4; cả bốn lưỡi kiếm đều nguyên vẹn và đếm được. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 55. FIVE OF SWORDS — Năm Kiếm

File: [swords-05.txt](swords-05.txt) · Nguồn: `prompts/out6/swords-05.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FIVE OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân tự tin mang ba thanh kiếm trên vai, nhìn hai nữ đồng hành trưởng thành khỏa thân đang rút lui trên bờ biển giông bão; hai thanh kiếm nằm trên cát.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu sẫm bị gió thổi tung, đi cùng nụ cười nhếch nhẹ đầy tự tin; Vóc dáng: thon gọn, nhanh nhẹn, vai góc cạnh, xoay người với những lưỡi kiếm đã thu gom; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 5 thanh kiếm): đúng năm thanh kiếm: ba thanh được người chiến thắng gom trong tay, giữ thẳng đứng và xòe ra để cả ba chuôi kiếm tách biệt, cộng hai thanh bị bỏ lại trên cát phía sau nhân vật — 3 + 2 = 5. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 56. SIX OF SWORDS — Sáu Kiếm

File: [swords-06.txt](swords-06.txt) · Nguồn: `prompts/out6/swords-06.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SIX OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trưởng thành khỏa thân và một hành khách trẻ em đang được người lái đò chống thuyền đưa qua sông; sáu thanh kiếm dựng thẳng dọc thuyền.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu tro nhạt được gom nhẹ trong tấm voan mờ như sương; Vóc dáng: dáng hành khách mảnh mai, yên lặng ngồi trong thuyền đò; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 6 thanh kiếm): đúng sáu thanh kiếm dựng thẳng trong thuyền — ba thanh bên trái các hành khách, ba thanh bên phải, 3 + 3 = 6; cách đều, cả sáu chuôi kiếm đều cao hơn mạn thuyền, không thanh nào cắt ngang các nhân vật. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 57. SEVEN OF SWORDS — Bảy Kiếm

File: [swords-07.txt](swords-07.txt) · Nguồn: `prompts/out6/swords-07.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SEVEN OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân nhanh nhẹn, lén mang năm thanh kiếm trong tay, ngoái nhìn về doanh trại nơi hai thanh kiếm vẫn còn dựng thẳng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ sẫm rối nhẹ, toát vẻ tinh nghịch; Vóc dáng: vóc dáng kẻ tinh ranh mảnh mai, nhanh nhẹn, bước chân nhẹ, đang rón rén rời đi; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 7 thanh kiếm): năm thanh kiếm được mang trong hai tay nhân vật, giữ thẳng đứng và xòe tách ra để có BỐN KHOẢNG TRỜI TRỐNG giữa năm chuôi kiếm — năm chuôi kiếm, bốn khoảng trống — cộng HAI thanh kiếm cắm thẳng trên cỏ phía sau nhân vật, giữa chúng có MỘT KHOẢNG CỎ TRỐNG RỘNG — hai thanh kiếm, một khoảng trống; 5 + 2 = 7. LÁ NÀY ĐÃ TỪNG SAI MỘT LẦN DO HIỆN CHÍN THANH KIẾM: lỗi thường gặp là vẽ BỐN thanh kiếm cắm trên cỏ thay vì hai. Cắm đúng HAI thanh trên cỏ, tuyệt đối không phải bốn, và đếm: 1, 2. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 58. EIGHT OF SWORDS — Tám Kiếm

File: [swords-08.txt](swords-08.txt) · Nguồn: `prompts/out6/swords-08.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "EIGHT OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ khỏa thân bịt mắt, bị trói lỏng, đứng trong vòng tám thanh kiếm; phía sau là một pháo đài trên vách đá.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu sẫm được buộc lỏng bằng dải ruy băng đỏ thẫm; Vóc dáng: dáng người mảnh mai, thanh tú và dễ tổn thương, được bao quanh bởi những lưỡi kiếm dựng thẳng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 8 thanh kiếm): tám thanh kiếm cắm thành một vòng tròn mở quanh nàng — BA thanh phía trước với hai khoảng trống giữa chúng, MỘT thanh bên trái, MỘT thanh bên phải, BA thanh phía sau với hai khoảng trống giữa chúng; 3 + 1 + 1 + 3 = 8. Đi quanh vòng và đếm tám khoảng đất trống giữa các thanh liền kề: 1, 2, 3, 4, 5, 6, 7, 8. LÁ NÀY ĐÃ TỪNG SAI MỘT LẦN DO HIỆN CHÍN THANH KIẾM: lỗi thường gặp là thêm một thanh vào nhóm phía sau nàng. Giữ nhóm phía sau ở đúng BA thanh. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 59. NINE OF SWORDS — Chín Kiếm

File: [swords-09.txt](swords-09.txt) · Nguồn: `prompts/out6/swords-09.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "NINE OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ khỏa thân đau khổ ngồi bật dậy trên giường vào ban đêm, để lộ vai và lưng trần, úp mặt trong hai bàn tay; chín thanh kiếm gắn thành các hàng trên bức tường tối.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen dài buông thành những gợn sóng buồn bã phủ lên hai bàn tay đang ôm mặt khóc; Vóc dáng: dáng người mảnh mai, thanh tú trong áo ngủ, đang ngồi và trút bỏ cảm xúc; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 9 thanh kiếm): đúng chín thanh kiếm gắn trên bức tường tối thành ba hàng, mỗi hàng ba thanh — 3 + 3 + 3 = 9; một ô lưới gọn gàng 3 x 3 gồm các lưỡi kiếm nằm ngang, cả chín đều đếm được, không thanh nào bị đầu hay bàn tay nàng che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 60. TEN OF SWORDS — Mười Kiếm

File: [swords-10.txt](swords-10.txt) · Nguồn: `prompts/out6/swords-10.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TEN OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân yên bình nằm trên bờ biển lúc bình minh dưới mười thanh kiếm dựng thẳng; ánh nắng vàng rọi xuyên qua mặt nước tối.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc sẫm màu mượt như lụa trải trên cát ven bờ; Vóc dáng: dáng thiếu nữ trưởng thành thon gọn nằm yên bình, tắm trong ánh vàng buổi sớm từ đường chân trời; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 10 thanh kiếm): đúng mười thanh kiếm cắm dọc theo lưng thành hai hàng so le, mỗi hàng năm thanh — 5 + 5 = 10; cả mười chuôi kiếm đều đếm được theo một dãy từ vai đến hông, cách đều, không chồng lấp. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 61. PAGE OF SWORDS — Hầu Cận Kiếm

File: [swords-page.txt](swords-page.txt) · Nguồn: `prompts/out6/swords-page.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "PAGE OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hầu cận trẻ khỏa thân, cảnh giác đứng trên gò đất lộng gió, dùng cả hai tay cầm một thanh kiếm giơ cao.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 18 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu mật ong bị gió thổi tung, cắt kiểu pixie tỉa lông vũ sắc nét; Vóc dáng: mềm dẻo, sắc sảo và cảnh giác, tư thế trên đồi đá mang sức bật thể thao; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm, được nắm bằng cả hai tay; không có dao găm, không có lưỡi kiếm thứ hai. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 62. KNIGHT OF SWORDS — Kỵ Sĩ Kiếm

File: [swords-knight.txt](swords-knight.txt) · Nguồn: `prompts/out6/swords-knight.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KNIGHT OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ kỵ sĩ 21 tuổi khỏa thân dữ dội, xông lên trên ngựa phi nước đại, giơ kiếm cao giữa gió bão.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc sẫm màu tung mạnh ra sau từ bên dưới chiếc mũ giáp hở gắn cánh; Vóc dáng: nữ kỵ sĩ dữ dội, thể thao, đang lao tới đầy khí phách; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm, chĩa về phía trước như một cây thương; không có lưỡi kiếm nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 63. QUEEN OF SWORDS — Hoàng Hậu Kiếm

File: [swords-queen.txt](swords-queen.txt) · Nguồn: `prompts/out6/swords-queen.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "QUEEN OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng trưởng thành khỏa thân, nghiêm nghị và tôn quý, tạo dáng duyên dáng gợi cảm nhưng vẫn đầy uy nghi khi ngự trên ngai, ngồi trên ngai đá chạm bướm phía trên biển mây, một tay cầm thanh kiếm dựng thẳng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đỏ nâu gỗ gụ đậm được tết đan cầu kỳ thành vòng miện; Vóc dáng: cao đẹp như tượng, đường nét nhìn nghiêng sắc sảo, xương quai xanh thanh nhã và nghiêm nghị, vẻ đẹp trí tuệ nghiêm trang; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm dựng thẳng; không có lưỡi kiếm nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 64. KING OF SWORDS — Vua Kiếm

File: [swords-king.txt](swords-king.txt) · Nguồn: `prompts/out6/swords-king.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KING OF SWORDS" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ thẩm phán tối cao 25 tuổi khỏa thân, nghiêm nghị và uy nghi, ngồi trên ngai đá cao, cầm thanh kiếm chân lý dựng thẳng; phía sau là bầu trời xanh trong.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 25 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc đen như cánh quạ được cắt gọn, đội vòng miện vàng sắc cạnh; Vóc dáng: nữ quân vương chấp pháp cao lớn, uy nghi, ánh mắt sắc sảo, cầm lưỡi kiếm dựng thẳng; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 thanh kiếm): đúng một thanh kiếm dựng thẳng; không có lưỡi kiếm nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

---

<a id="nhom-pentacles"></a>

## Tiền — 14 lá

### 65. ACE OF PENTACLES — Át Tiền

File: [pentacles-ace.txt](pentacles-ace.txt) · Nguồn: `prompts/out6/pentacles-ace.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "ACE OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một bàn tay thần thánh trao một đồng tiền vàng lớn khắc ngôi sao năm cánh phía trên cổng khu vườn xanh tốt có hoa loa kèn; phía xa là núi.

KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 đồng tiền khắc ngôi sao năm cánh): đúng một đồng tiền vàng lớn khắc ngôi sao năm cánh trong bàn tay thần thánh; không có đồng tiền nào khác, không có tiền rải rác trong vườn. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 66. TWO OF PENTACLES — Hai Tiền

File: [pentacles-02.txt](pentacles-02.txt) · Nguồn: `prompts/out6/pentacles-02.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TWO OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ 19 tuổi khỏa thân vui tươi nhảy múa trên sân hiên ven biển, tung hứng hai đồng tiền vàng khắc ngôi sao năm cánh nằm trong dải ruy băng hình vô cực; phía sau là thuyền giữa những đợt sóng cuộn.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 19 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng cát uốn lọn rối nhẹ, nảy theo điệu nhảy; Vóc dáng: vũ công trẻ nhanh nhẹn, mềm dẻo và linh hoạt, giữ thăng bằng hai đồng tiền trong dải ruy băng hình vô cực; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 2 đồng tiền khắc ngôi sao năm cánh): đúng hai đồng tiền, mỗi đầu của dải ruy băng uốn vòng vô cực có một đồng, mỗi tay cầm một đồng; cả hai mặt đĩa đều nhìn thấy trọn vẹn trên nền trời, không có đồng tiền thứ ba. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 67. THREE OF PENTACLES — Ba Tiền

File: [pentacles-03.txt](pentacles-03.txt) · Nguồn: `prompts/out6/pentacles-03.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "THREE OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ điêu khắc trẻ khỏa thân, tóc buông xõa, đang đục một cây cột trong xưởng; một tu sĩ và một kiến trúc sư đang nhận xét; ba đồng tiền được gắn vào vòm phía trên.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu đỏ sẫm tết cuộn thành vòng miện gọn gàng, tiện cho công việc; Vóc dáng: tập trung, đôi vai nghệ nhân săn chắc, đôi tay rõ khối đang chế tác cho nhà thờ lớn; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 3 đồng tiền khắc ngôi sao năm cánh): đúng ba đồng tiền gắn vào vòm đá phía trên người điêu khắc — một đồng ở đỉnh vòm và hai đồng tại hai chân vòm, 1 + 2 = 3; cả ba mặt đĩa đều nhìn thấy trọn vẹn, không đồng nào bị bóng vòm che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 68. FOUR OF PENTACLES — Bốn Tiền

File: [pentacles-04.txt](pentacles-04.txt) · Nguồn: `prompts/out6/pentacles-04.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FOUR OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân giàu có ngồi trên ghế đá, ôm chặt một đồng tiền vàng khắc ngôi sao năm cánh trước ngực, một đồng trên vương miện và hai đồng dưới chân.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu sẫm được chải gọn, đi cùng dáng ôm vàng sát người; Vóc dáng: tư thế ngồi vững chãi, ổn định, canh giữ của cải; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 4 đồng tiền khắc ngôi sao năm cánh): đúng bốn đồng tiền: một đồng ôm sát ngực nhân vật, một đồng giữ thăng bằng trong vương miện, hai đồng đè dưới hai bàn chân — 1 + 1 + 2 = 4; cả bốn mặt đĩa đều nhìn thấy trọn vẹn, không đồng nào bị vùi trong đất hay bị áo choàng của nhân vật che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 69. FIVE OF PENTACLES — Năm Tiền

File: [pentacles-05.txt](pentacles-05.txt) · Nguồn: `prompts/out6/pentacles-05.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "FIVE OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: hai nữ hành khất trưởng thành khỏa thân đi ngang một nhà thờ tỏa sáng giữa tuyết; năm đồng tiền phát sáng trong ô cửa sổ kính màu cao.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 20 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài nâu sẫm bị gió thổi tung, đón những bông tuyết đang rơi; Vóc dáng: dáng người mảnh mai, run rẩy nhưng bền bỉ dưới cửa sổ nhà thờ; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 5 đồng tiền khắc ngôi sao năm cánh): đúng năm đồng tiền phát sáng gắn trong cửa sổ kính màu cao theo bố cục năm điểm — một đồng ở chính giữa phía trên, hai đồng ở hàng giữa, hai đồng ở hàng dưới, 1 + 2 + 2 = 5; cả năm mặt đĩa đều tách biệt và đếm được. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 70. SIX OF PENTACLES — Sáu Tiền

File: [pentacles-06.txt](pentacles-06.txt) · Nguồn: `prompts/out6/pentacles-06.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SIX OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân sung túc, một tay cầm cân, phân phát tiền vàng cho hai thiếu nữ trưởng thành khỏa thân đang quỳ.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu vàng được chải chuốt theo phong cách thương nhân; Vóc dáng: sung túc, tư thế đứng thẳng trang nghiêm khi phân phát tiền; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 6 đồng tiền khắc ngôi sao năm cánh): đúng sáu đồng tiền trên cân — ba đồng xếp chồng trong đĩa cân trái và ba đồng xếp chồng trong đĩa cân phải, 3 + 3 = 6; cả sáu mặt đĩa đều nhìn thấy phía trên mép đĩa cân, không có đồng tiền rời trên mặt đất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 71. SEVEN OF PENTACLES — Bảy Tiền

File: [pentacles-07.txt](pentacles-07.txt) · Nguồn: `prompts/out6/pentacles-07.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "SEVEN OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ trẻ khỏa thân kiên nhẫn tựa vào cây gậy làm vườn, trầm ngắm bảy đồng tiền vàng khắc ngôi sao năm cánh nở trên dây leo xanh tốt.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ ấm vương mồ hôi, tựa trên cán cuốc; Vóc dáng: thon gọn, cơ bắp săn chắc nhờ lao động đồng áng, tư thế kiên nhẫn và trầm tư; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 7 đồng tiền khắc ngôi sao năm cánh): đúng bảy đồng tiền mọc trên dây leo — ba đồng ở nhánh trái, ba đồng ở nhánh phải, một đồng ở chính giữa phía trên, 3 + 3 + 1 = 7; cả bảy đều nhìn thấy trọn vẹn và không bị lá che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 72. EIGHT OF PENTACLES — Tám Tiền

File: [pentacles-08.txt](pentacles-08.txt) · Nguồn: `prompts/out6/pentacles-08.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "EIGHT OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ học việc trẻ khỏa thân, tóc nâu hạt dẻ ghim thành búi thấp gọn gàng, đang đục một đĩa đá trơn tại bàn làm việc; tám đồng tiền xếp thành một hàng dọc mép bàn; nhìn qua cửa sổ thấy thị trấn.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 21 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu hạt dẻ búi thấp gọn gàng, toát vẻ tập trung; Vóc dáng: mảnh mai và tỉ mỉ, đôi tay vững vàng khắc tiền tại bàn làm việc; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 8 đồng tiền khắc ngôi sao năm cánh): đúng tám đồng tiền đã hoàn thiện trong MỘT hàng thẳng gồm 8 đồng dọc mép trước của bàn, cách đều và cả tám đều đếm được; đĩa đá trống nàng đang đục còn dang dở và không có ngôi sao, nên KHÔNG được tính và không được trông giống đồng tiền. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 73. NINE OF PENTACLES — Chín Tiền

File: [pentacles-09.txt](pentacles-09.txt) · Nguồn: `prompts/out6/pentacles-09.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "NINE OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một phụ nữ khỏa thân thanh lịch có chim ưng đậu trên bàn tay trần, tay kia chạm vào chùm nho chín; chín đồng tiền nằm dọc xà giàn cây, một con ốc sên dưới chân nàng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc dài nâu cà phê đậm như dây nho sẫm màu, uốn lọn lỏng đan chỉ vàng; Vóc dáng: dáng đồng hồ cát quý tộc duyên dáng, tinh tế giữa vườn nho đang nở hoa; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 9 đồng tiền khắc ngôi sao năm cánh): đúng chín đồng tiền gắn trên xà giàn cây trong MỘT hàng gồm 9 đồng, cách đều trên nền trời thoáng, cả chín đều nhìn thấy trọn vẹn, không đồng nào bị lá hoặc cơ thể nàng che — đếm từ trái sang phải: 1 đến 9. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 74. TEN OF PENTACLES — Mười Tiền

File: [pentacles-10.txt](pentacles-10.txt) · Nguồn: `prompts/out6/pentacles-10.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "TEN OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một đại sảnh gia đình — một nữ chủ gia đình trưởng thành khỏa thân đang ngồi, hai phụ nữ trưởng thành khỏa thân đứng với một bàn tay đặt ở eo người kia, một đứa trẻ chơi cùng hai con chó — mười đồng tiền tạo thành huy hiệu hình kim tự tháp trên tường phía sau họ.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 22 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc nâu mật ong ấm được tết thành vòng miện dày; Vóc dáng: vẻ đẹp nữ chủ gia đình mãn nguyện, dịu dàng, được bao quanh bởi của cải gia tộc; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 10 đồng tiền khắc ngôi sao năm cánh): đúng mười đồng tiền trên tường theo hình kim tự tháp Cây Sự Sống — 4 đồng ở hàng dưới cùng, 3 đồng ở hàng trên, 2 đồng ở hàng tiếp theo, 1 đồng ở đỉnh, 4 + 3 + 2 + 1 = 10; cả mười mặt đĩa đều đếm được, không đồng nào bị các nhân vật che khuất. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 75. PAGE OF PENTACLES — Hầu Cận Tiền

File: [pentacles-page.txt](pentacles-page.txt) · Nguồn: `prompts/out6/pentacles-page.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "PAGE OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hầu cận trẻ khỏa thân ham học đang chăm chú nghiên cứu một đồng tiền lớn khắc ngôi sao năm cánh cầm bằng cả hai tay; phía sau là cánh đồng đã cày.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 18 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc vàng óng buông xõa quá vai, bắt ánh nắng đồng cỏ; Vóc dáng: vóc dáng học giả trẻ nhỏ nhắn, nghiêm túc, nâng đồng tiền cao với vẻ tôn kính; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 đồng tiền khắc ngôi sao năm cánh): đúng một đồng tiền lớn, được cầm bằng cả hai tay; không có đồng tiền nào khác ở bất kỳ đâu. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 76. KNIGHT OF PENTACLES — Kỵ Sĩ Tiền

File: [pentacles-knight.txt](pentacles-knight.txt) · Nguồn: `prompts/out6/pentacles-knight.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KNIGHT OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ kỵ sĩ 23 tuổi khỏa thân kiên định, cầm đồng tiền vàng khắc ngôi sao năm cánh với vẻ tôn kính điềm tĩnh trên cánh đồng đã cày.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 23 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc màu đồng sẫm tết dưới chiếc mũ giáp gắn mào lá sồi; Vóc dáng: nữ kỵ sĩ vững chắc, thể thao trên chiến mã to khỏe điềm tĩnh; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 đồng tiền khắc ngôi sao năm cánh): đúng một đồng tiền, nằm trong lòng bàn tay mở của nhân vật; không có đồng tiền nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 77. QUEEN OF PENTACLES — Hoàng Hậu Tiền

File: [pentacles-queen.txt](pentacles-queen.txt) · Nguồn: `prompts/out6/pentacles-queen.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "QUEEN OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng khỏa thân ấm áp đội vòng hoa, ngồi trên ngai chạm dê, để lộ một bên ngực, một đồng tiền khắc ngôi sao năm cánh đặt trong lòng; trong vườn có một con thỏ.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 24 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc màu sô-cô-la đậm ánh vàng đỏ, đội vòng dây leo đang nở hoa; Vóc dáng: đầy đặn, mang nét mẫu tính, đường cong nữ tính phóng khoáng và ấm áp trên ngai chạm thú; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 đồng tiền khắc ngôi sao năm cánh): đúng một đồng tiền, đặt trong lòng nàng; không có đồng tiền nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```

### 78. KING OF PENTACLES — Vua Tiền

File: [pentacles-king.txt](pentacles-king.txt) · Nguồn: `prompts/out6/pentacles-king.txt`

```text
CHUẨN THAM CHIẾU: dùng cards/17-the-star.png làm mẫu tham chiếu thị giác cho bố cục 784×1360 đã đo, tỷ lệ khoảng mở của khung, ánh sáng, sắc thái màu, chiều sâu và cách thể hiện nét vàng cổ mảnh. Thay cảnh trong ảnh tham chiếu bằng cảnh của lá bài này.

Tạo tranh cho "KING OF PENTACLES" theo mô tả cảnh gốc. Đây chỉ là phần tranh minh họa, không phải một lá bài Tarot thành phẩm. Cảnh phải phủ kín toàn bộ bề mặt tranh từ mép này đến mép kia, không chừa khoảng riêng ở đầu hoặc cuối.

CẢNH: một nữ hoàng tài lộc 25 tuổi khỏa thân giàu có ngồi trên ngai chạm bò đực giữa dây nho đang nở hoa và tường lâu đài, cầm một đồng tiền vàng khắc ngôi sao năm cánh trong lòng.

THÔNG SỐ NHÂN VẬT (nguồn: cards.json): Tuổi: 25 (bắt buộc là người trưởng thành trẻ tuổi, từ 18 đến 25 tuổi); Tóc: tóc sẫm màu gợn sóng, đan cùng lá nguyệt quế vàng và nho chín; Vóc dáng: quân vương tráng kiện, giàu có, ngồi thoải mái trong khu vườn lâu đài xanh tốt; Vẻ gợi cảm: thể hiện nét gợi cảm mỹ thuật rõ nét nhưng tinh tế — tự tin, đĩnh đạc, hình thể cổ điển mềm mại, làn da mang chất hội họa trong ánh sáng vàng ấm. KHÓA SỐ LƯỢNG (CHÍNH XÁC 1 đồng tiền khắc ngôi sao năm cánh): đúng một đồng tiền, được cầm trong một tay; không có đồng tiền nào khác. KHÓA GIẢI PHẪU (QUY TẮC BẮT BUỘC): mỗi nhân vật có đúng hai tay, hai chân, một đầu và một thân; mọi khớp (vai, khuỷu tay, cổ tay, hông, đầu gối, cổ chân) phải nối tự nhiên với cơ thể — KHÔNG thừa chi, KHÔNG có chi mọc dính vào sườn, hông, ngực hoặc lưng, KHÔNG thiếu hay cụt tay, KHÔNG biến dạng khớp, KHÔNG sai số lượng ngón tay; giữ hai cánh tay tách rõ khỏi thân, nhìn rõ nách, khuỷu tay và cổ tay.

KHÓA ĐẦU RA: bề mặt tranh dọc có kích thước chính xác 784 × 1360 pixel, bố cục 7:12. Chỉ xuất phần tranh vẽ thuần túy phủ kín từ mép này đến mép kia. Không lề ngoài, không đường viền, không khung, không nét vàng, không hoa văn góc, không ô nền bên trong, không đĩa huy chương, không huy hiệu, không biểu tượng đồ họa, không biểu tượng huy hiệu gia tộc, không ký hiệu chất bài, không ruy băng, không bảng tên, không tiêu đề, không chữ cái, không chữ số, không dấu chìm và không chữ trang trí ở bất kỳ đâu. Không vẽ tên lá bài hoặc bất kỳ văn bản nào vào ảnh.

ĐẦU RA THEO THAM CHIẾU THE STAR: tái hiện bầu không khí thanh lịch và khung đã đo của lá tham chiếu mà không sao chép các vật thể của nó. Giữ cảnh rõ ràng, chân thực và không phô bày chi tiết nhạy cảm; sử dụng đường nét cơ thể, tư thế, ánh sáng và môi trường tự nhiên. Giữ nguyên các khóa số lượng gốc của lá bài và chỉ dùng những vật thể có trong cảnh gốc. Xuất PNG dọc với kích thước chính xác 784 × 1360.
```
