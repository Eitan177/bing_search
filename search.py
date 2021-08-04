import streamlit as st
import streamlit.components.v1 as components
import os
import pyimgur
st.set_page_config(layout="wide")
st.title('similar image search with sp unknowns')

col1, col2= st.beta_columns(2)

with col1:
    video_file = open('streamlit-search-2021-08-03-10-08-47.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

with col2:
    st.title('<-- Tutorial Video is on the left. The search, including the visual search box and the digital slides, is immediately below the video (scroll down to see)')

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


client_id = "76cac0ffabcb911" # put your client ID here
st.title('To add Keywords to the search we will use google visual search-')
st.title('step 1) put in the path to the image (something like C:/Users/\{whateveryouridis\}/Downloads/\{nameoftheimage\}.png or the url of the image \(right click the image in the visual search result and copy image address\)')
st.title('step 2) add key words in second column, click, and link will be created')
col1, col2 = st.beta_columns(2)
with col1:
    path=st.text_input('url or local path to your file','')
    ##PATH="file:///C:/Users/ehalper2/Downloads/8067.ndpi-[38151,40957,52981,55787]2x.png"
    

with col2:
    words1=st.text_input('1) keyword','')
    words2=st.text_input('2) keyword','')
    words3=st.text_input('3) keyword','')




if path != '':
    if path[0:4]!='http':
        im = pyimgur.Imgur(client_id)
        
        uploaded_image = im.upload_image(path, title="Uploaded with PyImgur")
        st.header("https://www.google.com/searchbyimage?image_url="+uploaded_image.link+"&q="+words1+"+"+words2+"+"+words3)
    else:
        st.header("https://www.google.com/searchbyimage?image_url="+path+"&q="+words1+"+"+words2+"+"+words3)
    
