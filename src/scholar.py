
# src/scholar.py

def google_scholar(author_name: str) -> str:
   
    """
    Return a Google Scholar search URL for the given author name.
    """
    base_url = "https://scholar.google.com/scholar?q="
    query = "+".join(author_name.strip().split())
    return base_url + query





    