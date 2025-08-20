def get_pubmed_link(author_name: str) -> str:
    """
    Return a PubMed search URL for the given author name.
    """
    base_url = "https://pubmed.ncbi.nlm.nih.gov/?term="
    query = "+".join(author_name.strip().split())
    return base_url + query