import streamlit as st
from PIL import Image
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

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
st.header("Research Interest")
"- Quiver Representations, Cluster Algebras, Algebraic Combinatorics"

"- Representation theory, Lie groups and Lie algebras"

"- Character theory of finite groups (specially, of finite Coxeter-Weyl groups)"

"- Geometric invariant theory, Invariant Theory"

"- Modular forms and Automorphic forms"

"- Hyperbolic spaces"

st.header("Preprints")

st.header("Publications")
"- **Son Dang Nguyen**, [\"A proof of Lee-Lee's conjecture about geometry of rigid modules,\"](https://id.elsevier.com/as/authorization.oauth2?platSite=SD%2Fscience&scope=openid%20email%20profile%20els_auth_info%20els_idp_info%20els_idp_analytics_attrs%20els_sa_discover%20urn%3Acom%3Aelsevier%3Aidp%3Apolicy%3Aproduct%3Ainst_assoc&response_type=code&redirect_uri=https%3A%2F%2Fwww.sciencedirect.com%2Fuser%2Fidentity%2Flanding&authType=SINGLE_SIGN_IN&prompt=login&client_id=SDFE-v3&state=retryCounter%3D0%26csrfToken%3Dcab0d417-ad7d-4f7d-85af-40abe8472ce8%26idpPolicy%3Durn%253Acom%253Aelsevier%253Aidp%253Apolicy%253Aproduct%253Ainst_assoc%26returnUrl%3D%252Fscience%252Farticle%252Fabs%252Fpii%252FS0021869322004045%26prompt%3Dlogin%26cid%3Darp-3a4a63a7-8670-47dd-9b94-0c02e11738d6) " "J. Algebra 611 (2022), 422-434."
image1 = Image.open('Capture2.JPG')
image2 = Image.open('Capture3.JPG')
list_image=[image1,image2]
st.image(list_image,width=300)
#st.image(image1,width=300)
"The conjecture characterizes abstract algebraic properties of non-crossing curves on a punctured disk or a Riemann surface with many genus. The figures are main ideas to prove the conjecture."

"- **Son Dang Nguyen**, Ervin, Tucker J.; Jackson, Blake; Lane, Jay; Lee, Kyungyong; O'Donohue, Jack; Vaughan, Michael., [\"Permutations whose reverse shares the same recording tableau in the RS correspondence\"](https://www.mat.univie.ac.at/~slc/wpapers/s86jackson.pdf), Sém. Lothar. Combin. 86 (2022)"
st.latex(r'''
 |\{w \in \mathfrak{S}_n | \, Q(w) = Q(w^r)\}|= \left\{ \begin{gathered}
    {{2^{\frac{{n - 1}}{2}}}\left( \begin{gathered}
  n - 1 \\ 
  \frac{{n - 1}}{2} \\ 
\end{gathered}  \right)} {\text{ if n odd}}\\
   0  {\text{ if n even}}\\ 
\end{gathered}  \right.
    ''')

"- **Son Dang Nguyen**, [\"Constrained Fermat-Torricelli-Weber Problem in real Hilbert Spaces\"](https://arxiv.org/pdf/1806.04296.pdf)."

st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)