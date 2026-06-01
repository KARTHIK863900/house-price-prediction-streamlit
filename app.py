import streamlit as st
import pandas as pd
from pickle import load
st.write('Regression Model')
st.write('How much House-Price')
def get_input():
    bul=st.sidebar.number_input('Enter the Buliding type',min_value=1,max_value=2)
    yy=st.sidebar.number_input('Enter the year of sale',min_value=2000,max_value=2025)
    mm=st.sidebar.slider('Enter the month of sale',min_value=1,max_value=12)
    typp=st.sidebar.selectbox('Enter the type of property',['House','Apartment'])
    pp=st.sidebar.number_input('Enter the property')
    Area=st.sidebar.number_input('Enter the area in ft')
    status=st.sidebar.selectbox('status',['Available','sold'])
    if typp=='House':
       typp=0
    else:
        typp=1
    if status=='Available':
        status=1
    else:
        status=0
    user_input=pd.DataFrame({
        'Building Type':bul,
        'Year of sale':yy,
        'Month of sale':mm,
        'Type of property':typp,
        'Property #':pp,
        'Area (ft.)':Area,
        'Status':status},index=[1])
    return user_input
features=get_input()
loaded_model=load(open('lreg.pkl','rb'))
if st.sidebar.button('Submit'):
    st.write(features)
    res=loaded_model.predict(features)
    st.success(f"The House Price is:{res[0]:,.2f}")


