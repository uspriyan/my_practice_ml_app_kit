import streamlit as st
import pandas as pd
st.title('Machine Learning Model')
st.info('here we are going to find Penguin Species')
df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
x=df.drop('species',axis=1)
y_raw=df[['species']]
dummy_df1=pd.get_dummies(df)
with st.expander('Penguine Table'):
  df
  st.write('X-value')
  x
  st.write('Y-value')
  y_raw
  #encode
  dummy_df1[:1]
with st.expander('Data Visualization'):
  st.info('Graph between Length of Penguin VS Body Mass of Penguine')
  #"island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')
with st.sidebar:
  st.header('Modifications')
  Species=st.selectbox('Species',('Adelie','Gentoo','Chinstrap'))
  island=st.selectbox('Island',('Torgersen','Dream','Biscoe'))
  #Torgersen Dream Biscoe
  bill_depth_mm=st.slider('bill_depth_mm',3.4,11.2)
  bill_weight_g=st.slider('bill_weight_g',4.5,10.3)
  gender=st.selectbox('gender',('Male','Female'))
with st.expander('My_table'):
  data={
   'island': island,            
    'bill_length_mm': 43.9,     
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': 201.0,  # Added: Missing column (you can replace with a slider variable)
    'body_mass_g': bill_weight_g,# Matches column location
    'sex': gender
  }
  new_df1=pd.DataFrame(data,index=[0])
  st.write('##Input row')
  new_df1
  st.write('Combined Table')
  my_table=pd.concat([new_df1,x],axis=0,ignore_index=True)
  my_table
