import streamlit as st
from PIL import Image
import numpy as np

#import deepface
import cv2

from deepface import DeepFace
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

#import face_recognition

#Face detection function by OpenCV
#def Face_aged_gender_detection(image_name):
    #Loading pre-built models
    #age model
#    age_model = cv2.dnn.readNetFromCaffe("age.prototxt.txt", "dex_chalearn_iccv2015.caffemodel")
    #gender model
#    gender_model = cv2.dnn.readNetFromCaffe("gender.prototxt.txt", "gender.caffemodel")
#    img = cv2.imread(image_name)
#    gray = cv2.imread(image_name, 0)
    #plt.figure(figsize=(12,8))
    #plt.imshow(gray, cmap="gray")
    #plt.show()

#    cascPath = "haarcascade_frontalface_default.xml"
#    haar_detector = cv2.CascadeClassifier(cascPath)
#    faces = haar_detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw rectangle around the face
    #for (x, y, w, h) in faces:
    #    cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 255, 255), 3)

    #plt.figure(figsize=(12,8))
    #plt.imshow(gray, cmap="gray")
    #plt.show()

#    for x, y, w, h in faces:
#        detected_face = img[int(y):int(y+h), int(x):int(x+w)]

    #Caffe model expects (1, 3, 224, 224) shaped inputs but OpenCV loads (224, 224, 3) shaped images even if we resize. 
    # blobFromImage function under deep neural networks module of OpenCV transforms read images to the expected shape.
#    detected_face = cv2.resize(detected_face, (224, 224)) #img shape is (224, 224, 3) now
#    img_blob = cv2.dnn.blobFromImage(detected_face ) # img_blob shape is (1, 3, 224, 224)

    #Predictions
    # OpenCV requires to set input and call forward commands respectively to make predictions.
#    age_model.setInput(img_blob)
#    age_dist = age_model.forward()[0]
#    gender_model.setInput(img_blob)
#    gender_class = gender_model.forward()[0]
    #Firslty, age model returns 101 dimensional vector.
    # In the original study, element wise multiplication is applied to the output vector and index vector.
#    output_indexes = np.array([i for i in range(0, 101)])
#    apparent_predictions = round(np.sum(age_dist * output_indexes), 0)
    #Gender model returns 2 dimensional model.
    #If the 1st dimension value is greater than the 2nd one, then it is a woman
    #Vice versa, if the 2nd dimension value is greater than the 1st one, then it it is a man.
#    gender = 'Woman ' if np.argmax(gender_class) == 0 else 'Man'

    #Result
    #print("Age=",apparent_predictions,"Gender=",gender)
#    return [apparent_predictions,gender]


#Face detection function by DeepFace of Facebook
def deepface_detect(img):
    demography = DeepFace.analyze(img, actions = ['age', 'gender', 'race', 'emotion'])
    #image = cv2.imread(img)

    #print("Age: ", demography[0]["age"])
    #print("Gender: ", demography[0]["gender"])
    #print("Race: ", demography[0]["race"])
    #print("Emotion: ", demography[0]["emotion"])
    return demography


# Test
#st.header("Gender-and-Age-Detection")
#st.subheader("OpenCV")

#uploaded_file = st.file_uploader("", key="uploaded_file")
#submit=st.button("Submit", key="submit")
#if submit:
 #    image = Image.open(uploaded_file)
     #image.save("img_uploaded.jpg")
#    image_name="img_uploaded.jpg"
 #   detection=Face_aged_gender_detection(image_name)
 #   st.write("Age=",detection[0],",Gender=",detection[1])
  #   st.image(image,width=200)

def show_test(image2):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    image2 = image2.convert('RGB')
    image2 = np.array(image2)
    # image2 = open_cv_image[:, :, ::-1].copy()
    # opencvImage = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    # image2.save("img_uploaded.jpg")
    # image_name2="img_uploaded.jpg"
    detection2=deepface_detect(image2)
    # detection2=deepface_detect(image_name2)
    # deepface_detect(image2)
    st.write("Age=",detection2[0]["age"])
    # use max(hash,key=hash.get)
    st.write("Gender=",max(detection2[0]["gender"],key=detection2[0]["gender"].get))
    #st.write("Gender=",detection2[0]["gender"])
    st.write("Race=",max(detection2[0]["race"],key=detection2[0]["race"].get))
    #st.write("Race=",detection2[0]["race"])
    st.write("Emotion=",max(detection2[0]["emotion"],key=detection2[0]["emotion"].get))
    #st.write("Emotion=",detection2[0]["emotion"])
    face_objs=DeepFace.detectFace(image2, detector_backend = backends[4])
    #face_objs = DeepFace.extract_faces(img_path = image_name2, target_size = (224, 224), detector_backend = backends[4])

    st.image(image2,width=400)
    st.image(face_objs,width=400)
#------------------------------------------------------------

st.subheader("DeepFace")
uploaded_file2=st.file_uploader("")
if st.button("Submit", key="submit2"):
    image2 = Image.open(uploaded_file2)
    "Waiting seconds..."
    show_test(image2)


picture = st.camera_input("",key="picture")
if picture:
    picture = Image.open(picture)
    st.image(picture)
    #st.success('Success', icon="✅")
    "Waiting seconds..."
    show_test(picture)
    #st.image("https://drive.google.com/file/d/1eDNB8HWWDEBVCBLqp_j8fhCaNMie3nq1/view?usp=share_link", width=300)
    
    
st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)

    
        
