import streamlit as st
import streamlit.components.v1 as components
from src.scholar import google_scholar
from src.pubmed import get_pubmed_link
from src.scopus import get_scopus_links  
from src.sninsights import get_sn_insights_link
from src.citation_search import pubmed_from_citation


st.title("Reviewer Finder Helper")

st.markdown("This tool will help you search for reviewer/researcher information on multiple platforms at the same time. At the moment the platforms are: Google Scholar, PubMed, SN Insights and Scopus.")
st.markdown("- For Scopus and SN Insights users have to log-in beforehand.")
st.markdown("""
- You can either:
    - search the potential reviewer by name/e-mail
    - search several potential reviewers from a specific citation (e.g. when trying to find reviewers from a manuscript's citations)
""")

st.markdown("---")  # separator line
st.subheader("Search reviewer by name/e-mail:")
st.markdown("Choosing name vs e-mail can return different results. Generally for established researchers using the name should work better, but for researchers with common names the e-mail can help differentiate them from others. Feel free to try both!")  


# Use a form to catch "Enter" as submission
with st.form(key="name_form"):
    author_name = st.text_input("Enter reviewer name or email:", "")
    submitted = st.form_submit_button("Search")

if submitted:
    # Generate links
    scholar_link = google_scholar(author_name)
    pubmed_link = get_pubmed_link(author_name)
    sninsights_link = get_sn_insights_link(author_name)
    scopus_links = get_scopus_links(author_name)  

    # Display links in the app
    st.markdown(f"<h5>Links for: {author_name}</h5>", unsafe_allow_html=True)
    st.markdown(f"🔗 [Google Scholar]({scholar_link})")
    st.markdown(f"🔗 [PubMed]({pubmed_link})")
    st.markdown(f"🔗 [SN Insights]({sninsights_link})")

    # If dict (multi-part case): show with labels
    if isinstance(scopus_links, dict):
        for label, link in scopus_links.items():
            st.markdown(f"🔗 [Scopus]({link}) ({label})")
    # If list (email or two-part name): show without labels
    else:
        for link in scopus_links:
            st.markdown(f"🔗 [Scopus]({link})")

# ------------ Citation Search ---------------- #

st.markdown("---")  # separator line
st.subheader("Search reviewers from citation:")
st.markdown("This will return a search by the **name** of the authors only (not e-mails)")

with st.form(key="citation_form"):
    citation_input = st.text_input("Paste **title** of cited manuscript:")
    citation_submitted = st.form_submit_button("Search")

if citation_submitted:
    with st.spinner("Searching PubMed..."):
        title, authors, pubmed_link, citation_string = pubmed_from_citation(citation_input)

    if not title:
        st.error("No PubMed record found for this citation.")
    else:
        st.markdown(
            f"**Manuscript found:**\n\n"
            f"{citation_string} [View on PubMed]({pubmed_link})"
        )

        # ---------- Generate links for each author ----------
        for author in authors:
            with st.expander(author):
                st.markdown(f"🔗 [Google Scholar]({google_scholar(author)})")
                st.markdown(f"🔗 [PubMed]({get_pubmed_link(author)})")
                st.markdown(f"🔗 [SN Insights]({get_sn_insights_link(author)})")

                scopus_links = get_scopus_links(author)
                # If dict (multi-part case): show with labels
                if isinstance(scopus_links, dict):
                    for label, link in scopus_links.items():
                        st.markdown(f"🔗 [Scopus]({link}) ({label})")
                # If list (email or two-part name): show without labels
                else:
                    for link in scopus_links:
                        st.markdown(f"🔗 [Scopus]({link})")


st.markdown("Developed by Julia Frankenberg Garcia. Feedback or suggestions are always welcome!")
