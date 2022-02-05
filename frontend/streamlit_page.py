import streamlit as st
import pandas as pd
import numpy as np

from pearl.preprocessing.base.normalize import Uniform

st.title('Do a simple Machine Learning')


st.subheader('Load your csv dataset')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df.head(10))

st.subheader("Summary:")
# st.write(df.describe())
# st.write(df.)
#st.checkbox('xcövxmövmcö')
#if st.button('Say hello, Ege'):
#    st.subheader('')
"""
---
"""


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data
data_load_state = st.text('Loading..')

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)

# Notify the reader that the data was successfully loaded
data_load_state.text('Done! (using st.cache)')


# st.subheader('Raw data')
# st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# st.subheader('Map of all pickups')
# st.map(data)

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
