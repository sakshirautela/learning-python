import streamlit as st
st.title("Sakshi Rautela")
st.text('hello!')
st.selectbox("selecet ypur intreset",['movies','novels','drawing'])
st.radio('select',('Female','Male'))
st.checkbox('Male')
st.checkbox('Female')
SelectBox=st.selectbox("selecet ypur coures",['MCA','BCA','BA'])
if(SelectBox=='MCA'):
    st.write('Your course is Mca')
elif(SelectBox=='BCA'):
    st.write('Your course is BCA')
elif(SelectBox=='BA'):
    st.write('Your course is BA')
MulSecet=st.multiselect('Your skills',['java','python','c'])
st.write('your coureses ',MulSecet)
st.time_input('time')
st.date_input('date')