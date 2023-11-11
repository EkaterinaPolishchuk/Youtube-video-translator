import json
import streamlit as st
import assemblyai as aai
from translate_text import get_translation
from api_secret import API_KEY_ASSEMBLYAI

st.set_page_config(layout="wide")

aai.settings.api_key = API_KEY_ASSEMBLYAI

st.title("Youtube Video Translation")

with open("video_info.json", "r", encoding='UTF-8') as file_object:
    videos_data = json.loads(file_object.read())
file_object.close()

languages = {
        "English": "en",
        "German": "de",
        "Ukrainian": "uk",
        "Russian": "ru",
        "Spanish": "sp",
        "Portuguese": "pt", 
        "Chinese": "zh",

}

col1, col2 = st.columns([2, 1])

with col1:
    selected_video = st.selectbox(label="Select the title of the video whose text you would like to translate",
                                options=videos_data.keys(),
                                placeholder="Choose a video",
                                index=None)

with col2:
    selected_language = st.selectbox(label="Translate to...",
                                options=languages.keys(),
                                placeholder="Choose a language",
                                index=None)

if selected_video and selected_language:
    transcriber = aai.Transcriber()

    with st.spinner('Wait for it...'):
        FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
        transcript = transcriber.transcribe(videos_data[selected_video]["audio_url"])
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown(selected_video)
        st.video(videos_data[selected_video]["video_url"])

    if transcript.error is None:
        col1, col2 = st.columns(2)
        with col1:
            original_text = st.text_area("Original text", transcript.text, height=500)
        with col2:
            if original_text is not None:
                translated_text = get_translation(original_text, languages[selected_language])
                final_translated_text = st.text_area("Translation", translated_text, height=500)
    else:
        st.warning("Error")
