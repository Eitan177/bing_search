import streamlit as st
import streamlit.components.v1 as components
import os
import pyimgur
import pdb


st.set_page_config(layout="wide")


col1, col2 = st.beta_columns(2)


class similar:
    def __init__(self):
        run_again='init'
        st.title('similar image search with sp unknowns')

        col1, col2= st.beta_columns(2)

        with col1:
            video_file = open('streamlit-search-2021-08-03-10-08-47.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

        with col2:
            st.title('<-- Tutorial Video is on the left. The search, including the visual search box and the digital slides, is immediately below the video (scroll down to see)')
        if 'bingkey' not in st.session_state:
            st.session_state['bingkey'] = 0
        if 'googlekey' not in st.session_state:
            st.session_state['googlekey']=0
        if 'alkey' not in st.session_state:
            st.session_state['alkey']=0    
        bing_key=st.session_state['bingkey']
        google_key=st.session_state['googlekey']
        album_key=st.session_state['alkey']
        while bing_key>=0:   
            self.showbing(bing_key)
            bing_key-=1
        while google_key>=0:
            self.showgoog(google_key)
            google_key-=1
        while album_key>=0:
            self.showalbum(album_key)
            album_key-=1

    def showbing(self,key):
        col1, col2 = st.beta_columns(2)
        with col1:
                wuse1=st.slider(
                'left window width for row '+str(key),
                200, 2000,900, 100)
                huse1=st.slider(
                'left window height for row '+str(key),
                200, 2000,900, 100)
                components.iframe("https://www.bing.com/visualsearch/Microsoft/SimilarImages",width=wuse1, height=huse1)

        with col2:
                wuse2=st.slider(
                'right window width for row '+str(key),
                200, 2000,900, 100)
                huse2=st.slider(
                'right window height for row '+str(key),
                200, 2000,900, 100)
                components.iframe("https://digital.pathology.johnshopkins.edu/imageSets/451", width=wuse2,height=huse2)
        if key==0:
            st.title('Click Button Below to Add another row for searching bing')
            bing_row_add=st.button('add bing visual search row '+str(st.session_state['bingkey'])+' (DOUBLE CLICK THIS BUTTON)')
            if bing_row_add:
                st.session_state['bingkey']+=1
        return self

    def showgoog(self,key):
        client_id = "76cac0ffabcb911" # put your client ID here
        st.title('To add Keywords to the search we will use google visual search-')
        st.title('step 1) put in the path to the image (something like C:/Users/\{whateveryouridis\}/Downloads/\{nameoftheimage\}.png or the url of the image \(right click the image in the visual search result and copy image address\)')
        st.title('step 2) add key words in second column, click, and link will be created')
        col1, col2 = st.beta_columns(2)
        with col1:
            path=st.text_input('url or local path to your file # '+str(key),'')
            restrictpage=st.selectbox('see results from this site and file # '+str(key),['All sites','pathology.jhu.edu','webpathology.com','pathologyoutlines.com','shutterstock.com','medcell.med.yale.edu','histologyguide.com','radiopaedia.org'])
            if restrictpage == 'All sites':
                restrictpage=''
            else:
                restrictpage="+site:"+restrictpage

        with col2:
            words1=st.text_input('1) keyword image #'+str(key),'')
            if words1 !='':
                words1="+"+words1
            words2=st.text_input('2) keyword#'+str(key),'')
            if words2 !='':
                words2="+"+words2
            words3=st.text_input('3) keyword#'+str(key),'')
            if words3 !='':
                words3="+"+words3




        if path != '':
            if path[0:4]!='http':
                im = pyimgur.Imgur(client_id)
                
                uploaded_image = im.upload_image(path, title="Uploaded with PyImgur")
                st.header("https://www.google.com/searchbyimage?image_url="+uploaded_image.link+"&q="+words1+"+"+words2+"+"+words3)
            else:
                if restrictpage=='All sites':
                    st.header("https://www.google.com/searchbyimage?image_url="+path+"&q="+words1+words2+words3)
                else:
                    st.header("https://www.google.com/searchbyimage?image_url="+path+"&q="+words1+words2+words3+restrictpage)
            
        if key==0: 
            st.title('Click Button Below to Add another row for searching google')
            goog_row_add=st.button('add google visual search row' +str(st.session_state['googlekey'])+ ' (DOUBLE CLICK THIS BUTTON)')
            if goog_row_add:
                st.session_state['googlekey']+=1
                                 
        return self
    def showalbum(self,key):
        col1, col2 = st.beta_columns(2)
        with col1:
                wuse3=st.slider(
                'left albumizr window width for row '+str(key),
                200, 2000,900, 100)
                huse3=st.slider(
                'left albumizr window height for row '+str(key),
                200, 2000,900, 100)
                components.iframe("https://deadsimplechat.com/cHaKPZUFD",width=wuse3, height=huse3)

        with col2:
                wuse4=st.slider(
                'right albumizr window width for row '+str(key),
                200, 2000,900, 100)
                huse4=st.slider(
                'right albumizr window height for row '+str(key),
                200, 2000,900, 100)
                components.iframe("https://albumizr.com/", width=wuse4,height=huse4)
        if key==0:
            st.title('Click Button Below to Add another row for Viewing Social Media')
            album_row_add=st.button('add albumizr row '+str(st.session_state['alkey'])+' (DOUBLE CLICK THIS BUTTON)')
            if album_row_add:
                st.session_state['alkey']+=1
        <a href="https://twitter.com/intent/tweet?button_hashtag=TwitterDev&ref_src=twsrc%5Etfw" class="twitter-hashtag-button" data-show-count="false">Tweet #TwitterDev</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>        
        return self
     
showsim=similar()
