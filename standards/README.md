# `standards/` — bộ chuẩn KHUNG VIỀN đo được

Thư mục này chứa **chuẩn khung** của bộ bài, sinh tự động từ một lá neo bằng
`scripts/build_frame_standard.py`. Đây là số liệu đo trên ảnh thật, không phải mô tả ước lệ.

## Lá neo hiện tại: `17-the-star`

| File | Nội dung |
|---|---|
| `standard.json` | Chuẩn máy đọc được: kích thước, độ dày dải viền, vị trí nét kẻ, cửa sổ nội dung, có/không đĩa huy hiệu & ruy băng, **ngưỡng đạt** |
| `frame-mask.png` | 784×1360 · **trắng = vùng khung được chấm**, đen = cửa sổ nội dung (không chấm) |
| `anchor.sha256` | Hash lá neo **tại thời điểm sinh chuẩn** → QA cảnh báo nếu lá neo bị sửa mà chuẩn chưa regenerate |
| `profile-cols.csv`, `profile-rows.csv` | Hồ sơ độ phủ kim tuyến theo cột / theo hàng (0–199px từ mép) — chữ ký của viền |
| `frame-report.md`, `frame-report.json` | Kết quả chấm 78 lá gần nhất |

## Lệnh

```bash
# 1. Sinh / cập nhật chuẩn từ lá neo hiện tại
python3 scripts/build_frame_standard.py --force

# 2. Chấm cả bộ theo chuẩn (exit 1 nếu có lá lệch → dùng trong CI được)
python3 scripts/check_frame_standard.py

# 3. Đổi lá neo sang một lá khác (ví dụ sang kiểu viền gân vàng đang phổ biến)
python3 scripts/build_frame_standard.py --anchor cards/13-death.png \
        --out standards/13-death --force
python3 scripts/check_frame_standard.py --standard standards/13-death/standard.json
```

## Kết quả gần nhất (2026-09-03)

- Chuẩn: **784×1360**, viền `thin-line-art`, nét kẻ đầu ở `x=18`/`y=21`, dải viền 32·33·35·36 px,
  độ phủ kim tuyến **11.6 %**, **không** đĩa medallion, **không** ruy băng.
- **1/78 lá ĐẠT** (chính lá neo). 77 lá còn lại dùng kiểu *heavy-filigree*: viền gân vàng dày +
  medallion + ruy băng, độ phủ kim tuyến 43–92 % và **khớp nhau gần tuyệt đối**
  (tương quan cấu trúc cặp đôi 0.99–1.00).
- Nói cách khác: **The Star là lá ngoại lai** của bộ. Muốn cả bộ theo The Star thì phải vẽ lại
  hàng loạt; muốn The Star theo bộ thì vẽ lại 1 lá. **Chưa quyết định — không tự sửa ảnh.**

## Vì sao không còn dùng "RMSE dải 60px ≤ 0.04"

Thước đo cũ lấy luôn **màu nền** của lá vào phép so sánh, nên một lá nền parchment sáng
luôn "lệch" một lá nền trời đêm tối dù viền giống hệt nhau → báo 77/78 lỗi mà không nói **lỗi ở đâu**.
Chuẩn mới tách riêng: *vị trí nét kẻ* (band), *hình dạng viền* (struct_corr, mực viền chồng khít),
*lượng kim tuyến* (coverage) và *sự hiện diện của đĩa huy hiệu/ruy băng* (plates).
