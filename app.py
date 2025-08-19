import streamlit as st
from src.scholar import google_scholar

st.title("Julia's Reviewer Finder Helper")

name = st.text_input("Enter Researcher Name:", "John Smith")

if st.button("Get Google Scholar Link"):
    link = google_scholar(name)
    st.markdown(f"🔗 [Click here to see the Google Scholar search for **{name}**]({link})")
