import cv2
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_colors():
    return pd.read_csv('colors.csv', names=['color', 'color_name', 'hex', 'R', 'G', 'B'], header=None)

colors_df = load_colors()

def get_color_name(R, G, B):
    minimum = float('inf')
    cname = ""
    for i in range(len(colors_df)):
        d = abs(R - int(colors_df.loc[i, "R"])) + abs(G - int(colors_df.loc[i, "G"])) + abs(B - int(colors_df.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = colors_df.loc[i, "color_name"]
    return cname

st.title("Color Detection App")
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("Click on the image to detect color (use sliders for coordinates).")
    x = st.slider("X-coordinate", 0, image.shape[1]-1)
    y = st.slider("Y-coordinate", 0, image.shape[0]-1)

    pixel_color = image[y, x]
    R, G, B = int(pixel_color[0]), int(pixel_color[1]), int(pixel_color[2])
    color_name = get_color_name(R, G, B)

    st.markdown(f"**Color Name:** {color_name}")
    st.markdown(f"**RGB:** ({R}, {G}, {B})")
    st.markdown(f'<div style="width:150px;height:50px;background-color:rgb({R},{G},{B});border:1px solid #000;"></div>', unsafe_allow_html=True)