
# src/scholar.py

import urllib.parse

def google_scholar(query: str) -> str:
    """
    Return a Google Scholar search URL for the given query.
    Works for both author names and emails.
    """
    base_url = "https://scholar.google.com/scholar?q="
    encoded_query = urllib.parse.quote(query.strip())  # safely encode spaces, @, etc.
    return base_url + encoded_query





    