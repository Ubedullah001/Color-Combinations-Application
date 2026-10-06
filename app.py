import streamlit as st
import numpy as np
from skimage.color import lab2rgb

st.set_page_config(
    page_title="ColorLab",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 ColorLab")
st.write("Explore RGB colors and create colors using LAB values.")

# -------------------------
# Primary RGB Colors
# -------------------------
st.header("Primary RGB Colors")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔴 Red")
    st.color_picker("Red", "#FF0000", disabled=True)

with col2:
    st.markdown("### 🟢 Green")
    st.color_picker("Green", "#00FF00", disabled=True)

with col3:
    st.markdown("### 🔵 Blue")
    st.color_picker("Blue", "#0000FF", disabled=True)

# -------------------------
# LAB Color
# -------------------------
st.header("Create Color Using LAB")

L = st.slider("L* Lightness", 0.0, 100.0, 50.0)
A = st.slider("a* Green ↔ Red", -128.0, 127.0, 0.0)
B = st.slider("b* Blue ↔ Yellow", -128.0, 127.0, 0.0)

# LAB to RGB
lab = np.array([[[L, A, B]]])

rgb = lab2rgb(lab)[0][0]

r = int(rgb[0] * 255)
g = int(rgb[1] * 255)
b = int(rgb[2] * 255)

hex_color = f"#{r:02X}{g:02X}{b:02X}"

# -------------------------
# Result
# -------------------------
st.subheader("Generated Color")

st.markdown(
    f"""
    <div style="
        width:100%;
        height:180px;
        background-color:{hex_color};
        border-radius:15px;
        border:1px solid #ccc;
    "></div>
    """,
    unsafe_allow_html=True
)

st.write("### Color Values")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("L*", f"{L:.1f}")

with col2:
    st.metric("a*", f"{A:.1f}")

with col3:
    st.metric("b*", f"{B:.1f}")

st.write(f"**RGB:** ({r}, {g}, {b})")
st.write(f"**HEX:** {hex_color}")

st.info("Change the LAB values to create different colors.")
