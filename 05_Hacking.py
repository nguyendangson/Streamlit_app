import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()


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

"**Top popular cyber attacks:**"

"- SQL injection"

"- Cross Site Scripting (XSS)"

"- Cross-site request forgery (CSRF)"

"- Man-in-the-middle (MitM) attack"

"- Malware attack"

"- SSL/TSL attack"