import streamlit as st
import streamlit.components.v1 as components
from src.scholar import google_scholar
from src.pubmed import get_pubmed_link
from src.scopus import get_scopus_link_two_names
from src.scopus import get_scopus_link_multi_names
from src.sninsights import get_sn_insights_link
from src.citation_search import pubmed_from_citation



st.title("Julia's Reviewer Finder Helper")

st.markdown("- This tool will perform the search on 4 platforms at the same time: Google Scholar, PubMed, SN Insights and Scopus.")
st.markdown("- For Scopus and SN Insights users have to log-in beforehand.")
st.markdown("""
- You can either:
    - search the author name
    - search several authors from a specific citation
""")

st.markdown("---")  # separator line
st.subheader("Search author by name:")

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
    st.markdown(f"<h5>Links for: {author_name}</h5>", unsafe_allow_html=True)
    st.markdown(f"🔗 [Google Scholar]({scholar_link})")
    st.markdown(f"🔗 [PubMed]({pubmed_link})")
    st.markdown(f"🔗 [SN Insights]({sninsights_link})")
    if len(parts) == 2:
        st.markdown(f"🔗 [Scopus]({scopus_link})")
    else:
        for option, link in scopus_links.items():
            st.markdown(f"🔗 [Scopus]({link}) ({option})")


# ------------ Citation Search ---------------- #

st.markdown("---")  # separator line
st.subheader("Search authors from citation:")

with st.form(key="citation_form"):
    citation_input = st.text_input("Paste **title** of cited manuscript:")
    citation_submitted = st.form_submit_button("Search")

if citation_submitted:
    with st.spinner("Searching PubMed..."):
        title, authors, pubmed_link, citation_string = pubmed_from_citation(citation_input)

    if not title:
        st.error("No PubMed record found for this citation.")
    else:
        #st.markdown(f"**Title:** {title}")
        st.markdown(f"**Manuscritp found:** {citation_string} [View on PubMed]({pubmed_link})")


        # ---------- Generate links for each author ----------
        for author in authors:
            with st.expander(author):
                # Google Scholar
                gs_link = google_scholar(author)
                st.markdown(f"🔗 [Google Scholar]({gs_link})")

                # PubMed
                pm_link = get_pubmed_link(author)
                st.markdown(f"🔗 [PubMed]({pm_link})")

                # SN Insights
                sn_link = get_sn_insights_link(author)
                st.markdown(f"🔗 [SN Insights]({sn_link})")

                # Scopus
                parts = author.strip().split()
                if len(parts) == 2:
                    sc_link = get_scopus_link_two_names(author)
                    st.markdown(f"🔗 [Scopus]({sc_link})")
                elif len(parts) >= 3:
                    sc_links = get_scopus_link_multi_names(author)
                    for option, link in sc_links.items():
                        st.markdown(f"🔗 [Scopus]({link}) ({option})")
