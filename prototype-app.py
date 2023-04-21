import streamlit

import detection
import streamlit as st

# Streamlit Prototype APP
# To run : streamlit prototype.py

st.set_page_config(
    page_title="Trash Detection App",
    page_icon="♻️",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open('ecology.jpg')

st.image(image,
      use_column_width=True)


def main():
    st.title("Trash Object Detection")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Abalone Age Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        image_data = Image.open(uploaded_file)
    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> The Abalone is young</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> The Abalone is middle aged</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The Abalone is old</h2>
       </div>
    """


    picture = st.camera_input('Take a picture!')
    if picture is not None:
        # Read an image file
        image_data = Image.open(picture)

    if st.button("Check your picture for trash."):
        result = detection.detect(detection.detection_graph, picture)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        streamlit.pyplot(result)


if __name__=='__main__':
    main()
