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

import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time # to simulate a real time data, time loop
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()
#from st_pages import Page, show_pages, add_page_title

#Title= "📈Stocks"
#st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

#st.title(Title)


Input_stock=st.text_input("Input your Stock:")
#start=st.text_input("Start:")
#end=st.text_input("End:")
#history_months=st.number_input("Months:")
if Input_stock:

    #end= dt.datetime.today()
    #start= end + relativedelta(months=-6)
    stock= yf.Ticker(Input_stock)
    #Input_stock="aapl"
    #pdr.get_data_yahoo('aapl',start=start,end=end)
    #pdr.get_data_yahoo('AAPL', start="2017-08-13",end="2017-08-14")
    #st.write(pdr.get_data_yahoo("aapl",str(start),str(end)))
    #pdr.DataReader("AAPL", "yahoo", start="2017-08-13",end="2017-08-14")

    #st.write(stock.actions)
    #st.write(stock.info)
    #st.write(stock.news)
    #st.write(stock.shares)

    data=stock.history(period="max")
    #st.write(data)
    data["Dividend"]=stock.dividends
    data["Dividend"].fillna(0, inplace=True)  # fill empty to zero   
    data["50 moving avarege"]=data["Open"].rolling(window = 50, min_periods = 1).mean()
    data["150 moving avarege"]=data["Open"].rolling(window = 150, min_periods = 1).mean()
    data["200 moving avarege"]=data["Open"].rolling(window = 150, min_periods = 1).mean()

    tab1, tab2 = st.tabs(["Dividend", "History"])
    #fig = px.line(data,  y="Dividend", title='History ')
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
    
    
    #st.write(stock.get_shares_full(start="2022-01-01", end=None))

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
        
        
st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)

        

