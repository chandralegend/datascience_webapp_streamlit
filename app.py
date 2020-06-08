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
    lowercase = lambda x: str(x).lower().replace(" ","_")
    data.rename(lowercase, axis='columns', inplace = True)
    data.rename(columns = {
        'crash_date_crash_time' : 'date/time'
    }, inplace = True)
    # logging.info(str(data.columns))
    return data

data = load_data(10000)
# logging.info('Loaded the dataset successfully')

st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured",0,19)
st.map(data.query("number_of_persons_injured >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

st.header("How many collisions occur during a give time of the day?")
hour = st.slider("Hour to look at", 0, 23)
data = data[data['date/time'].dt.hour == hour]

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)