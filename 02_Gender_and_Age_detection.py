import streamlit as st
from PIL import Image
import numpy as np
import cv2 
import mediapipe as mp
import deepface
from deepface import DeepFace
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

#Face detection function by DeepFace of Facebook
# def deepface_detect(img):
#     demography = DeepFace.analyze(img, actions = ['age', 'gender', 'race', 'emotion'])

#     return demography

def deepface_detect(img):
    demography = DeepFace.analyze(img, actions = ['age'])

    return demography


def show_test(image2):
    backends = ['ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    image2 = image2.convert('RGB')
    image2 = np.array(image2)
    detection2=deepface_detect(image2)
    st.write("Age=",detection2[0]["age"])
    #st.write("Gender=",max(detection2[0]["gender"],key=detection2[0]["gender"].get))
    #st.write("Race=",max(detection2[0]["race"],key=detection2[0]["race"].get))

    # Emotion: happy, neutral, angry, sad, disgust and surprise
    #st.write("Emotion=",max(detection2[0]["emotion"],key=detection2[0]["emotion"].get))
    face_objs = DeepFace.detectFace(image2, detector_backend = backends[3])

    #st.image(image2,width=400)
    #st.image(face_objs,width=400)
#------------------------------------------------------------

st.subheader("DeepFace")
uploaded_file2=st.file_uploader("")
if st.button("Submit", key="submit2"):
    st.success('Success', icon="✅")
    image2 = Image.open(uploaded_file2)
    "Waiting seconds..."
    show_test(image2)


picture = st.camera_input("",key="picture")
if picture:
    picture = Image.open(picture)
    st.image(picture)
    st.success('Success', icon="✅")
    "Waiting seconds..."
    show_test(picture)
    #st.image("https://drive.google.com/file/d/1eDNB8HWWDEBVCBLqp_j8fhCaNMie3nq1/view?usp=share_link", width=300)

    
st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)
