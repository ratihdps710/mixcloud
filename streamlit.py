import streamlit as st
import requests

# Function to upload MP3 file to Mixcloud
def upload_to_mixcloud(mp3_file, title, access_token):
    with open(mp3_file, 'rb') as f:
        files = {
            'mp3': f,
        }
        data = {
            'name': title,
        }
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        r = requests.post('https://api.mixcloud.com/upload/', headers=headers, files=files, data=data)
        return r.json()

# Streamlit UI
st.title('Mixcloud MP3 Upload')

# Input for Access Token
access_token = st.text_input('Enter your Mixcloud Access Token:', type="password")

# Upload MP3 File
uploaded_file = st.file_uploader("Choose an MP3 file", type="mp3")

# Input for Title
title = st.text_input('Enter the title of the episode')

# Button to trigger upload
if st.button('Upload'):
    if uploaded_file and title and access_token:
        # Save the uploaded file to a temporary location
        with open('temp_episode.mp3', 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        # Call the function to upload the file
        result = upload_to_mixcloud('temp_episode.mp3', title, access_token)
        
        # Display result
        st.write(result)
    else:
        st.error('Please make sure all fields are filled!')
