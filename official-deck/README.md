# 📜 SENSUAL GOTHIC TAROT — BỘ BÀI CHÍNH THỨC

Bộ bài **78 lá** theo khung bài mới: **4 lớp, vàng kim, KHÔNG biểu tượng** —
đang tiến hành từng nhóm, bắt đầu với **Ẩn Chính (Major Arcana — 22 lá)**.

## 📁 Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| `official-deck/major/` | **22 lá Ẩn Chính** (hoàn chỉnh, khung mới) |
| `official-deck/content/` | Ảnh nội dung **full-bleed chưa khung** (trung gian, có thể tái sinh) |
| `cards/` | Thư viện lịch sử / anchor The Star + các lá đã nâng cấp |

## 🎴 Khung bài chính thức (4 lớp)

1. **NỀN** — giấy da cổ phủ kín lá
2. **NỘI DUNG** — cảnh **tràn viền** (full-bleed), mép chui xuống khung
3. **KHUNG** — viền **vàng kim mảnh** sát lề, đè lên nội dung (KHÔNG medallion/biểu tượng)
4. **TÊN** — chữ **Blackletter cong** theo cung, đặt trực tiếp trên cảnh (không khung chữ)

## ✅ Tiến độ — ẨN CHÍNH (22 lá)

| # | Lá | File | Trạng thái |
|---|---|---|---|
| 0 | THE FOOL | `00-fool.png` | ✅ |
| 1 | THE MAGICIAN | `01-magician.png` | ✅ |
| 2 | THE HIGH PRIESTESS | `02-priestess.png` | ✅ |
| 3 | THE EMPRESS | `03-empress.png` | ✅ |
| 4 | THE EMPEROR | `04-emperor.png` | ✅ |
| 5 | THE HIEROPHANT | `05-hierophant.png` | ✅ |
| 6 | THE LOVERS | `06-lovers.png` | ✅ |
| 7 | THE CHARIOT | `07-chariot.png` | ✅ |
| 8 | STRENGTH | `08-strength.png` | 🔄 đang tạo |
| 9 | THE HERMIT | `09-hermit.png` | ✅ |
| 10 | WHEEL OF FORTUNE | `10-wheel.png` | ⏳ |
| 11 | JUSTICE | `11-justice.png` | ⏳ |
| 12 | THE HANGED MAN | `12-hanged.png` | ⏳ |
| 13 | DEATH | `13-death.png` | ⏳ |
| 14 | TEMPERANCE | `14-temperance.png` | ⏳ |
| 15 | THE DEVIL | `15-devil.png` | ⏳ |
| 16 | THE TOWER | `16-tower.png` | ⏳ |
| 17 | THE STAR | `17-the-star.png` | ✅ |
| 18 | THE MOON | `18-moon.png` | ⏳ |
| 19 | THE SUN | `19-sun.png` | ⏳ |
| 20 | JUDGEMENT | `20-judgement.png` | ⏳ |
| 21 | THE WORLD | `21-world.png` | ⏳ |

## 📤 Tái tạo

```bash
# Dựng lại asset khung (nếu thiếu) — tạo khung mới cho lá
python3 scripts/apply_new_frame.py kit
# Ghép nội dung vào khung mới
python3 scripts/compose_card.py <content.png> official-deck/major/<slug>.png --title "<NAME>"
```
