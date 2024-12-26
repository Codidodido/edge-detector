import streamlit as st
from detector import *

st.set_page_config(page_title="EDGE DETECTOR")
ph = st.file_uploader(label="photo", type=".jpg") 
threshold =st.number_input(label="threshold", min_value=0, value=0)
if ph and (threshold != 0):
    old = Image.open(ph)
    # old = open_image("download.jpg")
    # old.save(ph._file_urls)
    col1, col2 = st.columns(2)
    with col1:
        st.image(old)
    with col2:
        processed_image = process_image(old , threshold)
        if process_image:
            output_path = "modified_image.jpg"
            processed_image.save(output_path)
            st.image(output_path)