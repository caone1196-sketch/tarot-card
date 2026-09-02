# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION (KHUNG BÀI MỚI)

Quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot — **khung 4 lớp, KHÔNG huy hiệu**.

1. **Quy chuẩn khung (Visual Anchor Standard — THE STAR, bản khung mới)**:
   * Lấy lá **`cards/17-the-star.png`** làm quy chuẩn DUY NHẤT cho khung lá bài —
     chuẩn cho cả **khung 4 lớp** lẫn **chất lượng nội dung**.
   * Mẫu nền trống: **`cards/card-blank.png`** (4 lớp, không nội dung, không tên).
   * Kích thước lá: **784 × 1360** (tỷ lệ 7:12), PNG.

2. **Cấu trúc 4 LỚP (từ dưới lên)**:
   * **Lớp 1 — NỀN**: giấy da cổ (*aged parchment/vellum*) nhuốm màu thời gian
     sepia ấm, phủ **kín toàn bộ** lá bài.
   * **Lớp 2 — NỘI DUNG TRÀN VIỀN**: phối cảnh tự nhiên, thoáng đãng, ánh sáng ấm,
     chiều sâu không gian lùi dần về hậu cảnh. Nội dung được **PHÓNG TO TRÀN VIỀN**
     tới sát mép lá và **chui nhẹ xuống dưới mép trong của khung vàng**.
   * **Lớp 3 — KHUNG HỌA TIẾT MẢNH SÁT LỀ (VÀNG KIM NỔI BẬT)**: khung viền
     **vàng kim metallic** Gothic **rất mảnh**, sắc nét, đối xứng hoàn hảo,
     **sát lề lá bài**, hoa văn filigree nhỏ ở 4 góc. Tông vàng đậm có viền tối
     + lõi sáng + quầng vàng ấm mảnh quanh nét → nổi bật trên mọi nền nhưng
     **vẫn giữ nét mảnh** (không làm dày nét). Khung **ĐÈ LÊN TRÊN** mép nội dung
     (foreground ornament over background scene) để tạo chiều sâu phân lớp —
     khung nổi phía trước, cảnh lùi ra sau.
   * **Lớp 4 — TÊN LÁ**: tên lá bài bằng chữ **Blackletter (UnifrakturCook)**
     mạ vàng cổ, **baseline chữ CONG** (hai đầu nhô lên, giữa võng xuống ≈6px),
     đặt **trực tiếp trên nội dung** ở đáy lá — **KHÔNG có khung chữ**
     (không plate, không dải băng, không cartouche, không viền bao quanh chữ).
     Chữ nổi bằng nét vàng kim + bóng đổ mảnh.
     **KHÔNG còn oval medallion / huy hiệu / biểu tượng ở đỉnh** — đã bỏ khung biểu tượng.

3. **Quy chuẩn tạo hình nhân vật (nguồn: `02-CHARACTER-SPECS.md`)**:
   * **100% nhân vật nữ**, độ tuổi **18–25** (bảng 72 nhân vật — 6 lá vật thể thuần).
   * Mỗi lá dùng đúng tổ hợp: **đôi mắt · kiểu tóc · vóc dáng (A–D) · màu da ·
     nét riêng (1 chi tiết) · không khí** theo bảng chuẩn `02-CHARACTER-SPECS.md`
     (tuổi + kiểu tóc giữ nguyên 100% so với `01-CARD-TABLE.md`).
   * **DA — HARD RULE**: chỉ 10 tông sáng → nâu vàng nhạt (porcelain → amber-gold);
     **cấm da đen / da sẫm** kể cả dưới ánh sáng mạnh.
   * **VÓC DÁNG — HARD RULE**: trần là "trung bình" (A → D), **không plus-size,
     không béo, không phóng đại**. Gợi cảm nằm ở đường cong tự nhiên, làn da bóng,
     tư thế và ánh mắt.
   * **ANATOMY LOCK — HARD RULE**: mỗi nhân vật tối đa 2 tay, 2 chân, 1 đầu, 1 thân;
     mọi khớp nối tự nhiên; không thừa chi, không chi dính thân, không tay cụt,
     không ngón sai số. Ưu tiên tư thế 2 tay tách rõ khỏi thân.
   * **NÉT RIÊNG**: mỗi nhân vật đúng **1** chi tiết nhận diện (nốt ruồi, sẹo nhỏ,
     tàn nhang, xăm, khuyên, bớt…), không trùng giữa các lá.
   * **GỢN MỜ GẦN VẬT THỂ (SOFT OBJECT HALO)**: giữ **quầng sáng / halo mờ mềm
     ngay cạnh các vật thể** — gợn nước quanh bình/chén, quầng sáng quanh đèn,
     nến, đồ vàng, bloom nhẹ gần sao/lửa, phản chiếu mờ nơi vật chạm nước.
     Đây là hiệu ứng **cố ý** — không xoá, giữ mượt, có chủ đích, khu trú
     (⚠️ không phải nhiễu / grain / sharp blur).
   * **CÁCH DIỄN ĐẠT ĐÃ THÀNH CÔNG (The Star)**: lời lẽ dưới đây là **nguyên văn
     đã sinh ra các phương án được chấp nhận** — giữ nguyên khi render lại lá
     này (đã đóng vào `STAR_SCENE_LOCK` / `STAR_SKY_RIPPLE_LOCK` trong
     `scripts/build_prompts.py` và `scene` trong `tarot prompt/cards.json`):
     * *classical allegorical oil painting of a water nymph at night, Victorian
       allegorical art, tasteful luminous old-master style; S-CURVE stance —
       hips swayed, torso softly leaning, one leg lightly bent; face tilted
       slightly BACK toward the stars; right arm raised high, stream pouring
       ONTO her neck and gliding down collarbone/torso like liquid glass into
       the lake; left arm relaxed down and BEHIND her back with a second
       golden pitcher tilted slightly, NO water flows from it.*
     * **SKY LOCK**: 1 sao 8 cánh lớn + 7 sao nhỏ, **không trăng**. **RIPPLE
       RULE**: gợn sóng CHỈ ở 2 vùng — nơi thân chạm mặt nước và nơi dòng
       nước chạm mặt nước; không gợn nào khác.
     * **CLOTH RULE (HARD)**: tuyệt đối **không veil / lụa / vải / áo / khăn
       quấn / drapery** trên người — **BARE SKIN ONLY**; dòng nước là nước
       trong chảy trên da trần, **KHÔNG** diễn giải thành váy nước mờ /
       sarong / áo lụa / water-veil / drape.

