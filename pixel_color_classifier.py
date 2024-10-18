# © 2024 Numantic Solutions
# https://github.com/Numantic-NMoroney
# MIT License
#

import streamlit as st
from io import StringIO, BytesIO

from PIL import Image
import PIL.ImageOps


lut = PIL.Image.open("ml_color-k17-65x65x65.png")
# lut = PIL.Image.open("ml_color-k5-65x65x65.png")
# lut = PIL.Image.open("ml_color-k11-65x65x65.png")

w1 = lut.size[0]

def pixel_color_classify(img, lut):
    classfied = PIL.Image.new(mode="RGB", size=img.size)

    wide, high = img.size[0], img.size[1]
    for y in range(high) :
      # print (y, end=' ', flush=True)
      for x in range(wide) :
        pixel = img.getpixel((x, y))
        rq = int(pixel[0] / 4)
        gq = int(pixel[1] / 4)
        bq = int(pixel[2] / 4)
        xq = bq
        yq = gq + (rq * w1)
        qrgb = lut.getpixel((xq, yq))
        classfied.putpixel((x, y), (qrgb[0], qrgb[1], qrgb[2]))
    return classfied

st.header("Pixel Color Classifier")

with st.sidebar:
    st.markdown("Need a test image?")
    st.markdown("* [pencils](https://commons.wikimedia.org/wiki/File:Colouring_pencils.jpg)")
    st.markdown("* [yarn](https://commons.wikimedia.org/wiki/File:Bobines_fil_Rouffignac.jpg)")
    st.markdown("* [bangles](https://commons.wikimedia.org/wiki/File:Colourful_bangles_at_a_shop,_Colaba,_Mumbai.jpg)") 
    st.markdown("* [peppers](https://commons.wikimedia.org/wiki/File:Colorful_Bell_Peppers.JPG)")
    st.markdown("* [threads](https://commons.wikimedia.org/wiki/File:Colorful_(87069771).jpeg)")
    st.markdown("* [pottery](https://commons.wikimedia.org/wiki/File:Colorful_pottery.jpg)")
    st.markdown("* [powders](https://commons.wikimedia.org/wiki/File:Holi_shop.jpg)")
    st.markdown("* [daisies](https://commons.wikimedia.org/wiki/File:Colorful_Crazy_Daisies_(1)_(2530872878).jpg)")
    st.markdown("* [lichen](https://commons.wikimedia.org/wiki/File:At_the_Dewdrop_trail_viewpoint…colorful_lichens_(8467194826).jpg)")
    st.markdown("* [more yarn](https://commons.wikimedia.org/wiki/File:Rainbow_yarn_for_knitting,_display_in_front_of_a_needlework_shop_in_Graz,_Austria,_GW23-100.jpg)")
    st.markdown("---")
    st.markdown("This is a [Streamlit Community Cloud](https://streamlit.io/cloud) App with the following [privacy notice](https://streamlit.io/privacy-policy) and [terms of use](https://streamlit.io/terms-of-use)")

col_a, col_b = st.columns([0.8, 0.2])
with col_a:

    st.markdown("Apply radial SVM with 17 color term LUT to classify pixels.")
    st.markdown("This is an app from the [Machine Learning and Color](https://github.com/NMoroney/MachineLearningAndColor) repository.") 
    uploaded_file = st.file_uploader("Choose a JPG file", type='jpg')
    if uploaded_file is not None:
        bytes_ = uploaded_file.getvalue()

        img = Image.open(BytesIO(bytes_))
        wide, high = img.size
        ws = 500
        scale = float(ws) / wide
        hs = int(float(high) * scale)
        img = img.resize((ws, hs))

        st.image(img)

        st.markdown("---")

        classified = pixel_color_classify(img, lut)
        st.image(classified)

