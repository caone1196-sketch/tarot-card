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

import requests
import streamlit as st
import numpy as np
import cv2
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
CARDS_DIR = os.path.join(ROOT, "cards")
DECK_JSON = os.path.join(CARDS_DIR, "deck.json")
STAR_REF = os.path.join(CARDS_DIR, "17-the-star.png")

# Thư viện lá bài trên GitHub (nguồn chính), local là dự phòng.
GITHUB_REPO = "caone1196-sketch/tarot-card"
GITHUB_REF = "arena/01a058af-tarot-card"
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
    """Ảnh lá bài: local nếu có, nếu không thì dùng thư viện GitHub (raw)."""
    local = os.path.join(CARDS_DIR, card["image"])
    if os.path.exists(local):
        return local
    return f"{GITHUB_RAW}/{card['image']}"


def group_of(slug: str) -> str:
    if slug[:2].isdigit():
        return "major"
    for key, _ in GROUPS:
        if slug.startswith(key + "-"):
            return key
    return "other"


def frame_rmse(img_path: str, ref: str = STAR_REF) -> float | None:
    """RMSE of the left 60px border strip vs the Star anchor (0..1)."""
    a = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    b = cv2.imread(ref, cv2.IMREAD_GRAYSCALE)
    if a is None or b is None:
        return None
    a = a[:, :60]
    b = b[:, :60]
    return float(np.sqrt(np.mean((a.astype(np.float64) - b.astype(np.float64)) ** 2)) / 255.0)


def rebuild_gallery():
    res = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "build_gallery.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    return res.returncode == 0, (res.stdout + res.stderr).strip()


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
    st.caption("Chuẩn khung: The Star · 100% nhân vật nữ 18–25")
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
                st.markdown(f"*Huy hiệu:* {c.get('emblem', '—')}")
                st.markdown(f"**Độ tuổi:** {c.get('age', '—')}")
                st.markdown(f"**Mái tóc:** {c.get('hair', '—')}")
                st.markdown(f"**Thân hình:** {c.get('build', '—')}")
                st.markdown(f"**Cảnh / chủ đề:** {c.get('scene', '—')}")
                rmse = frame_rmse(os.path.join(CARDS_DIR, c["image"]))
                if rmse is not None:
                    ok = "✅" if rmse <= 0.04 else "⚠️"
                    st.markdown(f"**Khung viền (RMSE vs The Star):** {rmse:.4f} {ok}")
            if st.button("Đóng chi tiết"):
                del st.session_state["detail_slug"]

# ---------------------------------------------------------------- upload
elif page == "📤 Tải lên lá bài":
    st.header("📤 Tải lên / thay thế lá bài")
    st.write("Tải ảnh PNG/JPG lên để thay thế một lá có sẵn, hoặc thêm lá mới. "
             "Ảnh sẽ được kiểm tra khung viền so với chuẩn The Star.")

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

            # preview frame RMSE
            tmp = "/tmp/_upload_preview.png"
            pil.save(tmp)
            rmse = frame_rmse(tmp)
            if rmse is not None:
                ok = "✅ khớp tốt" if rmse <= 0.04 else "⚠️ lệch nhiều"
                st.markdown(f"**Khung viền RMSE vs The Star:** {rmse:.4f} — {ok}")

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
            st.markdown(f"*Huy hiệu:* {c.get('emblem', '—')}")
            st.markdown(f"**Độ tuổi:** {c.get('age', '—')}")
            st.markdown(f"**Mái tóc:** {c.get('hair', '—')}")
            st.markdown(f"**Thân hình:** {c.get('build', '—')}")
            st.markdown(f"**Cảnh / chủ đề:** {c.get('scene', '—')}")

# ---------------------------------------------------------------- frame check
elif page == "ℹ️ Kiểm tra khung viền":
    st.header("ℹ️ Kiểm tra khung viền (RMSE vs The Star)")
    st.write("Đo độ lệch khung viền của từng lá so với lá chuẩn The Star. "
             "RMSE ≤ 0.04 được xem là khớp tốt.")
    cards = deck["cards"]
    if st.button("🔎 Quét toàn bộ 78 lá"):
        rows = []
        prog = st.progress(0.0, text="Đang quét…")
        for i, c in enumerate(cards):
            p = os.path.join(CARDS_DIR, c["image"])
            r = frame_rmse(p)
            rows.append((c["slug"], c["title"], r))
            prog.progress((i + 1) / len(cards), text=f"Đang quét {i + 1}/{len(cards)}")
        prog.empty()
        st.session_state["frame_rows"] = rows

    rows = st.session_state.get("frame_rows")
    if rows:
        import pandas as pd
        df = pd.DataFrame(rows, columns=["Slug", "Tên", "RMSE"])
        df["Trạng thái"] = df["RMSE"].apply(
            lambda r: "✅" if (r is not None and r <= 0.04) else ("⚠️" if r is not None else "?"))
        st.dataframe(df, use_container_width=True)
        st.download_button(
            "📥 Tải xuống CSV",
            df.to_csv(index=False).encode("utf-8"),
            "frame_rmse.csv",
            "text/csv",
        )
