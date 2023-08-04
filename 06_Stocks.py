import streamlit as st
import yfinance as yf
import pandas as pd
from yahoo_fin import stock_info
#from matplotlib.animation import FuncAnimation
from pandas_datareader import data as pdr
#from stock_pandas import StockDataFrame
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px # interactive charts

from dateutil.relativedelta import relativedelta
import time # to simulate a real time data, time loop
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()
#from st_pages import Page, show_pages, add_page_title

#Title= "📈Stocks"
#st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

import datetime as dt
from datetime import datetime
end = dt.datetime.now()
start = end - dt.timedelta(weeks=52)

def stocks(input):
    data = yf.download(input, start=start, end=end)
    max=round(data["Close"].max(),2)
    min=round(data["Close"].min(),2)
    real_price= round(stock_info.get_live_price(input),2)
    st.slider(input + " ("+ str(min) + ", " + str(real_price) + ", " + str(max) + ")", int(min), int(max), int(real_price))
    st.divider()
    #st.metric(label=input, value= stock_info.get_live_price(input),delta=stock_info.get_live_price(input)-price)

st.header("Trending Stocks" )
coll=st.columns(4)
with coll[0]:
    stocks("SCCO")
    stocks("FCX")
    stocks("TECK")
    stocks("COIN")
    stocks("BOIL")
    stocks("SOFI")
    stocks("UPST")
    stocks("CVNA")
    stocks("ROKU")
    stocks("PLTR")
    stocks("EXAS")
    stocks("PINS")
    stocks("ABBNY")
    stocks("ISNPY")
    stocks("UBER")
    stocks("UBS")
    stocks("CCL")
    stocks("DASH")
    stocks("WPM")
    stocks("W")
with coll[1]:
    stocks("U")
    stocks("GILD")
    stocks("Z")
    stocks("ZM")
    stocks("STLA")
    stocks("SIRI")
    stocks("QS")
    stocks("AFRM")
    stocks("RIVN")
    stocks("LCID")
    stocks("NIO")
    stocks("XPEV")
    stocks("LI")
    stocks("SQ")
    stocks("MU")
    stocks("HOOD")
    stocks("DPSGY")
    stocks("PYPL")
    stocks("RBLX")
    stocks("SHOP")
    stocks("DHI")
    stocks("MBLY")
    stocks("SMCI")
    stocks("PINS")
    stocks("UBER")
    stocks("ABNB")
    stocks("SBUX")
with coll[2]:
    stocks("MARA")
    stocks("RIOT")
    stocks("VCYT")
    stocks("PATH")
    stocks("TTD")
    stocks("HUBS")
    stocks("PGR")
    stocks("SCCO")
    stocks("DKNG")
    stocks("KBR")
    stocks("VRTX")
with coll[3]:
    stocks("DPST")
    stocks("YINN")
    stocks("EURL")
    stocks("INDL")
    stocks("KORU")
    stocks("BRZU")
    stocks("SYM")
    stocks("ITUB")
    stocks("ENPH")
    stocks("LKNCY")
    stocks("APLD")
    stocks("EXPE")

st.header("Top 1% Companies" )

data = yf.download("AAPL", start=start, end=end)

col=st.columns(4)
with col[0]:
    stocks("MSFT")
    stocks("GOOG")
    stocks("AMZN")
    stocks("NVDA")
    stocks("TSLA")
    stocks("BRK-B")
    stocks("META")
    stocks("TSM")
    stocks("V")
    stocks("LVMUY")
    stocks("TCEHY")
    stocks("UNH")
    stocks("LLY")
    stocks("XOM")
    stocks("JNJ")
    stocks("WMT")
    stocks("JPM")
    stocks("NVO")
    stocks("AVGO")
    stocks("MA")
    stocks("PG")
    stocks("ORCL")
    stocks("HD")

with col[1]:
    stocks("RHHBY")
    stocks("NSRGY")
    stocks("LRLCY")
    stocks("ABBV")
    stocks("BABA")    
    stocks("BAC")
    stocks("AZN")
    stocks("COST")
    stocks("ADBE")
    stocks("HESAY")
    stocks("IDCBY")
    stocks("PFE")
    stocks("TM")
    stocks("MCD")
    stocks("NVS")
    stocks("CSCO")
    stocks("SHEL")
    stocks("CVX")
    stocks("ASML")
    stocks("MRK")
    stocks("KO")
    stocks("PEP")

    #st.header("Big tech")
    #placeholder = st.empty()
    #for seconds in range(5):
        # creating a single-element container.
     #   with placeholder.container():
     #       stocks("aapl")
      #      stocks("msft")
      #      stocks("nflx")
      #      stocks("meta")
      #      time.sleep(1)   # need the code to real time     

