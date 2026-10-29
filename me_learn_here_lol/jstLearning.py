import numpy as np
import matplotlib as plt
import streamlit as st
import pandas as pd
import plotly

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c'])

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

x = st.slider('x', min_value=0, max_value=1000)

st.text_input("Your name", key='name')

st.write(st.session_state.name)