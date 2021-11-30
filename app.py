import streamlit as st
import pandas as pd

st.write('# Hello World!')
st.write('## A subtitle')

#df = pd.read_csv('data/Austin_Animal_Center_Intakes_061521_with_location_details.csv')

animal_type = st.sidebar.radio(
    label='Choose your animal type',
    options=['Dog', 'Cat']
)

st.write(animal_type)