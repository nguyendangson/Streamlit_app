import streamlit as st
from PIL import Image

from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

show_pages([
    Section(name="Home", icon="🏠"),
    Page("About.py", "About", "🧐"),
    Page("04_Contact.py", "Contact", "📪"),
    Section(name="Math", icon="🔢"),
    Page("03_Publications.py", "Publications", "📜"),
    Section(name="Data Science", icon="🤖"),
    Page("06_Stocks.py", "Stocks", "📈"),
    Page("02_Gender_and_Age_detection.py", "Detection", "👁️"),
    Section(name="Information Security", icon="🔐"),
    Page("05_Hacking.py", "Hack", "😈")
])

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1604147706283-d7119b5b822c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )



image = Image.open('Son Nguyen.jpg')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image,width=200)

"I am currently a Ph.D. candidate in Mathematics at The University of Alabama, Tuscaloosa. I am fortunate to be advised by Prof. [Kyungyong Lee](https://math.ua.edu/people/klee/). Before coming to Alabama, I earned a Master's degree in Optimization and Statistics at Wayne State University, Detroit, Michigan."

"I am interested in both Math and Computer Science. In Math, my research focuses on combinatorial problems related to Lie Theory and Representation Theory, especially Quiver Represetation and Cluster Algebras. I also love Geometric Invariant Theory, Geodesic Optimization and Orbit-Closure-Separation problems which surprisingly very closed to P"r"$\ne$""NP problem, Matrix Scaling, Tensor problems, and Tensor Normal Models in pure Computer Science (see [Avi Wigderson ICM talk](https://www.youtube.com/watch?v=oOnyful_oPY&ab_channel=InternationalMathematicalUnion))."

"In Computer Science, I am interested in machine learning, cryptography, hacking and security. I am trying to share cool projects I learned on the homepage with Streamlit of Python."
