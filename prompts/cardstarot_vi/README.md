# 78 prompt tiếng Việt — dải lụa eo/hông

Quy chuẩn **waist-ribbon-v1**, xác nhận ngày **06/09/2026**. Đây là bộ **render riêng**, không thay thế `cards.json`, `prompts/out6_vi` hoặc các ảnh gốc.

## Phạm vi

- **69 lá người trưởng thành:** dải lụa ngà chỉ quấn eo/hông, có lớp lót màu da kín; phần trước thân trên không phô bày nhờ góc nhìn/tóc/tư thế tự nhiên.
- **3 lá có trẻ em:** `cups-10`, `swords-06`, `pentacles-10`. Tất cả người lớn và trẻ em mặc kín, bối cảnh trung tính; không kế thừa mô tả trang phục mỏng. Không dùng ảnh tham chiếu người quấn lụa cho nhóm này.
- **6 lá không có nhân vật toàn thân:** Ace of Wands, Eight of Wands, Ace of Cups, Ace of Swords, Three of Swords, Ace of Pentacles. Không thêm người hoặc dải vải; giữ bàn tay/đạo cụ/biểu tượng theo cảnh.
- Đủ **22 lá Ẩn Chính + 56 lá Ẩn Phụ**. Chuẩn bị 78 prompt không đồng nghĩa đã tạo 78 ảnh; ảnh được thực hiện từng đợt **3 lá**, không có tác vụ tạo ảnh tự chạy ngầm.

## Bảo toàn nội dung

- Slug, tiêu đề, nhóm, tuổi và trường dữ liệu thẻ lấy từ `tarot prompt/cards.json`; cảnh, tóc, vóc dáng và khóa số lượng dùng bản dịch tĩnh `prompts/out6_vi` tương ứng.
- Các câu buộc phô bày cơ thể trong mô tả cũ được trung tính hóa ở **file render này**, để không mâu thuẫn trang phục/góc nhìn mới. Không ghi ngược thay đổi về nguồn.
- **62 khóa số lượng được giữ nguyên văn**, không tự tạo khóa cho 16 lá thiếu trường `count`. Giữ các hành động và đồ vật riêng, không ép mọi người đứng giống The Fool.
- Trên các lá có trẻ em, bỏ mô tả hình thể/gợi cảm của người lớn; chỉ giữ thông tin cần thiết và dùng trang phục gia đình kín đáo. Không thay tuổi trẻ em bằng tuổi nhân vật chính.
- “95%” ở nhóm người trưởng thành là **quy ước thị giác**, không phải phép đo độ xuyên sáng; lớp lót và các vùng cần che vẫn kín.
- Kích thước đích: **PNG 784 × 1360**, tranh phủ kín ảnh. Không khung hoặc tên lá; những biểu tượng thuộc cảnh gốc vẫn giữ, không bổ sung huy hiệu trang trí.
- Bản dịch là dữ liệu tĩnh. Nếu `cards.json` thay đổi, cần rà soát bản dịch tương ứng trước khi dựng lại bộ render; không có đồng bộ/biên dịch dịch thuật tự động.

## Tạo lại và kiểm tra

```bash
python3 scripts/build_cardstarot_prompts_vi.py
python3 scripts/build_cardstarot_prompts_vi.py --check
python3 -m unittest discover -s tests -p 'test_cardstarot_prompts_vi.py' -v
```

Script chỉ ghi `prompts/cardstarot_vi/`, không gọi API tạo ảnh, không sửa nguồn hoặc gallery. `--check` chỉ đọc và so sánh. Thông tin trạng thái ảnh thật nằm ở [`cardstarot/README.md`](../../cardstarot/README.md), không suy ra từ sự tồn tại của file prompt.

- [Toàn bộ 78 prompt](TAT-CA-78-PROMPT.md)
- [Quy chuẩn trang phục, góc nhìn và ngoại lệ](STYLE.md)
- [Manifest, hash nguồn và profile từng lá](manifest.json)
- [Ảnh mẫu dải lụa](../../cardstarot/variants/00-fool-waist-ribbon.png) — chỉ dành cho nhóm người trưởng thành

## Danh sách

