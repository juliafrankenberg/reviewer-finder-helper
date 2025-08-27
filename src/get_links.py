### test just to simplify getting links


from src.scholar import google_scholar
from src.pubmed import get_pubmed_link
from src.sninsights import get_sn_insights_link
from src.scopus import get_scopus_link_two_names, get_scopus_link_multi_names
import streamlit as st

def display_author_links(author_name: str):
    """
    Generates and displays all platform links for an author.
    Uses a Streamlit expander for neatness.
    """
    with st.expander(author_name):
        # Google Scholar
        st.markdown(f"🔗 [Google Scholar]({google_scholar(author_name)})")
        
        # PubMed
        st.markdown(f"🔗 [PubMed]({get_pubmed_link(author_name)})")
        
        # SN Insights
        st.markdown(f"🔗 [SN Insights]({get_sn_insights_link(author_name)})")
        
        # Scopus
        parts = author_name.strip().split()
        if len(parts) == 2:
            st.markdown(f"🔗 [Scopus]({get_scopus_link_two_names(author_name)})")
        elif len(parts) >= 3:
            sc_links = get_scopus_link_multi_names(author_name)
            for option, link in sc_links.items():
                st.markdown(f"🔗 [Scopus]({link}) ({option})")
