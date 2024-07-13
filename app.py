# import library
import streamlit as st
import pandas as pd
import numpy as np

# menulis title
st.write("Here's our first attempt at using data to create a table: SIC batch 5")

# menulis dataframe
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# menulis dataframe
st.write("menulis dataframe menggunakan st.dataframe")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# menulis dataframe pakai styler
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# membuat chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# membuat peta
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# membuat slider
x = st.slider('this is variable x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# membuat input nama
st.text_input("Masukan nama anda", key="name")

# You can access the value at any point with:
st.session_state.name

# create checkox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
# create selectbox
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option