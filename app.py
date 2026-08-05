# create virtual environment
# windows
# python -m venv venv 
# venv\Scripts\activate
# install streamlit 
# pip install streamlit 
# pip show streamlit
# pip install scikit-learn
# pip show scikit-learn
# pip install seaborn 
# pip show seaborn
# pip install matplotlib
# pip show matplotlib

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# --------------------------------------------------------------
# load model
model = pickle.load(open('svm.pkl','rb'))

# Give title for application
st.title("Insurance Price Prediction App")

# How to take input from users
age = st.number_input('Age',min_value=18 , max_value= 100 , value=25)
bmi = st.number_input('BMI',min_value=30 , max_value= 80 , value=40)
gender = st.selectbox('Gender',('male','female'))
smoker = st.selectbox('Smoker',('yes' ,'no'))
region = st.selectbox('Region',('southwest', 'southeast' ,'northwest', 'northeast'))
children = st.number_input('Children',min_value=0 , max_value= 6 , value=2)

# convert categories back to numbers
# refer to encoding
# smoker : label encoder
# yes:1 , no 0
Smoker = 1 if smoker=='yes' else 0

# gender : one hot encoding
sex_female = 1 if gender=='female' else 0
sex_male = 1 if gender=='male' else 0

# region : Target encoder
# 'northwest':0,'southwest':1,'northeast':2,'southeast':3
region_dict = {'northwest':0,'southwest':1,'northeast':2,'southeast':3}
Region = region_dict[region]

# create dataframe
data = pd.DataFrame({
    'age':[age], 'bmi':[bmi],'children':[children],
    'Smoker':[Smoker],'sex_female':[sex_female],'sex_male':[sex_male],
    'Region':[Region]})

# Scaling
sc = MinMaxScaler()
data[['age','bmi']]= sc.fit_transform(data[['age','bmi']])

# Predictions
if st.button('Predict'):
  prediction = model.predict(data)
  output = round(np.exp(prediction[0]),2)
  st.success(f'Price predictions: ${output}')

# run app
# streamlit run app.py