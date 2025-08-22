import streamlit as st
import streamlit.components.v1 as components
from src.scholar import google_scholar
from src.pubmed import get_pubmed_link
from src.scopus import get_scopus_link_two_names
from src.scopus import get_scopus_link_multi_names
from src.sninsights import get_sn_insights_link

st.title("Julia's Reviewer Finder Helper")

st.markdown("This tool will perform the search on 4 platforms at the same time: Google Scholar, PubMed, SN Insights and Scopus.")
st.markdown("For Scopus and SN Insights users have to log-in beforehand.")



# Use a form to catch "Enter" as submission
with st.form(key="name_form"):
    author_name = st.text_input("Enter author name:", "")
    submitted = st.form_submit_button("Search")

if submitted:
    # Generate links
    scholar_link = google_scholar(author_name)
    pubmed_link = get_pubmed_link(author_name)
    sninsights_link = get_sn_insights_link(author_name)


    parts = author_name.strip().split()
    if len(parts) == 2:
        scopus_link = get_scopus_link_two_names(author_name)
    elif len(parts) >= 3:
        scopus_links = get_scopus_link_multi_names(author_name)
        

    # Display links in the app
    st.subheader(f"Links for: {author_name}")
    st.markdown(f"🔗 [Google Scholar]({scholar_link})")
    st.markdown(f"🔗 [PubMed]({pubmed_link})")
    st.markdown(f"🔗 [SN Insights]({sninsights_link})")
    if len(parts) == 2:
        st.markdown(f"🔗 [Scopus]({scopus_link})")
    else:
        for option, link in scopus_links.items():
            st.markdown(f"🔗 [Scopus]({link}) ({option})")


