import urllib.parse

def get_pubmed_link(query: str) -> str:
    """
    Return a PubMed search URL for the given query.
    Works for both author names and emails.
    """
    base_url = "https://pubmed.ncbi.nlm.nih.gov/?term="
    encoded_query = urllib.parse.quote(query.strip())
    return base_url + encoded_query
