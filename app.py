"""
Sensual Gothic Tarot — Streamlit app
Quản lý bộ bài: xem bộ sưu tập, tải lên/thay thế lá bài, rút bài ngẫu nhiên.

Chạy:
    streamlit run app.py --server.address=0.0.0.0 --server.port=8501
"""
import os
import io
import json
import subprocess
import sys
import base64
import re

import requests
import streamlit as st
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
CARDS_DIR = os.path.join(ROOT, "cards")
DECK_JSON = os.path.join(CARDS_DIR, "deck.json")
# Bộ chuẩn khung (viền) do scripts/build_frame_standard.py sinh từ lá neo hiện tại.
STANDARD_DIR = os.path.join(ROOT, "standards", "17-the-star")
CARD_NAME_RE = re.compile(r"^[A-Za-z0-9._-]+$")

# Thư viện lá bài trên GitHub (nguồn chính), local là dự phòng.
GITHUB_REPO = "caone1196-sketch/tarot-card"
GITHUB_REF = "arena/01a05dca-tarot-card"
GITHUB_API = f"https://api.github.com/repos/{GITHUB_REPO}/contents/cards"
GITHUB_RAW = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_REF}/cards"
GROUPS = [
    ("major", "Ẩn Chính"),
    ("wands", "Gậy"),
    ("cups", "Cốc"),
    ("swords", "Kiếm"),
    ("pentacles", "Tiền"),
]

st.set_page_config(page_title="Sensual Gothic Tarot", page_icon="🔮", layout="wide")


