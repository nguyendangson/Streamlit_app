import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px # interactive charts

#pip install pyttsx3
#pip install PyPDF2

#import PyPDF2
#from PyPDF2 import PdfReader
#from PyPDF2 import PdfFileReader
import pyttsx3
import espeak
#import os

from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

# path of the PDF file
#path = open('file.pdf', 'rb')
  
# creating a PdfFileReader object
#pdfReader = PdfReader(path)

# the page with which you want to start
# this will read the page of 25th page.
#from_page = pdfReader.pages[1]

Input_text=st.text_input("Input your Text to Speak:")
if Input_text:
    espeak.init()
    speak = espeak.Espeak()
    #speak = pyttsx3.init()
    speak.say(Input_text)
    speak.runAndWait()

# extracting the text from the PDF into strings
#text = from_page.extract_text()
  
# reading the text
#speak = pyttsx3.init()
#speak.say(text)
#speak.say("Hello World")
#speak.runAndWait()
#speak.stop()

#speak.save_to_file("Hello World", 'speech.mp3')
#speak.runAndWait()
#speak.stop()

# Different Voices
#voices = speak.getProperty('voices')
#for voice in voices:
#    print(voice, voice.id)
#    speak.setProperty('voice', voice.id)
#    speak.say("Hello World!")
#    speak.runAndWait()
#    speak.stop()

#rate = speak.getProperty('rate')
#print (rate)
#speak.setProperty('rate', 100) # Decrease the Speed Rate 

#volume = engine.getProperty('volume')
#print(volume)                            # current volume level
#speak.setProperty('volume', 2.0)



st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True )
