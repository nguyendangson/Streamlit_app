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