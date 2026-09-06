# 🎨 look/ — Bộ chuẩn "THE STAR LOOK" cho 78 lá bài

Bộ kit **tạo look đồng nhất** (phong cách vẽ + tỉ lệ) neo theo lá chuẩn
`cards/17-the-star.png`. **Không thay đổi ảnh nào trong `cards/`.**

## Thành phần

```
look/
├── 00-STYLE-GUIDE.md      ← chuẩn look tổng (đọc trước)
├── template.md            ← master prompt template (điền chỗ trống)
├── prompts/               ← 78 prompt chuẩn hóa (mỗi lá 1 file .txt)
├── frame-template.png     ← khung chuẩn (bản sao cards/card-blank.png)
├── palette.png            ← ảnh mẫu bảng màu neo
└── build_prompts.py       ← script tái sinh 78 prompt từ tarot prompt/cards.json
```

## Cách dùng nhanh

1. **Xem chuẩn look**: mở `00-STYLE-GUIDE.md` (và `palette.png`).
2. **Lấy prompt một lá**:
   ```bash
   python3 look/build_prompts.py 00-fool
   ```
3. **Tái sinh toàn bộ 78 prompt**:
   ```bash
   python3 look/build_prompts.py
   ```
4. **Tạo lại một lá theo đúng look** (quy trình gợi ý):
   - Dán prompt của lá vào trình tạo ảnh (kèm ảnh tham chiếu `cards/17-the-star.png` nếu có hỗ trợ).
   - Ảnh ra phải đạt checklist ở mục 9 của `00-STYLE-GUIDE.md` (784×1360, khung RMSE ≤ 0.04, đúng số vật thể, đúng giải phẫu).
   - Nếu chỉ thay nội dung bên trong: ghép nội dung lên `frame-template.png` (cách neo khung xem `AGENTS.md` mục 4).

## Lưu ý

- Dữ liệu nguồn (scene / huy hiệu / tuổi / tóc / vóc dáng / khoá số lượng) lấy từ
  `tarot prompt/cards.json` — bảng chuẩn người dùng chỉ định.
- Bộ kit này là **dữ liệu dẫn xuất tham chiếu**, không ghi đè `cards/`, `tarot prompt/`
  hay `prompts/out/`.
