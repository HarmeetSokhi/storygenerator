import streamlit as st
from pydub import AudioSegment
import tempfile
import os
from createstory import create_story_from_image 

def main():
    st.set_page_config(page_title="Convert drawing to a story and play it", layout="wide")
    st.title("Convert Kids drawing in a story")
    # Upload image file
    image_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

    if image_file is not None:
    # Display the uploaded photo
        col1, col2, col3 = st.columns([0.3,0.4,0.3])

        with col1:
            st.header("Drawing")
            st.image(image_file, caption="Uploaded Photo", use_column_width=True)
        file_path = get_file_path(image_file)  
        #Process the image and generate audio
        with col2:
            with st.spinner(text="Working on story..."):
                print("create_story")
                audio =  create_story_from_image(file_path,st,col1,col2,col3)

def get_file_path(file_uploader):
    """Get the complete file path from the file uploader"""
    with open(file_uploader.name, "wb") as file:
        file.write(file_uploader.getbuffer())
    return os.path.abspath(file.name)

if __name__ == '__main__':
    main()
