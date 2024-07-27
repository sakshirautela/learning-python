import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

chart_data=pd.DataFrame(np.random.rand(20,3))
st.header('Line Graph')
st.line_chart(chart_data)
st.header('Area Chart')
st.area_chart(chart_data)
st.header('Bar Graph')
st.bar_chart(chart_data)


df=pd.read_csv('iris.csv')
st.dataframe(df)
st.header('data Visulaization using the matplotlib')
fig=plt.figure(figsize=(15,10))
df['Species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.header('distributed data Visulaization using the Seaborn library')
fig=plt.figure(figsize=(15,8))
sns.histplot(df['Sepal.Length'])
st.pyplot(fig)

st.header("Scatter plot")
fig,ax=plt.subplots(figsize=(15,5))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.header("count plot")
fig=plt.figure(figsize=(15,5))
sns.countplot(data=df,x='Species')
st.pyplot(fig)

st.header("Box plot")
fig=plt.figure(figsize=(15,5))
sns.boxplot(data=df,x='Species',y='Petal.Length')
st.pyplot(fig)


