#!/usr/bin/env python3
"""
KHUNG BÀI MỚI — 4 lớp, KHÔNG huy hiệu (no emblem medallion).

Cấu trúc 4 lớp (từ dưới lên):
  1. NỀN          : giấy da cổ aged parchment phủ kín cả lá  (01-background-parchment.png)
  2. NỘI DUNG     : artwork TRÀN VIỀN — phủ kín 784x1360, mép nội dung chui
                     xuống DƯỚI khung hoạ tiết                        (02-content-*.png)
  3. KHUNG HỌA TIẾT MẢNH: khung viền vàng mảnh, sát lề lá, đè LÊN nội dung
                                                                    (03-frame-thin-clean.png)
  4. KHUNG TÊN    : dải băng trang trí ở đáy + tên lá chữ Gothic    (04-title-band-clean.png)

KHÔNG còn oval medallion / huy hiệu ở đỉnh (bỏ khung biểu tượng).

Usage:
  python3 scripts/apply_new_frame.py kit                  # dựng lại các asset trong variants/frame-kit/
  python3 scripts/apply_new_frame.py blank                # dựng lại cards/card-blank.png + .jpg
  python3 scripts/apply_new_frame.py card <slug> --content <raw.png> [--title "TEXT"]
  python3 scripts/apply_new_frame.py star                 # dựng lại mốc chuẩn cards/17-the-star.png
"""

import json
import sys
from pathlib import Path

import math as _m

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CARDS_DIR = ROOT / "cards"
LAYERS_DIR = ROOT / "variants" / "layers"
KIT_DIR = ROOT / "variants" / "frame-kit"
CARDS_JSON = ROOT / "tarot prompt" / "cards.json"

W, H = 784, 1360                      # kích thước lá bài chuẩn
FONT = ROOT / "variants" / "fonts" / "UnifrakturCook-Bold.ttf"
GOLD = (255, 226, 150)                # vàng chữ — khớp tên trong title band
GOLD_EDGE = (70, 40, 10)
TEXT_CENTER_Y = 1224                  # tâm midline khung chữ cartouche (plate y 1156..1290)
TEXT_MAX_W = 320                      # bề rộng tối đa của dòng tên (trong plate x 159..625)
TEXT_SAG = 6.0                        # độ võng giữa plate (px) — chữ cong theo khung chữ

PARCHMENT = LAYERS_DIR / "01-background-parchment.png"
STAR_CONTENT = LAYERS_DIR / "02-content-the-star.png"
FRAME_SRC = LAYERS_DIR / "03-frame-filigree.png"
TITLE_SRC = LAYERS_DIR / "04-title-the-star.png"

# asset xuất ra (clean)
KIT_PARCHMENT = KIT_DIR / "01-background-parchment.png"
KIT_STAR_CONTENT = KIT_DIR / "02-content-the-star-fullbleed.png"
KIT_FRAME = KIT_DIR / "03-frame-thin-clean.png"
KIT_TITLE_BAND = KIT_DIR / "04-title-band-clean.png"
KIT_PREVIEW = KIT_DIR / "05-preview-4-layers.png"


# ---------------------------------------------------------------- tools
def load_rgba(path: Path) -> Image.Image:
    return Image.open(path).convert("RGBA")


def ensure_kit() -> None:
    """Tự dựng lại các asset khung trong variants/frame-kit/ nếu bị xoá.

    frame-kit là file tái tạo được (đã ở trong .gitignore); mọi lệnh compose/
    blank/star đều gọi hàm này để luôn có asset khung dùng chung."""
    if not (KIT_FRAME.exists() and KIT_PARCHMENT.exists()):
        build_kit()


# Bảng màu vàng kim (metallic antique gold)
GOLD_PALETTE = {
    "shadow": np.array([96, 52, 8], np.float32),     # viền tối — tạo cảm giác kim loại
    "mid": np.array([228, 168, 52], np.float32),     # thân nét vàng
    "core": np.array([255, 228, 132], np.float32),   # lõi sáng
    "glow": np.array([255, 198, 84], np.float32),    # quầng sáng ấm
}


