# https://www.youtube.com/watch?v=MavAU3adGk4&ab_channel=Mr.PSolver
# https://www.youtube.com/watch?v=fB4qTzUjLaQ&ab_channel=MarcEvanstein%2Fmusic%E2%80%A4py
import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

#pip install scamp
#pip install scamp_extensions
import pandas as pd
from scamp import *
import scamp_extensions
from scamp_extensions.pitch import Scale
import math
from time import time

s = Session()

melodic_minor = Scale.melodic_minor(62)

strings = s.new_part("strings")
# strings = s.new_part("Clarinet")
# strings = s.new_part("Trumpet")

end = time() + 10 # run for 20 seconds

music=pd.DataFrame({"beat": [math.sin(s.beat())]})
chart=st.line_chart(data=music, width=300, height=500)

while time() < end:
    raw_pitch = math.sin(s.beat())
    #raw_pitch = 80 + 10 * math.cos(s.beat())
    #raw_pitch = 80 + 10 * math.sin(s.beat() * 3) + 8 * math.sin(s.beat() * 5)
    #raw_pitch = 80 + math.tan(s.beat())
    st.write([time(),s.beat()])
    new_data=pd.DataFrame({"beat": [math.sin(s.beat())]})
    chart.add_rows(new_data)
    #     raw_pitch = 80 + 10 * math.sin(100 / (0.1 + s.beat()))
    strings.play_note(melodic_minor.round(raw_pitch), 0.8, 0.05, "staccato")    # sin(x) with x from 0.8

# Fibonacci music 

st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True )