# ---------------------------------------------------------------- helpers
@st.cache_data(ttl=600, show_spinner=False)
def load_deck():
    # 1) local (đồng bộ với các commit đã push; upload ghi vào local)
    if os.path.exists(DECK_JSON):
        try:
            with open(DECK_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    # 2) fallback: thư viện trên GitHub (api.github.com — đọc được từ server)
    try:
        r = requests.get(
            f"{GITHUB_API}/deck.json", params={"ref": GITHUB_REF}, timeout=12
        )
        if r.status_code == 200:
            d = r.json()
            if d.get("encoding") == "base64":
                return json.loads(base64.b64decode(d["content"]).decode("utf-8"))
    except Exception:
        pass
    return {"total": 0, "cards": []}


def card_image_src(card):
    """Ảnh lá bài: local nếu có (tên phải an toàn), nếu không thì dùng thư viện GitHub (raw)."""
    local = safe_card_path(card.get("image", ""))
    if local and os.path.exists(local):
        return local
    name = os.path.basename(str(card.get("image", "")))
    return f"{GITHUB_RAW}/{name}"


def group_of(slug: str) -> str:
    if slug[:2].isdigit():
        return "major"
    for key, _ in GROUPS:
        if slug.startswith(key + "-"):
            return key
    return "other"


def safe_card_path(image_name: str) -> str | None:
    """Đường dẫn ảnh trong cards/ — chặn `..` và đường dẫn tuyệt đối (deck.json là dữ liệu)."""
    if not isinstance(image_name, str) or not CARD_NAME_RE.fullmatch(image_name):
        return None
    p = os.path.realpath(os.path.join(CARDS_DIR, image_name))
    return p if p.startswith(os.path.realpath(CARDS_DIR) + os.sep) else None


@st.cache_resource(show_spinner=False)
def load_frame_standard():
    """Bộ chuẩn khung sinh bởi scripts/build_frame_standard.py (neo: The Star hiện tại)."""
    std_file = os.path.join(STANDARD_DIR, "standard.json")
    if not os.path.exists(std_file):
        return None
    try:
        sys.path.insert(0, os.path.join(ROOT, "scripts"))
        from check_frame_standard import load_standard  # noqa: PLC0415
        return load_standard(std_file)
    except Exception as e:                     # thiếu cv2/numpy, chuẩn hỏng…
        st.session_state["_std_err"] = f"{type(e).__name__}: {e}"
        return None


def frame_deviation(img_path: str):
    """Chấm khung viền 1 lá theo bộ chuẩn. Trả dict của check_frame_standard hoặc None."""
    L = load_frame_standard()
    if L is None or not img_path or not os.path.exists(img_path):
        return None
    try:
        sys.path.insert(0, os.path.join(ROOT, "scripts"))
        from check_frame_standard import score_card  # noqa: PLC0415
        return score_card(img_path, L)
    except Exception:
        return None


def rebuild_gallery():
    res = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "build_gallery.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    return res.returncode == 0, (res.stdout + res.stderr).strip()


def _fmt_metric(key: str, v: dict) -> str:
    """Diễn giải 1 chỉ tiêu kiểm khung cho người dùng phổ thông."""
    if key == "size":
        return f"{v['measured'][0]}×{v['measured'][1]} (chuẩn {v['expected'][0]}×{v['expected'][1]})"
    if key == "coverage":
        return (f"độ phủ kim tuyến {v['measured'] * 100:.1f}% "
                f"(chuẩn {v['expected'] * 100:.1f}%, cho phép ±{v['tolerance'] * 100:.0f}%)")
    if key == "struct_corr":
        return f"tương quan cấu trúc viền {v['measured']:.3f} (tối thiểu {v['min']:.2f})"
    if key == "ink_iou":
        return f"mực viền chồng khít {v['measured']:.3f} (tối thiểu {v['min']:.2f})"
    if key == "band":
        d = v["delta_px"]
        return (f"độ dày dải viền lệch " + ", ".join(f"{k} {n}px" for k, n in d.items())
                + f" (cho phép ±{v['tolerance']}px)")
    if key == "plates":
        got = ", ".join(f"{k}={'có' if p else 'không'}" for k, p in v["measured"].items())
        return f"đĩa huy hiệu/ruy băng: {got} (chuẩn: " + ", ".join(
            f"{k}={'có' if p else 'không'}" for k, p in v["expected"].items()) + ")"
    return json.dumps(v, ensure_ascii=False)


def all_slugs():
    deck = load_deck()
    return [c["slug"] for c in deck["cards"]]


def slug_to_title(slug: str) -> str:
    deck = load_deck()
    for c in deck["cards"]:
        if c["slug"] == slug:
            return c["title"]
    return slug.replace("-", " ").title()


# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.title("🔮 Sensual Gothic Tarot")
    deck = load_deck()
    st.caption(f"Bộ bài {deck.get('total', len(deck.get('cards', [])))} lá")
    page = st.radio(
        "Chức năng",
        ["🖼️ Bộ sưu tập", "📤 Tải lên lá bài", "🎴 Rút một lá", "ℹ️ Kiểm tra khung viền"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Chuẩn khung: `standards/17-the-star` · sinh từ lá The Star hiện tại")
    st.caption(f"Thư viện lá bài: github.com/{GITHUB_REPO} · nhánh `{GITHUB_REF}`")

# ---------------------------------------------------------------- gallery
if page == "🖼️ Bộ sưu tập":
    st.header("🖼️ Bộ sưu tập")
    cards = deck["cards"]

    c_search, c_group, c_sort = st.columns([2, 1, 1])
    with c_search:
        q = st.text_input("Tìm kiếm", placeholder="Tên, huy hiệu, độ tuổi, chủ đề…")
    with c_group:
        group_sel = st.selectbox("Nhóm", ["Tất cả"] + [g[1] for g in GROUPS] + ["Khác"])
    with c_sort:
        sort_sel = st.selectbox("Sắp xếp", ["Theo bộ bài", "Theo tên"])

    filtered = []
    for c in cards:
        g = group_of(c["slug"])
        if group_sel != "Tất cả":
            want_key = next((k for k, v in GROUPS if v == group_sel), "other")
            if g != want_key:
                continue
        if q:
            hay = " ".join(str(c.get(k, "")) for k in ("title", "emblem", "age", "hair", "build", "scene")).lower()
            if q.lower() not in hay:
                continue
        filtered.append(c)

    if sort_sel == "Theo tên":
        filtered = sorted(filtered, key=lambda c: c["title"])

    st.caption(f"Hiển thị {len(filtered)} lá")
    if not filtered:
        st.info("Không có lá bài nào khớp.")
    else:
        n_cols = 6
        for i in range(0, len(filtered), n_cols):
            cols = st.columns(n_cols)
            for j, c in enumerate(filtered[i:i + n_cols]):
                with cols[j]:
                    st.image(card_image_src(c), width=200)
                    st.markdown(f"**{c['title']}**")
                    st.caption(c.get("age", "—"))
                    if st.button("Chi tiết", key=f"detail_{c['slug']}"):
                        st.session_state["detail_slug"] = c["slug"]

    if "detail_slug" in st.session_state:
        slug = st.session_state["detail_slug"]
        c = next((x for x in deck["cards"] if x["slug"] == slug), None)
        if c:
            st.divider()
            left, right = st.columns([1, 2])
            with left:
                st.image(card_image_src(c), width=360)
            with right:
                st.subheader(c["title"])
                if c.get("emblem"):
                    st.markdown(f"*Huy hiệu:* {c.get('emblem')}")
                st.markdown(f"**Độ tuổi:** {c.get('age', '—')}")
                st.markdown(f"**Mái tóc:** {c.get('hair', '—')}")
                st.markdown(f"**Thân hình:** {c.get('build', '—')}")
                st.markdown(f"**Cảnh / chủ đề:** {c.get('scene', '—')}")
                fr = frame_deviation(safe_card_path(c["image"]) or "")
                if fr:
                    st.markdown("**Khung viền** (so với `standards/17-the-star`): "
                                + ("✅ ĐẠT chuẩn" if fr["ok"] else "⚠️ LỆCH chuẩn"))
                    for k, v in fr["checks"].items():
                        if k.startswith("_"):
                            continue
                        st.caption(("· ✅ " if v.get("pass") else "· ⚠️ ")
                                   + f"`{k}`: {_fmt_metric(k, v)}")
                else:
                    st.caption("Chưa có bộ chuẩn khung — chạy `python3 scripts/build_frame_standard.py --force`.")
            if st.button("Đóng chi tiết"):
                del st.session_state["detail_slug"]

# ---------------------------------------------------------------- upload
elif page == "📤 Tải lên lá bài":
    st.header("📤 Tải lên / thay thế lá bài")
    st.write("Tải ảnh PNG/JPG lên để thay thế một lá có sẵn, hoặc thêm lá mới. "
             "Ảnh sẽ được chấm khung viền theo bộ chuẩn `standards/17-the-star/standard.json`.")

    up = st.file_uploader("Chọn ảnh lá bài", type=["png", "jpg", "jpeg"])
    if up is not None:
        raw = up.getvalue()
        try:
            pil = Image.open(io.BytesIO(raw)).convert("RGB")
        except Exception as e:
            st.error(f"Không đọc được ảnh: {e}")
            pil = None
        if pil is not None:
            w, h = pil.size
            st.write(f"Kích thước ảnh tải lên: **{w} × {h}**")
            if (w, h) != (784, 1360):
                st.warning("Kích thước chuẩn của bộ bài là 784 × 1360 (7:12). "
                           "Ảnh sẽ được giữ nguyên kích thước — có thể lệch tỷ lệ khi hiển thị.")

            slugs = all_slugs() + ["card-back", "card-blank"]
            default_slug = os.path.splitext(up.name)[0]
            default_idx = slugs.index(default_slug) if default_slug in slugs else 0
            target = st.selectbox(
                "Lá bài đích (thay thế)",
                slugs,
                index=default_idx,
                format_func=lambda s: slug_to_title(s) if not s.startswith("card-") else s,
            )

            c1, c2 = st.columns([1, 1])
            with c1:
                st.subheader("Xem trước ảnh tải lên")
                st.image(pil, width=280)
            with c2:
                st.subheader("Lá hiện tại")
                cur = os.path.join(CARDS_DIR, target + ".png")
                if os.path.exists(cur):
                    st.image(cur, width=280)
                else:
                    st.caption("(chưa có ảnh — sẽ thêm mới)")

            # preview theo bộ chuẩn khung
            import tempfile
            with tempfile.TemporaryDirectory(prefix="tarot-prev-") as td:
                tmp = os.path.join(td, "preview.png")
                pil.save(tmp)
                fr = frame_deviation(tmp)
            if fr:
                st.markdown("**Khung viền** (so với `standards/17-the-star`): "
                            + ("✅ ĐẠT chuẩn" if fr["ok"] else "⚠️ LỆCH chuẩn"))
                for k, v in fr["checks"].items():
                    if not k.startswith("_"):
                        st.caption(("· ✅ " if v.get("pass") else "· ⚠️ ") + f"`{k}`: {_fmt_metric(k, v)}")
            else:
                st.caption("Chưa đo được khung viền (thiếu bộ chuẩn hoặc ảnh không đọc được).")

            if st.button("💾 Lưu vào bộ bài", type="primary"):
                dest = os.path.join(CARDS_DIR, target + ".png")
                pil.save(dest)
                ok, msg = rebuild_gallery()
                load_deck.clear()
                st.cache_data.clear()
                if ok:
                    st.success(f"Đã lưu `{target}.png` và cập nhật gallery. {msg}")
                else:
                    st.error(f"Đã lưu ảnh nhưng cập nhật gallery thất bại: {msg}")

# ---------------------------------------------------------------- random
elif page == "🎴 Rút một lá":
    st.header("🎴 Rút một lá bài")
    if st.button("✦ Rút ngẫu nhiên", type="primary"):
        import random
        cards = deck["cards"]
        c = random.choice(cards)
        st.session_state["random_card"] = c
    c = st.session_state.get("random_card")
    if c:
        left, right = st.columns([1, 2])
        with left:
            st.image(card_image_src(c), width=380)
        with right:
            st.subheader(c["title"])
            if c.get("emblem"):
                st.markdown(f"*Huy hiệu:* {c.get('emblem')}")
            st.markdown(f"**Độ tuổi:** {c.get('age', '—')}")
            st.markdown(f"**Mái tóc:** {c.get('hair', '—')}")
            st.markdown(f"**Thân hình:** {c.get('build', '—')}")
            st.markdown(f"**Cảnh / chủ đề:** {c.get('scene', '—')}")

# ---------------------------------------------------------------- frame check
elif page == "ℹ️ Kiểm tra khung viền":
    st.header("ℹ️ Kiểm tra khung viền (theo bộ chuẩn The Star)")
    std = load_frame_standard()
    if std is None:
        st.warning(
            "Chưa tìm thấy bộ chuẩn khung ở `standards/17-the-star/`. Sinh lại bằng:\n\n"
            "```\npython3 scripts/build_frame_standard.py --force\n```"
        )
        st.stop()
    cards = deck["cards"]
    s_ = std["std"]
    st.caption(
        f"Chuẩn: `{s_['anchor_card']['slug']}` · {s_['card_size_wh'][0]}×{s_['card_size_wh'][1]} · "
        f"kiểu viền **{s_['frame_style']}** · độ phủ kim tuyến "
        f"{s_['frame']['gold_coverage_total'] * 100:.1f}% · dải viền {s_['frame']['band_px']} · "
        f"đĩa huy hiệu {s_['plates']['medallion']['present']}, ruy băng {s_['plates']['ribbon']['present']}"
    )
    st.caption(
        "Ngưỡng: độ phủ ±"
        f"{s_['tolerance']['gold_coverage_abs'] * 100:.0f}% · tương quan cấu trúc ≥"
        f"{s_['tolerance']['band_struct_corr_min']} · mực viền chồng khít ≥"
        f"{s_['tolerance']['frame_ink_iou_min']} · độ dày dải ±{s_['tolerance']['rule_offset_px']}px"
    )
    if st.button("🔎 Quét toàn bộ", type="primary"):
        rows = []
        prog = st.progress(0.0, text="Đang quét…")
        for i, c in enumerate(cards):
            p = safe_card_path(c["image"]) or ""
            r = frame_deviation(p)
            ck = (r or {}).get("checks", {})
            rows.append({
                "Slug": c["slug"], "Tên": c["title"],
                "Đạt": "✅" if (r or {}).get("ok") else "⚠️",
                "Phủ kim tuyến %": round(100 * ck.get("coverage", {}).get("measured", 0), 1),
                "Tương quan": round(ck.get("struct_corr", {}).get("measured", 0), 3),
                "Chồng khít": round(ck.get("ink_iou", {}).get("measured", 0), 3),
                "Lệch dải (px)": max(ck.get("band", {}).get("delta_px", {"x": 0}).values()),
                "Chỉ tiêu lệch": ", ".join((r or {}).get("failed", ["—"])),
            })
            prog.progress((i + 1) / max(1, len(cards)), text=f"Đang quét {i + 1}/{len(cards)}")
        prog.empty()
        st.session_state["frame_rows"] = rows

    rows = st.session_state.get("frame_rows")
    if rows:
        import pandas as pd
        df = pd.DataFrame(rows)
        n_ok = int((df["Đạt"] == "✅").sum())
        st.info(f"{n_ok}/{len(df)} lá ĐẠT chuẩn · {len(df) - n_ok} lá lệch. "
                "Lệch khung ở đây là **lệch thị giác thật**, không phải lỗi kích thước.")
        st.dataframe(df, width="stretch")
        st.download_button(
            "📥 Tải xuống CSV",
            df.to_csv(index=False).encode("utf-8"),
            "frame_check.csv",
            "text/csv",
        )
