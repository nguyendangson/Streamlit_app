import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image

from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

show_pages([
    Section(name="Home", icon="🏠"),
    Page("About.py", "About ", "🧐"),
    Page("03_Publications.py", "Research", "ℼ"),
    Page("12_Activities.py", "Activities", "🤝"),
    Page("11_Teaching.py", "Teaching", "👨‍🏫"),
    #Page("CV.py", "CV", "📋"),
    Page("04_Contact.py", "Contact me", "📪"),
    #Section(name="Math", icon="🔢"),
    Section(name="Data Science", icon="🤖"),
    Page("06_Stocks.py", "Stocks", "📈"),
    #Page("02_Gender_and_Age_detection.py", "Detection", "👁️"),
    Page("10_Data_Map.py", "Data Map", "🌍"),
    Page("13_Natural_Language_Processing.py", "Natural Language Processing", "🔠"),
    #Page("14_Music_and_Songs_Generated.py", "Music and Songs Generated", "♬♪"),
    
    #Section(name="Information Security", icon="🔐"),
    #Page("05_Hacking.py", "Hack", "😈")
])

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-gray-geometric-pattern-background-vector_53876-136510.jpg?w=1060&t=st=1681246927~exp=1681247527~hmac=175d0a73d7a955330a694cda7e115db8bae29571a0caa75cae2b4f35da35a9dc");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

image = Image.open('Son Nguyen.jpg')
st.header("Son Dang Nguyen")
st.image(image, width=400)

"I am currently a Ph.D. candidate in Mathematics at The University of Alabama, Tuscaloosa. I am fortunate to be advised by Prof. [Kyungyong Lee](https://math.ua.edu/people/klee/). Before coming to Alabama, I earned a Master's degree in Optimization and Statistics at Wayne State University, Detroit, Michigan."

"I am interested in both Math and Computer Science. In Math, my research focuses on combinatorial problems related to Lie Theory and Representation Theory, especially Quiver Represetation and Cluster Algebras. I also love Geometric Invariant Theory, Geodesic Optimization and Orbit-Closure-Separation problems which surprisingly very closed to P"r"$\ne$""NP problem, Matrix Scaling, Tensor problems, and Tensor Normal Models in pure Computer Science (see [Avi Wigderson ICM talk](https://www.youtube.com/watch?v=oOnyful_oPY&ab_channel=InternationalMathematicalUnion))."

"In Computer Science, I am interested in machine learning. I am trying to share cool projects I learned on the homepage with Streamlit of Python."

st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)
