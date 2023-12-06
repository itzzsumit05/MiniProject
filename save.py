#Library
import streamlit as st
from PIL import Image
from keras.models import load_model
import json
from keras.utils import img_to_array
import numpy as np
from streamlit_lottie import st_lottie 

#Load Model.
model = load_model("modelv1.h5")

#UI
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

heart = load_lottiefile("Heart.json")
loading = load_lottiefile("Animation - 1701836245377.json")
col1,col2 = st.columns([2,1])
with col1:
    st.markdown("<h1 style='text-align: center;'>Tyre Health Analysis</h1>", unsafe_allow_html=True)
    
with col2:
    st_lottie(
    heart,
    speed=1,
    reverse=False,
    loop=True,
    height=100,
    width=100
    )
# img = Image.open("doctor.png")
# img = img.resize((200,200))
# st.image(img)   
str = 'Good'
red = 'E30505'
st.markdown("<h1 style='text-align: center;>&nbsp;</h1>", unsafe_allow_html=True)


#Upload File
uploaded_file = st.file_uploader("Choose Tire Image From Top..", type="jpg")
if uploaded_file is not None:
        #Preproccessing
        img = Image.open(uploaded_file)
        image = img.resize((256,256))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        #Predict
        y = model.predict(image)
        n = y[0][0]*10

        #Range Of Value
        if n>=0 and n<=2:
             str = 'Very Bad'
        elif n>2 and n<=4:
             str = 'Bad'
        elif n>4 and n<=6:
             str = 'Average'
        elif n>6 and n<=8:
             str = 'Good'
        elif n>8:
             str = 'Excellent'                   
        col3,col4 = st.columns([1,3])
        with col4:
            st.image(img, caption='Uploaded',width=200)
        st.write("Predicting....")

        #Indicator
        st.select_slider(
            'Tyre Health Rate',
            options=['Very Bad', 'Bad', 'Average', 'Good', 'Excellent'],
            value=(str))
        st.text(n)
           
            
        