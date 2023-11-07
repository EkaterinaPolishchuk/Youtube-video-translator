import streamlit as st
import assemblyai as aai
from api_secret import API_KEY_ASSEMBLYAI
from main import get_video_data

st.set_page_config(layout="wide")

aai.settings.api_key = API_KEY_ASSEMBLYAI

st.title("Youtube Video Translation")

video_data = get_video_data()
selected_video = st.selectbox(label="Select video", options=video_data.keys())

col1, col2, col3 = st.columns(3)
with col2:
    print(video_data[selected_video]["video_url"])
    st.video(video_data[selected_video]["video_url"])

transcriber = aai.Transcriber()

transcript = transcriber.transcribe(video_data[selected_video]["audio_url"])
st.text(transcript.text)