def _rgba(rgb: np.ndarray, alpha: np.ndarray) -> Image.Image:
    """Dựng ảnh RGBA từ mảng màu (H,W,3) + alpha (H,W) 0..255."""
    arr = np.dstack([np.clip(rgb, 0, 255).astype(np.uint8),
                     np.clip(alpha, 0, 255).astype(np.uint8)])
    return Image.fromarray(arr, "RGBA")


def regild_frame(src: Path, dst: Path, thr: int = 40,
                 glow_sigma: float = 2.0, glow_strength: float = 0.55,
                 rim_width: int = 1) -> None:
    """Mạ lại hoạ tiết vàng theo phong cách VÀNG KIM NỔI BẬT — vẫn giữ nét mảnh.

    - Bỏ 'bụi sao' mờ (alpha < thr) như cũ.
    - Giữ NGUYÊN mask nét (độ mảnh không đổi), chỉ tô lại màu:
        viền tối 1px quanh nét + thân vàng đậm + lõi sáng + quầng vàng ấm mảnh.
    - Quầng sáng tạo độ nổi khỏi nền giấy da cổ / cảnh tối mà không làm dày nét.
    """
    im = load_rgba(src)
    a = np.array(im).astype(np.float32)
    alpha = a[..., 3].copy()
    alpha[alpha < thr] = 0.0
    m = alpha / 255.0                      # độ phủ 0..1 (KHÔNG đổi)
    stroke = (alpha >= 180).astype(np.float32)  # chỉ NÉT CHÍNH (không phủ nền mờ)

    # quầng sáng ấm quanh NÉT (mờ, thấp — chỉ tạo độ nổi; nền mờ không bị vàng hoá)
    glow_a = np.clip(cv2.GaussianBlur(stroke, (0, 0), glow_sigma) * glow_strength, 0, 1) * 255
    glow_rgb = np.broadcast_to(GOLD_PALETTE["glow"], m.shape + (3,)).copy()

    # viền tối sát mép ngoài nét (kim loại)
    k = np.ones((3, 3), np.uint8)
    rim = np.clip(cv2.dilate(stroke, k, iterations=rim_width) - stroke, 0, 1)
    rim = cv2.GaussianBlur(rim, (0, 0), 0.6)
    rim_a = np.clip(rim * 0.85, 0, 1) * 255
    rim_rgb = np.broadcast_to(GOLD_PALETTE["shadow"], m.shape + (3,)).copy()

    # thân nét: vàng đậm → lõi sáng theo độ phủ nét + độ sáng gốc
    lum = a[..., :3].mean(2) / 255.0
    t = np.clip(1.1 * stroke + 0.45 * lum - 0.45, 0, 1)
    gilded = (GOLD_PALETTE["mid"][None, None, :] * (1 - t[..., None])
              + GOLD_PALETTE["core"][None, None, :] * t[..., None])

    # giữ nguyên màu pixel cho vùng nền mờ (fill plate), chỉ đổi màu ở nét chính
    body = a[..., :3] * (1 - stroke[..., None]) + gilded * stroke[..., None]

    out = Image.new("RGBA", (m.shape[1], m.shape[0]), (0, 0, 0, 0))
    out.alpha_composite(_rgba(glow_rgb, glow_a))
    out.alpha_composite(_rgba(rim_rgb, rim_a))
    out.alpha_composite(_rgba(body, alpha))
    out.save(dst)
    print(f"frame regilded: {dst}  (px alpha>0 = {int((alpha > 0).sum())})")


