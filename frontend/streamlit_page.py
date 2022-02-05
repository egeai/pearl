import streamlit as st
import pandas as pd
import numpy as np
from streamlit_manager import *

from PIL import Image
image = Image.open('/Users/bertan/development/MachineLearningProjects/ege/pearl/frontend/hill.jpeg')
st.image(image, caption='Sunrise by the mountains')

st.header('A step by step simple Machine Learning')
st.subheader('1. Load your dataset')

"""
 Please upload a CSV file *
"""
# Upload csv file
uploaded_file = st.file_uploader("Choose a file")
sp = StreamlitPreparation()
if uploaded_file is not None:
    df = sp.load_data(uploaded_file)
    st.write(df.head(10))

    if st.checkbox('Uniform column names'):
        sp.uniform_column_names().head()

    if st.checkbox('Uniform categorical columns'):
        sp.uniform_categorical_columns().head()

    if st.button('Show preprocessed dataframe'):
        st.write(sp.get_uniformed_df())

    # df = pd.read_csv(uploaded_file)
    # un = Uniform(df)
    #uniformed = un.uniform_column_names()
    #st.write(uniformed.head(10))

# st.subheader("Summary:")
# st.write(df.describe())
# st.write(df.)
# st.checkbox('xcövxmövmcö')
# if st.button('Say hello, Ege'):
#    st.subheader('')



