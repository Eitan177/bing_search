import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")
st.title('similar image search with sp unknowns and microsoft')

col1, col2= st.beta_columns(2)

with col1:
    video_file = open('streamlit-search-2021-08-03-10-08-47.webm', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
col1, col2 = st.beta_columns(2)



with col1:
    wuse1=st.slider(
    'left window width',
    200, 2000,900, 100)
    components.iframe("https://www.bing.com/visualsearch/Microsoft/SimilarImages",width=wuse1, height=1000)

with col2:
    wuse2=st.slider(
    'right window width',
    200, 2000,900, 100)
    components.iframe("https://digital.pathology.johnshopkins.edu/imageSets/451", width=wuse2,height=1000)

