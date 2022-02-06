import streamlit as st
import pandas as pd
import numpy as np
from streamlit_manager import *

from PIL import Image
image = Image.open('/Users/bertan/development/MachineLearningProjects/ege/pearl/frontend/hill.jpeg')
st.image(image, caption='Sunrise by the mountains')

st.header('A step by step simple Machine Learning')
st.subheader('1. Load your dataset')

st.write("###### a. Upload a CSV file *")

# Upload csv file
uploaded_file = st.file_uploader("Choose a file")
sp = StreamlitPreparation()
if uploaded_file is not None:
    df = sp.load_data(uploaded_file)
    st.write(df.head(10))
    st.write("###### b. Shape of the data(rows, columns)")
    st.write(sp.shape_of_df())
    st.write("###### Question 1:")
    target_variable = st.radio(
        "What's the target variable of the dataset?",
        (sp.columns()))


    # st.write("###### c. Shape of the data(rows, columns)")
    # st.write(sp.shape_of_df())

    st.subheader('2. Explore and clean the data')
    st.subheader('3. Split the data into train/validation/test')
    st.subheader('4. Fit an initial model and evaluate')
    st.subheader('5. Tune hyperparameters')
    st.subheader('6. Evaluate on the validation set')
    st.subheader('7. Final model selection and evaluation')

    # Machine learning is used to examine past data to predict future outcomes.

    # What is Feature Engineering?
    # Feature engineering is the process of transforming raw data into features
    # that better represent the underlying signal to be fed to a machine learning
    # model, resulting in improved model accuracy on unseen data.

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