def strip_title_text(src: Path, dst: Path) -> None:
    """(Cũ — giữ lịch sử) Xoá chỉ phần CHỮ trong dải băng mở.

    KHÔNG dùng nữa: khung tên mới là cartouche khép kín (build_closed_band).
    """
    im = load_rgba(src)
    a = np.array(im)
    alpha = a[..., 3].astype(np.uint8).copy()
    x0, x1, y0, y1 = 272, 534, 1206, 1251
    alpha[y0:y1, x0:x1] = 0
    a[..., 3] = alpha
    Image.fromarray(a).save(dst)
    print(f"title band clean (legacy): {dst}")


def _spiral(d: ImageDraw.ImageDraw, cx: float, cy: float,
            r_out: float, turns: float, line, width: int = 2,
            start_angle: float = 0.0) -> None:
    """Vẽ xoắn ốc (scroll roll) bằng đường liền — đầu cuộn của khung chữ."""
    pts = []
    steps = int(turns * 360 / 6)
    for i in range(steps + 1):
        t = i / steps * turns * 2 * _m.pi
        r = r_out * (1.0 - 0.62 * (t / (turns * 2 * _m.pi)))
        pts.append((cx + r * _m.cos(t + start_angle),
                    cy + r * _m.sin(t + start_angle)))
    d.line(pts, fill=line, width=width, joint="curve")


def build_closed_band(dst: Path) -> None:
    """KHUNG CHỮ KHÉP KÍN — cartouche viền đóng hoàn toàn, hai đầu xoắn ốc.

    Thay cho dải băng "scroll hở" cũ (hai đuôi bay tự do, nét đáy lỏng):
    - Tấm plate bo góc (radius 26px) ở đáy lá, viền VÀNG KIM MẢNH đôi
      (ngoài 3px + trong 2px) — khép kín 100%, không hở mép.
    - Hai đầu: xoắn ốc scroll cổ (2.2 vòng) nối liền vào mép plate và
      kết thúc bằng 1 vòng lõi — mọi đường nét đều khép kín.
    - Nền plate phủ mờ (rgba 38,26,12 ~48%) để chữ nổi trên mọi nền mà
      nội dung tràn viền vẫn thấp thoáng.
    - Bố cục khớp text zone: plate x 150..634, y 1156..1290;
      chữ cong nằm gọn bên trong (x 232..552, y ~1204..1244).
    Màu nét trung gian (205,160,84) — regild_frame mạ vàng kim đồng bộ.
    """
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 150, 1156, 634, 1290
    r = 26
    line = (205, 160, 84, 255)
    # plate mờ (nội dung thấp thoáng — đủ đậm để chữ nổi trên nền sáng)
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=(38, 26, 12, 156))
    # viền ngoài + viền trong — KHÉP KÍN
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, outline=line, width=3)
    d.rounded_rectangle([x0 + 9, y0 + 9, x1 - 9, y1 - 9], radius=max(r - 9, 8),
                        outline=line, width=2)
    # hai đầu: xoắn ốc scroll cổ nối liền plate (2 vòng, lõi khép kín)
    cy = (y0 + y1) / 2
    _spiral(d, x0, cy, 20, 2.4, line, width=2, start_angle=_m.pi / 2)
    _spiral(d, x1, cy, 20, 2.4, line, width=2, start_angle=-_m.pi / 2)
    im.save(dst)
    print(f"closed title band: {dst}")


def draw_tracked(img: Image.Image, xy: tuple, title: str, font, tracking: int,
                 fill, stroke_width: int = 0, stroke_fill=None) -> None:
    """Vẽ chữ có letter-spacing; anchor 'mm' căn giữa theo tâm dòng."""
    d = ImageDraw.Draw(img)
    widths = [d.textlength(ch, font=font) for ch in title]
    total = sum(widths) + tracking * (len(title) - 1)
    x = xy[0] - total / 2
    for ch, cw in zip(title, widths):
        d.text((x + cw / 2, xy[1]), ch, font=font, anchor="mm",
               fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)
        x += cw + tracking