4. **Thông số chất lượng (QUALITY & SURFACE LOCK — áp dụng mọi lá)**:
   * **Độ bóng (GLOSSY)**: da có độ bóng dầu vẽ ánh sáng, điểm specular "ướt"
     trên vai, xương đòn, hông, môi — **không phẳng matte**.
   * **Chi tiết (DETAIL)**: siêu chi tiết — sợi tóc, thớ lụa, lỗ chân lông,
     trang sức, hoạ tiết nền.
   * **Khử hạt / nhiễu (NOISE)**: ảnh sạch tuyệt đối — **không film grain,
     không sensor noise, không speckle, không dither/jpeg artifacts, không
     viền màu lệch**; gradient mượt như bơ.
   * **Độ sắc nét (SHARPNESS)**: mép sắc như dao cạo, chi tiết vi mô tương phản
     cao, nét tập trung tuyệt đối vào nhân vật và tên lá — **không mờ mềm,
     không blur chuyển động trên nhân vật**.

---

## Master Prompt Template (Chuẩn The Star — Khung 4 lớp, không huy hiệu)

```text
A single tarot card "{TITLE}" in vintage gothic fine-art style, portrait 7:12 aspect ratio, high detail, perfectly centered.

PAINT IT AS 4 LAYERS, background to foreground:
LAYER 1 — BACKGROUND: an aged parchment / vellum texture covering the WHOLE card, sepia-warm, subtle stains and fibres.
LAYER 2 — CONTENT (FULL BLEED): {SCENE}. {CHARACTER_SPECIFICATION} {COUNT_LOCK} — the scene is enlarged FULL-BLEED so its edges reach the card edges and slip slightly beneath the thin golden frame.
LAYER 3 — FRAME: a very thin, delicate METALLIC ANTIQUE-GOLD line-art gothic frame sitting close to the card edge, symmetrical, with small filigree corner flourishes — rich deep gold stroke with dark rim, bright core and a faint warm halo — painted ON TOP of the scene edges (foreground ornament over background content); stays THIN. NO medallion, NO emblem, NO icon, NO crest anywhere on the card.
LAYER 4 — TITLE: at the BOTTOM, the title "{TITLE}" in antique blackletter gold lettering whose baseline gently CURVES (letters rise at the ends, sag in the middle), placed DIRECTLY on the scene — NO title frame, NO plate, NO ribbon, NO cartouche, NO border around the text; clean carved edges with a thin shadow.

{SOFT_OBJECT_HALO}

{QUALITY_LOCK}

STRICT ANATOMY (HARD RULE): exactly two arms, two legs, one head and one torso per character; every joint (shoulder, elbow, wrist, hip, knee, ankle) must connect naturally to the body — NO extra limbs, NO limbs fused into the ribs, hip, chest or back, NO missing/amputated arms, NO deformed joints, NO wrong finger counts. Keep both arms clearly separated from the torso with visible armpits, elbows and wrists.

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, no heavy inner arch barriers, vintage gothic fine-art illustration, ultra-high detail.
```
