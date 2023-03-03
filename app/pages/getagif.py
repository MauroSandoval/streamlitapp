import streamlit as st
import requests

api_key = st.secrets.api_key
st.markdown('## Please, ask for the funniest gif below')

st.text(st.secrets.some_magic_api.key)

prompt = st.text_input('Enter the topic for your gif')
url = 'https://api.giphy.com/v1/gifs/search'
params ={'api_key':api_key, 'q':prompt, 'limit':4}
response = requests.get(url, params=params).json()

while not prompt:
    st.stop()
    
st.markdown('### ENJOY your Gif-T')

st.markdown(
    f'<iframe src="{response["data"][0]["embed_url"]}" width="480" height="359" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    unsafe_allow_html=True
)

st.markdown(
    f'<iframe src="{response["data"][1]["embed_url"]}" width="480" height="359" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    unsafe_allow_html=True
)

st.markdown(
    f'<iframe src="{response["data"][2]["embed_url"]}" width="480" height="359" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    unsafe_allow_html=True
)
