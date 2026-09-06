# 🔮 THE STAR LOOK — Chuẩn phong cách vẽ & tỉ lệ đồng nhất cho 78 lá

> Bộ chuẩn "look" này **không thay đổi bất kỳ ảnh nào trong `cards/`**. Nó định nghĩa
> phong cách vẽ (drawing style), tỉ lệ và bảng màu duy nhất để cả 78 lá bài — hiện có
> lẫn khi tạo lại — đều ra cùng một "look", neo theo lá chuẩn **`cards/17-the-star.png`**.

---

## 1. Mỏ neo (Anchor) & mục tiêu

| | |
|---|---|
| **Lá chuẩn duy nhất** | `cards/17-the-star.png` (The Star) |
| **Mục tiêu** | 78 lá có cùng **nét vẽ**, cùng **ánh sáng**, cùng **khung viền**, cùng **tỉ lệ**; mỗi lá chỉ khác nội dung riêng (nhân vật, bối cảnh, huy hiệu, tên) |
| **Phạm vi** | 22 Ẩn Chính + 56 Ẩn Phụ = **78 lá** |

---

## 2. Tỉ lệ & kích thước chuẩn (đồng nhất tuyệt đối)

- **Kích thước:** `784 × 1360` px, PNG, RGB.
- **Tỉ lệ khung hình:** `7 : 12` (chiều rộng / chiều cao ≈ `0.576`).
- **Quy tắc:** mọi lá phải xuất đúng `784 × 1360`. Ảnh nguồn khác tỉ lệ phải được
  resize-crop về đúng tỉ lệ **trước** khi ghép khung (không ép méo hình).

---

## 3. Cấu trúc 4 lớp chiều sâu (4-Layer Depth)

| Lớp | Tên | Yêu cầu |
|---|---|---|
| **1** | Nền | Giấy da cổ (aged parchment/vellum) tông vàng nâu ấm, nhuốm màu thời gian |
| **2** | Nội dung | Phối cảnh thoáng đãng, ánh sáng ấm, chiều sâu lùi dần về hậu cảnh. **Phóng to, tràn nhẹ xuống dưới mép trong của khung vàng** |
| **3** | Khung viền | Viền mạ vàng Gothic **mỏng, sắc nét, đối xứng tuyệt đối**, hoa văn góc; **đè lên mép nội dung** (foreground ornament over background) |
| **4** | Huy hiệu & Tên | Oval medallion ở đỉnh chứa huy hiệu mạ vàng + dải ruy băng cuộn ở đáy chứa tên lá |

> ⚠️ Không dùng cổng vòm/cột đá phụ đóng khung nội dung — để không gian mở khoáng đạt
> như The Star.

---

## 4. Phong cách vẽ (Drawing Style — chuẩn The Star)

1. **Hội họa fine-art** kiểu tranh sơn dầu: nét cọ hữu cơ (painterly brushwork), hình khối
   chuyển mềm (softly blended forms), tiêu điểm chi tiết sắc nét.
2. **Ánh sáng ấm định hướng** + bóng mát lạnh nhẹ; phối cảnh khí quyển
   (atmospheric perspective) với chiều sâu không gian lùi dần về hậu cảnh.
3. **Da nhân vật** kết xuất kiểu painterly, tông vàng ấm, giải phẫu cổ điển mềm mại,
   gợi cảm có chừng mực (tasteful fine-art sensuality).
4. **Khung viền** mạ vàng Gothic thanh mảnh, nét line-art sắc, đối xứng; họa tiết filigree
   + hoa văn góc; **medallion oval** (huy hiệu) trên đỉnh + **ribbon** (tên lá) dưới đáy.
5. **Bố cục** chính giữa tuyệt đối, hướng dọc (portrait), mức chi tiết cao.

---

## 5. Bảng màu neo (đo từ `17-the-star.png`)

| Vai trò | Mã màu | Ghi chú |
|---|---|---|
| Kem giấy da / highlight | `#ecd5a9` | tone sáng nhất của nền |
| Vàng cổ — filigree | `#d6b988` | màu chủ đạo họa tiết |
| Viền vàng (line) | `#e0c595` | nét viền khung |
| Đồng (bronze) | `#c5a674` | khối vàng trung gian |
| Đồng sẫm | `#9f7e59` | bóng của họa tiết |
| Nâu đất (umber) | `#674b2e` | bóng sâu |
| Xanh đêm (nội dung) | `#343944` | bầu trời/bóng cảnh đêm |
| Gần đen | `#1a1c25` | vùng tối sâu |
| Xanh thép nhạt | `#76888f` | nước/đá (chất liệu lạnh) |

