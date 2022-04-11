from turtle import onclick
import streamlit as st
import pandas as pd 
import numpy as np

st.title('In Class Streamlit Example!!')

if 'cnt' not in st.session_state:
    st.session_state.cnt = 0

def increment():
    if st.session_state.cnt >= 10:
       st.session_state.cnt = 0
    else: 
        st.session_state.cnt += 1

st.button('Click Here', on_click=increment())
st.write("Count: " + str(st.session_state.cnt))

st.title("Data Stuff")
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load(num_rows):
    data = pd.read_csv(DATA_URL, nrows=num_rows)
    return data

data_state = st.text("Loading...")
data = load(10000)
data_state.text("Done!")
st.write(data)