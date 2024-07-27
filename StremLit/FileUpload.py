import streamlit as st
st.file_uploader('upload file',type=['pdf','docs'])

st.header("Working with Images")
img=st.file_uploader('uploade img',type=['png','jpef'])
if img is not None:
    st.image(img)
st.header("Working with viedo")
viedo=st.file_uploader('uploade img',type=['mp4'])
if viedo is not None:
    st.video(viedo,start_time=5)

st.header("Working with Audio")
audio=st.file_uploader('uploade img',type=['mp3'])
if audio is not None:
    st.audio(audio.read())