def curve_y(x: float, half_w: float, sag: float = TEXT_SAG) -> float:
    """Midline của dải băng — parabol võng xuống giữa (cong theo khung chữ).

    y = center + sag * ((x - cx)/half_w)^2  (giữa thấp hơn hai mép).
    """
    return TEXT_CENTER_Y + sag * ((x - W / 2) / max(half_w, 1.0)) ** 2


def draw_curved(img: Image.Image, title: str, font, tracking: int, fill,
                half_w: float, shadow: bool = False) -> None:
    """Vẽ chữ CONG THEO CUNG PARABOL của dải băng.

    Mỗi ký tự được vẽ riêng trên một tile, xoay theo tiếp tuyến của cung tại
    tâm ký tự rồi dán vào đúng vị trí trên midline — chữ ôm theo khung chữ.
    - half_w: nửa bề rộng dòng chữ (tỉ lệ độ cong).
    """
    d = ImageDraw.Draw(img)
    widths = [d.textlength(ch, font=font) for ch in title]
    total = sum(widths) + tracking * (len(title) - 1)
    x0 = W / 2 - total / 2
    x = x0
    tile_h = 120
    for ch, cw in zip(title, widths):
        cx = x + cw / 2
        cy = curve_y(cx, half_w)
        # tiếp tuyến tại cx: dy/dx
        eps = 0.5
        slope = (curve_y(cx + eps, half_w) - curve_y(cx - eps, half_w)) / (2 * eps)
        ang = _m.degrees(_m.atan(slope))

        tile = Image.new("RGBA", (int(cw) + 24, tile_h), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        td.text((12, tile_h / 2), ch, font=font, anchor="lm", fill=fill)
        if shadow:
            td.text((12, tile_h / 2 + 1), ch, font=font, anchor="lm",
                    stroke_width=2, stroke_fill=(12, 6, 0, 200))
        tile = tile.rotate(-ang, resample=Image.BICUBIC, expand=False,
                           fillcolor=(0, 0, 0, 0))

        # căn tâm nét chữ vào (cx, cy)
        a = np.asarray(tile)[..., 3]
        ys, xs = np.nonzero(a > 30)
        if len(xs):
            kx, ky = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
            img.alpha_composite(tile, (int(round(cx - kx)), int(round(cy - ky))))
        x += cw + tracking


def render_title(title: str) -> Image.Image:
    """Vẽ tên lá bằng UnifrakturCook-Bold (Blackletter), chữ CONG theo khung.

    - Cỡ chữ: lớn nhất sao cho dòng tên nằm gọn giữa 2 mép cuộn ruy băng
      (interior ~ x 230..560 → TEXT_MAX_W = 320px), thân chữ ≤36px.
    - Chữ chạy trên midline parabol (võng TEXT_SAG ≈ 5px) — cong theo chính
      đường cong của khung chữ; mỗi ký tự xoay theo tiếp tuyến.
    """
    tracking = 3
    font = None
    for size in range(52, 17, -1):
        f = ImageFont.truetype(str(FONT), size)
        probe_img = Image.new("RGBA", (1500, 300), (0, 0, 0, 0))
        probe = ImageDraw.Draw(probe_img)
        probe.text((750, 150), title, font=f, anchor="mm", fill=(255, 255, 255, 255))
        a = np.asarray(probe_img)[..., 3]
        ys, xs = np.nonzero(a > 30)
        w, h = xs.max() - xs.min(), ys.max() - ys.min()
        if h <= 36 and w + tracking * (len(title) - 1) <= TEXT_MAX_W:
            font = f
            break
    if font is None:
        font = ImageFont.truetype(str(FONT), 18)

    # tính nửa bề rộng dòng (để độ cong tỉ lệ với chiều dài chữ)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    probe_w = sum(probe.textlength(ch, font=font) for ch in title) + tracking * (len(title) - 1)
    half_w = max(probe_w / 2, 1.0)

    # vẽ bóng trước rồi chữ vàng lên trên (cùng đường cong)
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_curved(shadow, title, font, tracking, (12, 6, 0, 200), half_w, shadow=True)
    shadow = shadow.filter(ImageFilter.GaussianBlur(1.6))
    img = shadow
    draw_curved(img, title, font, tracking, GOLD + (255,), half_w)
    return img


def cover_resize(img: Image.Image, w: int, h: int) -> Image.Image:
    """Scale giữ tỷ lệ, phủ kín (cover) khung w x h, crop phần thừa."""
    scale = max(w / img.width, h / img.height)
    nw, nh = int(round(img.width * scale)), int(round(img.height * scale))
    img = img.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return img.crop((left, top, left + w, top + h))


def compose(content: Image.Image | None, title: str | None) -> Image.Image:
    ensure_kit()
    canvas = load_rgba(KIT_PARCHMENT).convert("RGBA")
    if content is not None:
        c = cover_resize(content.convert("RGB"), W, H).convert("RGBA")
        canvas.alpha_composite(c)
    canvas.alpha_composite(load_rgba(KIT_FRAME))
    # KHÔNG còn khung chữ (cartouche/ribbon) — chỉ giữ tên lá cong trực tiếp
    if title:
        canvas.alpha_composite(render_title(title))
    return canvas.convert("RGB")


def build_kit() -> None:
    KIT_DIR.mkdir(parents=True, exist_ok=True)
    # 1. nền
    Image.open(PARCHMENT).convert("RGB").save(KIT_PARCHMENT)
    # 2. ví dụ nội dung tràn viền (The Star)
    Image.open(STAR_CONTENT).convert("RGB").save(KIT_STAR_CONTENT)
    # 3. khung hoạ tiết mảnh — mạ vàng kim nổi bật (KHÔNG có khung chữ)
    regild_frame(FRAME_SRC, KIT_FRAME)
    # 4. xem trước: ghép các lớp (The Star) để đối chiếu — tên lá cong, không khung
    preview = compose(content=Image.open(KIT_STAR_CONTENT).convert("RGB"), title="THE STAR")
    preview.save(KIT_PREVIEW)


def build_blank() -> None:
    out = compose(content=None, title=None)
    out.save(CARDS_DIR / "card-blank.png")
    out.save(CARDS_DIR / "card-blank.jpg", quality=88)
    print(f"blank -> cards/card-blank.png + card-blank.jpg {out.size}")


def build_star() -> None:
    content = Image.open(KIT_STAR_CONTENT).convert("RGB")
    out = compose(content=content, title="THE STAR")
    out.save(CARDS_DIR / "17-the-star.png")
    print("anchor -> cards/17-the-star.png", out.size)


def build_card(slug: str, content_path: Path, title: str | None) -> None:
    content = Image.open(content_path).convert("RGB")
    if title is None:
        data = json.loads(CARDS_JSON.read_text(encoding="utf-8"))
        card = next((c for c in data["cards"] if c["slug"] == slug), None)
        title = card["title"] if card else slug.replace("-", " ").upper()
    out = compose(content=content, title=title)
    out.save(CARDS_DIR / f"{slug}.png")
    print(f"card -> cards/{slug}.png ({title}) {out.size}")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "kit":
        build_kit()
    elif cmd == "blank":
        build_blank()
    elif cmd == "star":
        build_star()
    elif cmd == "card":
        if len(sys.argv) < 4 or "--content" not in sys.argv:
            print("Usage: apply_new_frame.py card <slug> --content <raw.png> [--title TEXT]")
            sys.exit(1)
        slug = sys.argv[2]
        content_path = Path(sys.argv[sys.argv.index("--content") + 1])
        title = None
        if "--title" in sys.argv:
            title = sys.argv[sys.argv.index("--title") + 1]
        build_card(slug, content_path, title)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
