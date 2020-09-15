import streamlit as st
from requests_html import HTMLSession
session = HTMLSession()

import nltk
nltk.download('punkt')


#st.text_input()

st.write('https://www.tatielou.co.uk/pages/about-us')

url = "https://en.wikipedia.org/wiki/Michael_Jordan"

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

selector = "p"

with session.get(name) as r:
    paragraph = r.html.find(selector, first=False)
    text = " ".join([ p.text for p in paragraph])

#############################################

# temporary solution
#https://github.com/patil-suraj/question_generation/issues/22

st.write(text)

from pipelines import pipeline
nlp = pipeline("multitask-qa-qg")
faqs = nlp(text)

st.write(faqs)






