import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image

st.header("Starbucks in the US")
starbuck = pd.read_csv("starbucks_us_locations.csv")
starbuck = starbuck.iloc[:,[0,1]]
starbuck.columns = ['lon', 'lat']
#starbuck.dropna()
#starbuck= pd.DataFrame(starbuck, columns=['lat', 'lon'])

st.write(starbuck)
st.map(starbuck)


st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)
