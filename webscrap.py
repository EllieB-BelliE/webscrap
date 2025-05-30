#to run in cmd streamlit run webscrap.py

import requests
from bs4 import BeautifulSoup
import streamlit as st

def render():
    results = fetch_page()
    st.title("Wiki Find!")
    st.badge(str(results['status']),icon=":material/network_ping:",color="green")
    st.markdown(results['url'])
    st.subheader(results['content'])

def fetch_page():
    webpage = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(webpage.content, "html.parser")
    soup_page = soup.find("p")
    return {"status": webpage.status_code, "url": webpage.url, "content": soup_page.text}


render()


