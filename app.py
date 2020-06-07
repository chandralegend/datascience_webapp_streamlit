import streamlit as st
import pandas as pd
import numpy as np
import logging

DATA_URL = ("Motor_Vehicle_Collisions_-_Crashes.csv")
# DATA_URL = ("https://data.cityofnewyork.us/resource/h9gi-nx95.csv")

st.title("Motor Vehicle Collision in New York City")
st.markdown("This application is a streamlit dashboard use to analyze motor vehicle collision in NYC")

@st.cache(persist= True)
def load_data(n_rows):
    data = pd.read_csv(DATA_URL, nrows= n_rows, parse_dates=[['CRASH DATE', 'CRASH TIME']])
    data.dropna(subset = ['LATITUDE', 'LONGITUDE'], inplace = True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace = True)
    data.rename(columns = {
        'crash date_crash time' : 'date/time'
    }, inplace = True)
    return data

data = load_data(100000)
logging.info('Loaded the dataset successfully')

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)