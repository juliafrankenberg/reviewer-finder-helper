import streamlit as st
import streamlit.components.v1 as components
from src.scholar import google_scholar
from src.pubmed import get_pubmed_link
from src.scopus import get_scopus_link_two_names
from src.scopus import get_scopus_link_multi_names

st.title("Julia's Reviewer Finder Helper")

st.markdown("This tool will perform the search on three platforms at the same time: Google Scholar, PubMed and Scopus.")
st.markdown("For Scopus users have to log-in beforehand.")
st.markdown("Note: Links should open automatically, but pop-ups might be blocked")



# Use a form to catch "Enter" as submission
with st.form(key="name_form"):
    author_name = st.text_input("Enter author name:", "Julia Frankenberg Garcia")
    submitted = st.form_submit_button("Search")

if submitted:
    # Generate links
    scholar_link = google_scholar(author_name)
    pubmed_link = get_pubmed_link(author_name)

    # Collect all links to open in new tabs
    all_links = [scholar_link, pubmed_link]

    parts = author_name.strip().split()
    if len(parts) == 2:
        scopus_link = get_scopus_link_two_names(author_name)
        all_links.append(scopus_link)
    elif len(parts) >= 3:
        scopus_links = get_scopus_link_multi_names(author_name)
        for link in scopus_links.values():
            all_links.append(link)

    # Display links in the app
    st.subheader(f"Links for: {author_name}")
    st.markdown(f"🔗 [Google Scholar]({scholar_link})")
    st.markdown(f"🔗 [PubMed]({pubmed_link})")
    if len(parts) == 2:
        st.markdown(f"🔗 [Scopus]({scopus_link})")
    else:
        for option, link in scopus_links.items():
            st.markdown(f"🔗 [Scopus]({link}) ({option})")

    # Automatically open all links in new tabs
    js_code = "".join([f'window.open("{link}", "_blank");\n' for link in all_links])
    components.html(f"<script>{js_code}</script>")
