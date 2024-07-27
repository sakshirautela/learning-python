import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.figure_factory as pf 

st.header('1. Altair scatter plot')
data=pd.DataFrame(np.random.rand(300,5),columns=['a','b','c','d','e'])
chart=alt.Chart(data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

st.header('2. Interactive Chart')
st.subheader('2.1 Line Chart')
data=pd.read_csv('lang_data.csv')
courese_list=data.columns.tolist()
choose_lang=st.multiselect('choose courses',courese_list)
new_df=data[choose_lang]
st.line_chart(new_df)
st.subheader('2.2 Area Chart')
st.area_chart(new_df)

st.header('Data visulalization using plotly')
df=pd.read_csv('tips.csv')
st.dataframe(df)
st.subheader('Pie Chart')
fig=px.pie(df,values='total_bill',names='day')
st.plotly_chart(fig)


st.subheader('Histogram Chart')
x1=np.random.randn(200)
x2=np.random.randn(200)
x3=np.random.randn(200)
hist_data=[x1,x2,x3]
gorop_label=['g1','g2','g3']
fig=pf.create_distplot(hist_data,gorop_label)
st.plotly_chart(fig)