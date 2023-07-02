import streamlit as st
import numpy as np

st.title('Nama Kelompok')
st.write('&nbsp;Reno Julian Anggara &nbsp;&&nbsp; Faisa Syahla Syafani')

file = open("atuk.jpg", "rb")
image = file.read()

image_headline = widgets.Image(
                    value=image,
                    format='jpg',
                    width='250'
                )

label_headline = widgets.Label(
                    value='Photo by CDC on Unsplash',
                    style={'description_width': 'initial'}
                )

vbox_headline = widgets.VBox([image_headline, label_headline])