with col[2]:
    stocks("AAPL")
    stocks("ABT")
    stocks("LIN")
    stocks("DHR")
    stocks("NKE")
    stocks("CMCSA")
    stocks("DIS")
    stocks("TXN")
    stocks("SAP")
    stocks("BHP")
    stocks("CHDRY")
    stocks("WFC")
    stocks("TMUS")
    stocks("HSBC")
    stocks("UPS")
    stocks("NEE")
    stocks("VZ")
    stocks("PROSY")
    stocks("INTC")
    stocks("MS")
    stocks("PM")
    stocks("SIEGY")
    stocks("RTX")

with col[3]:
    stocks("BA")
    stocks("RY")
    stocks("SNY")
    stocks("UL")
    stocks("SPGI")
    stocks("AXP")
    stocks("LOW")
    stocks("CAT")
    stocks("INTU")
    stocks("COP")
    stocks("IBM")
    stocks("TMO")
    stocks("CRM")
    stocks("ACN")
    stocks("NFLX")
    stocks("TTE")
    stocks("AMD")
    stocks("QCOM")
    stocks("HON")
    stocks("BMY")
#    st.header("Big Pharmacy")
#    placeholder1 = st.empty()
#    for seconds in range(5):
        # creating a single-element container.
#        with placeholder1.container():
 #           stocks("nvs")
  #          stocks("lly")
   #         stocks("sny")
    #        stocks("rhhby")
     #       stocks("azn")
     #       time.sleep(1)  



Input_stock=st.text_input("Input your Stock to analyze:")

if Input_stock:
    stock= yf.Ticker(Input_stock)
    data=stock.history(period="max")
    data["Dividend"]=stock.dividends
    data["Dividend"].fillna(0, inplace=True)  # fill empty to zero   
    data["50 moving avarege"]=data["Open"].rolling(window = 50, min_periods = 1).mean()
    data["150 moving avarege"]=data["Open"].rolling(window = 150, min_periods = 1).mean()
    data["200 moving avarege"]=data["Open"].rolling(window = 150, min_periods = 1).mean()
    tab1, tab2 = st.tabs(["Dividend", "History"])
    with tab1:
        # Use the Streamlit theme.
        # This is the default. So you can also omit the theme argument.
        #st.plotly_chart(fig, theme=None, use_container_width=True)
        #st.line_chart(stock.dividends, width=300, height=500)
        col1, col2= st.columns(2)
        with col1:
            st.write(stock.dividends)
        with col2:
            st.line_chart(stock.dividends, width=300, height=500)
    with tab2:
        # Use the native Plotly theme.
        st.write(data[["Open","Dividend","50 moving avarege","150 moving avarege","200 moving avarege"]])
        st.line_chart(data[["Open","50 moving avarege","150 moving avarege","200 moving avarege"]], width=300, height=500)
    
    st.header("News:")
    for i in stock.news:
        st.write(i["link"])
    # stock.revenue_forecasts
    # stock.earnings_forecasts
    # stock.analyst_price_target

    st.header("Real-time stock:")
    #fig, real_time_stock = plt.subplots()
    real_time_stock=pd.DataFrame({"Time": datetime.now().strftime("%H:%M:%S"), "Real time stock": [stock_info.get_live_price(Input_stock)]})
    #chart=st.line_chart(real_time_stock, width=300, height=500)
    chart=st.line_chart(data=real_time_stock, width=300, height=500)
    #plt.style.use("fivethirtyeight")
    #figure=plt.figure()
    #plt.plot([real_time_stock])
    #chart=st.pyplot(figure)
    #if "live_stock" not in st.session_state:
    #    st.session_state.live_stock = []

    while True:
        #real_time_stock.append(stock_info.get_live_price(Input_stock))
        #st.write(stock_info.get_live_price(Input_stock))
        new_data=pd.DataFrame({"Time": datetime.now().strftime("%H:%M:%S"), "Real time stock": [stock_info.get_live_price(Input_stock)]})
        chart.add_rows(new_data)
        time.sleep(1)
        #st.metric(label="Stock price", value=stock_info.get_live_price(Input_stock))

st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True )