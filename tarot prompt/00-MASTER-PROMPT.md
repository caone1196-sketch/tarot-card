# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot:

1. **Quy chuẩn hiển thị nội dung (Visual Anchor Standard — THE STAR)**:
   * Lấy lá **`cards/17-the-star.png`** làm quy chuẩn hiển thị nội dung cho toàn bộ bộ bài.
   * Vùng hiển thị nội dung mở rộng tối đa, phủ kín toàn bộ vòm trung tâm từ mép này sang mép kia của khung viền Gothic mỏng.
   * **Loại bỏ cổng vòm / cột đá phụ chiếm diện tích**: Không dùng cột đá nhân tạo đóng khung gò bó, để không gian khoáng đạt, tự nhiên theo đúng bối cảnh của từng lá bài.

2. **Quy chuẩn tạo hình nhân vật (Sensual Fine-Art Figure Standard)**:
   * Kế thừa phong cách tạo hình sống động, gợi cảm và cổ điển từ tài liệu gốc `01-CARD-TABLE.md` (hình mẫu tiêu biểu như lá **The Empress**: *"a voluptuous nude empress, one breast bared, a crown of flowers in loosened hair, reclining on a velvet throne amid ripe golden wheat and fruits, a heart-shaped shield of Venus leaning beside her"*).
   * **100% Nhân vật nữ** trong độ tuổi thanh xuân từ **18 đến 25 tuổi**.
   * Mỗi lá bài giữ nét đặc trưng độc bản về vóc dáng (*slender, voluptuous, athletic, statuesque*), mái tóc và thần thái.

3. **Cấu trúc 4 Lớp Chiều Sâu (4-Layer Depth)**:
   * **Lớp 1 (Nền)**: Giấy da cổ (*Aged parchment/vellum*) nhuốm màu thời gian sepia ấm áp.
   * **Lớp 2 (Nội dung)**: Phối cảnh tự nhiên, thoáng đãng với ánh sáng ấm áp và chiều sâu không gian lùi dần về hậu cảnh.
   * **Lớp 3 (Khung viền)**: Khung viền mạ vàng Gothic mỏng, sắc nét, đối xứng hoàn hảo.
   * **Lớp 4 (Huy hiệu & Tên)**: Oval Medallion ở đỉnh chứa huy hiệu mạ vàng + Dải ruy băng cuộn ở đáy chứa tên lá bài.

---

## Master Prompt Template (Chuẩn The Star)

```text
A single tarot card "{TITLE}" built inside the reference frame, matching the EXACT open window display, scale, and lighting style of THE STAR: keep the intricate thin golden line-art border in vintage gothic style and aged parchment background texture.

At the TOP: inside the oval medallion plate, {EMBLEM} in glowing antique gold.
At the BOTTOM: inside the ribbon banner, the title "{TITLE}" in clean antique gold lettering.

In the large open center panel (filling the entire inner window edge to edge, matching the open space of The Star without heavy inner arch barriers):
{SCENE}. {CHARACTER_SPECIFICATION} {COUNT_LOCK}

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, symmetrical golden frame border, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail.
```
