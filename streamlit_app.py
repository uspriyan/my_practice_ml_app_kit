import streamlit as st
import pandas as pd
st.title('Machine Learning Model')
st.info('here we are going to find Penguin Species')
with st.expander('Penguine Table'):
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
