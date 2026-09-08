import streamlit as st
import pandas as pd
st.title('Machine Learning Model')
st.info('here we are going to find Penguin Species')
with st.expander('Penguine Table'):
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
with st.expander('Data Visualization'):
  #"island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex
  st.scatter_plot(data=df,x='bill_length_mm',y='body_mass_g',color='species')
  