| STT | Lá / prompt | Nhóm | Profile |
|---|---|---|---|
| 1 | [THE FOOL](00-fool.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 2 | [THE MAGICIAN](01-magician.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 3 | [THE HIGH PRIESTESS](02-priestess.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 4 | [THE EMPRESS](03-empress.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 5 | [THE EMPEROR](04-emperor.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 6 | [THE HIEROPHANT](05-hierophant.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 7 | [THE LOVERS](06-lovers.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 8 | [THE CHARIOT](07-chariot.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 9 | [STRENGTH](08-strength.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 10 | [THE HERMIT](09-hermit.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 11 | [WHEEL OF FORTUNE](10-wheel.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 12 | [JUSTICE](11-justice.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 13 | [THE HANGED](12-hanged.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 14 | [DEATH](13-death.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 15 | [TEMPERANCE](14-temperance.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 16 | [THE DEVIL](15-devil.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 17 | [THE TOWER](16-tower.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 18 | [THE STAR](17-the-star.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 19 | [THE MOON](18-moon.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 20 | [THE SUN](19-sun.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 21 | [JUDGEMENT](20-judgement.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 22 | [THE WORLD](21-world.txt) | major | Người trưởng thành — dải lụa eo/hông |
| 23 | [ACE OF WANDS](wands-ace.txt) | wands | Biểu tượng/bàn tay — không thêm nhân vật |
| 24 | [TWO OF WANDS](wands-02.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 25 | [THREE OF WANDS](wands-03.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 26 | [FOUR OF WANDS](wands-04.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 27 | [FIVE OF WANDS](wands-05.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 28 | [SIX OF WANDS](wands-06.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 29 | [SEVEN OF WANDS](wands-07.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 30 | [EIGHT OF WANDS](wands-08.txt) | wands | Biểu tượng/bàn tay — không thêm nhân vật |
| 31 | [NINE OF WANDS](wands-09.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 32 | [TEN OF WANDS](wands-10.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 33 | [PAGE OF WANDS](wands-page.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 34 | [KNIGHT OF WANDS](wands-knight.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 35 | [QUEEN OF WANDS](wands-queen.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 36 | [KING OF WANDS](wands-king.txt) | wands | Người trưởng thành — dải lụa eo/hông |
| 37 | [ACE OF CUPS](cups-ace.txt) | cups | Biểu tượng/bàn tay — không thêm nhân vật |
| 38 | [TWO OF CUPS](cups-02.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 39 | [THREE OF CUPS](cups-03.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 40 | [FOUR OF CUPS](cups-04.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 41 | [FIVE OF CUPS](cups-05.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 42 | [SIX OF CUPS](cups-06.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 43 | [SEVEN OF CUPS](cups-07.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 44 | [EIGHT OF CUPS](cups-08.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 45 | [NINE OF CUPS](cups-09.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 46 | [TEN OF CUPS](cups-10.txt) | cups | Có trẻ em — mọi nhân vật mặc kín |
| 47 | [PAGE OF CUPS](cups-page.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 48 | [KNIGHT OF CUPS](cups-knight.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 49 | [QUEEN OF CUPS](cups-queen.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 50 | [KING OF CUPS](cups-king.txt) | cups | Người trưởng thành — dải lụa eo/hông |
| 51 | [ACE OF SWORDS](swords-ace.txt) | swords | Biểu tượng/bàn tay — không thêm nhân vật |
| 52 | [TWO OF SWORDS](swords-02.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 53 | [THREE OF SWORDS](swords-03.txt) | swords | Biểu tượng/bàn tay — không thêm nhân vật |
| 54 | [FOUR OF SWORDS](swords-04.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 55 | [FIVE OF SWORDS](swords-05.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 56 | [SIX OF SWORDS](swords-06.txt) | swords | Có trẻ em — mọi nhân vật mặc kín |
| 57 | [SEVEN OF SWORDS](swords-07.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 58 | [EIGHT OF SWORDS](swords-08.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 59 | [NINE OF SWORDS](swords-09.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 60 | [TEN OF SWORDS](swords-10.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 61 | [PAGE OF SWORDS](swords-page.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 62 | [KNIGHT OF SWORDS](swords-knight.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 63 | [QUEEN OF SWORDS](swords-queen.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 64 | [KING OF SWORDS](swords-king.txt) | swords | Người trưởng thành — dải lụa eo/hông |
| 65 | [ACE OF PENTACLES](pentacles-ace.txt) | pentacles | Biểu tượng/bàn tay — không thêm nhân vật |
| 66 | [TWO OF PENTACLES](pentacles-02.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 67 | [THREE OF PENTACLES](pentacles-03.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 68 | [FOUR OF PENTACLES](pentacles-04.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 69 | [FIVE OF PENTACLES](pentacles-05.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 70 | [SIX OF PENTACLES](pentacles-06.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 71 | [SEVEN OF PENTACLES](pentacles-07.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 72 | [EIGHT OF PENTACLES](pentacles-08.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 73 | [NINE OF PENTACLES](pentacles-09.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 74 | [TEN OF PENTACLES](pentacles-10.txt) | pentacles | Có trẻ em — mọi nhân vật mặc kín |
| 75 | [PAGE OF PENTACLES](pentacles-page.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 76 | [KNIGHT OF PENTACLES](pentacles-knight.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 77 | [QUEEN OF PENTACLES](pentacles-queen.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
| 78 | [KING OF PENTACLES](pentacles-king.txt) | pentacles | Người trưởng thành — dải lụa eo/hông |
