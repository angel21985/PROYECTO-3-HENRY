from unittest.case import _BaseTestCaseContext
from urllib import request
import streamlit as st
import pandas as pd
import numpy as np
import plost
import plotly.graph_objects as go
from datetime import datetime
from PIL import Image
import requests
import json

#configuración de la página
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Data
url = "https://ftx.us/api"
data = requests.get(url)

#línea A
a1, a2, a3 = st.columns(3)
with a1:
    markets = requests.get("https://ftx.us/api/markets").json()
    data = markets["result"]
    df =pd.DataFrame(data)
    st.dataframe(df)
with a2:
    a2.metric("ejemplo", "1", "1")
with a3:
    a3.metric("ejemplo", "1", "1")

#línea B
b1, b2, b3, b4 = st.columns(4)
b1.metric("ejemplo", "70 °F", "1.2 °F")
b2.metric("ejemplo", "9 mph", "-8%")
b3.metric("ejemplo", "86%", "4%")
b4.metric("ejemplo", "86%", "4%")

#línea C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Diagrama de Velas')
    markets = requests.get("https://ftx.us/api/markets").json()
    data = markets["result"]
    df = pd.DataFrame(data)
    pages = {
        "USD: page_usd"
        "ETH: page_eth"
    }
    option = st.selectbox(
    'Seleccionar Moneda',
    ('USD', "ETH"))

    st.write('You selected:', option)
def page_usd():
    monedas = requests.get(f'https://ftx.com/api/markets/{option}/USD/candles?resolution=3600&start_time=1609462800').json()
    df1 = pd.DataFrame(monedas["result"])
    fig = go.Figure(data=[go.Candlestick(x=df1["start_time"],
                open=df1['open'],
                high=df1['high'],
                low=df1['low'],
                close=df1['close'])])
    fig.show()
    
"""def page_eth():
    fig = go.Figure(data=[go.Candlestick(x=df["Date"],
                open="http://ftx.us/api/markets/ETH"['open'],
                high="http://ftx.us/api/markets/ETH"['high'],
                low="http://ftx.us/api/markets/ETH/USD"['low'],
                close="http://ftx.us/api/markets/ETH/USD"['close'])])

    fig.show()



with c2:
    st.markdown('### Diagrama Torta')
    plost.donut_chart(
        data="https://ftx.us/api/markets",
        theta='q2',
        color='company')"""