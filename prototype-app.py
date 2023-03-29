import streamlit

import detection
import streamlit as st

# Streamlit Prototype APP
# To run : streamlit prototype-app.py

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
        # To read file as bytes:
        #bytes_data = uploaded_file.getvalue()
        #st.write(bytes_data)

        # To convert to a string based IO:
        #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        # To read file as string:
        #string_data = stringio.read()
        #st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        #dataframe = pd.read_csv(uploaded_file)
        #st.write(dataframe)

        #Read an image file
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

    #if st.button("Detect Trash in Image"):
        #result = detection.detect(detection.detection_graph, uploaded_file)
        #st.set_option('deprecation.showPyplotGlobalUse', False)
        #streamlit.pyplot(result)
        #output = predict_age(detection_graph, uploaded_file)
        #st.success('The age is {}'.format(output))

    picture = st.camera_input('Take a picture!')
    if picture is not None:
        # Read an image file
        image_data = Image.open(picture)

    if st.button("Check your picture for trash."):
        result = detection.detect(detection.detection_graph, picture)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        streamlit.pyplot(result)

       # if output == 1:
        #    st.markdown(safe_html,unsafe_allow_html=True)
       # elif output == 2:
         #   st.markdown(warn_html,unsafe_allow_html=True)
       # elif output == 3:
        #    st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
