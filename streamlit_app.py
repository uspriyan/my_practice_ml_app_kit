import streamlit as st
import pandas as pd
st.title('Machine Learning Model')
st.info('here we are going to find Penguin Species')
with st.expander('Penguine Table'):
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  st.write('X-value')
  x=df.drop('species',axis=1)
  x
  st.write('Y-value')
  y=df[['species']]
  y
  
  
with st.expander('Data Visualization'):
  st.info('Graph between Length of Penguin VS Body Mass of Penguine')
  #"island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')
  