- Nhiệt màu toàn lá: **ấm** (độ lệch R−B ≈ `+27`).
- Quy tắc: vùng khung & huy hiệu luôn nghiêng về **vàng cổ ấm**; vùng nội dung được
  phép lệch theo bối cảnh từng lá (đêm/ngày/đồng/bể…) nhưng phải giữ **nhiệt màu ấm
  và độ sáng tương đương The Star**.

> Xem ảnh mẫu màu: `look/palette.png`.

---

## 6. Nhân vật (Character)

- **100% nhân vật nữ**, độ tuổi **18–25** (theo `tarot prompt/01-CARD-TABLE.md`).
- Mỗi lá giữ nhận diện độc bản về tuổi, tóc, vóc dáng, thần thái (đã có trong bảng chuẩn).
- **Giải phẫu (HARD RULE):** tối đa **2 tay, 2 chân, 1 đầu, 1 thân**; mọi khớp nối tự
  nhiên; không thừa/thiếu chi, không chi dính thân, không khớp biến dạng, không sai số ngón.
- Ưu tiên tư thế **2 tay tách rõ khỏi thân** (có nách, khuỷu, cổ tay rõ) để giảm lỗi.

---

## 7. Khoá số lượng (Count Lock)

- Số vật thể (gậy/cốc/kiếm/tiền) **trong nội dung** và **trên huy hiệu** phải đúng con số
  của lá (xem `tarot prompt/cards.json` → trường `count`).
- Không tin AI tự đếm — kiểm chứng bằng code / đếm thủ công trước khi chốt ảnh.

---

## 8. Khối STYLE LOCK dùng chung (nhúng vào mọi prompt)

Đoạn tiếng Anh dưới đây được nhúng nguyên văn vào cả 78 prompt trong `look/prompts/`
để mọi lá ra cùng một phong cách:

```text
STYLE LOCK (unified deck look, anchored to THE STAR): fine-art oil-painting
illustration with painterly brushwork and softly blended forms; warm directional
light against soft cool shadows; rich atmospheric perspective with deep spatial
recession; aged parchment/vellum base with a thin, razor-sharp, perfectly
symmetrical golden gothic line-art border of antique gold filigree with corner
flourishes; palette anchored to The Star (cream #ecd5a9, antique gold #d6b988,
gold line #e0c595, bronze #c5a674 to #9f7e59 to umber #674b2e, deep slate
#343944 to near-black #1a1c25, muted steel blue #76888f); sensual fine-art
anatomy, tasteful classical rendering, painterly skin in warm golden light;
perfectly centered, portrait orientation 7:12 aspect ratio (784x1360), high detail.
```

---

## 9. Kiểm tra chấp nhận (Acceptance Checklist)

Trước khi một lá được coi là "đạt look":

- [ ] Kích thước đúng `784 × 1360` (tỉ lệ 7:12).
- [ ] Khung viền khớp chuẩn The Star — RMSE dải viền trái 60px **≤ 0.04**.
- [ ] Huy hiệu medallion trên + tên lá trong ribbon dưới khớp bảng chuẩn.
- [ ] Số lượng vật thể đúng (Count Lock).
- [ ] Giải phẫu đúng (Anatomy Lock).
- [ ] Nhiệt màu ấm, độ sáng ~ The Star (tránh quá tối/quá sáng/quá bão hòa).

---

## 10. Bộ kit đi kèm

| File | Ý nghĩa |
|---|---|
| `look/00-STYLE-GUIDE.md` | File này — chuẩn look tổng |
| `look/template.md` | Master prompt template (điền `{TITLE}` `{EMBLEM}` `{SCENE}` `{CHARACTER}` `{COUNT_LOCK}`) |
| `look/prompts/*.txt` | **78 prompt** chuẩn hóa (mỗi lá một file, đã nhúng STYLE LOCK) |
| `look/frame-template.png` | Khung chuẩn (bản sao `cards/card-blank.png`) để ghép nội dung |
| `look/palette.png` | Ảnh mẫu bảng màu neo |
| `look/build_prompts.py` | Script tái sinh 78 prompt từ `tarot prompt/cards.json` |

**Tái sinh prompt:** `python3 look/build_prompts.py`
