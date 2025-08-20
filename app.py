import streamlit as st
from src.scholar import google_scholar
from src.pubmed import get_pubmed_link
from src.scopus import get_scopus_link_two_names
from src.scopus import get_scopus_link_multi_names


st.title("Julia's Reviewer Finder Helper")

# Use a form to catch "Enter" as submission
with st.form(key="name_form"):
    author_name = st.text_input("Enter author name:", "Julia Frankenberg Garcia")
    submitted = st.form_submit_button("Search")

if submitted:
    # Generate links
    scholar_link = google_scholar(author_name)
    pubmed_link = get_pubmed_link(author_name)

    # Display links individually
    st.subheader(f"Links for: {author_name}")
    st.markdown(f"🔗 [Google Scholar]({scholar_link})")
    st.markdown(f"🔗 [PubMed]({pubmed_link})")
    #st.markdown(f"🔗 [Scopus]({scopus_link})")
    parts = author_name.strip().split()

    if len(parts) == 2:
        scopus_link = get_scopus_link_two_names(author_name)
        st.markdown(f"🔗 [Scopus]({scopus_link})")
    elif len(parts) >= 3:
        scopus_links = get_scopus_link_multi_names(author_name)
        for option, link in scopus_links.items():
            st.markdown(f"🔗 [Scopus]({link}) ({option})")
