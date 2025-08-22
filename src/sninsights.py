
import urllib.parse

def get_sn_insights_link(author_name: str) -> str:
    base_url = ("https://sn-insights.dimensions.ai/discover/publication"
                "?search_mode=content&search_text=researcher_name%3A(")
    query_name = urllib.parse.quote(author_name.strip())
    return f"{base_url}{query_name})&search_type=kws&search_field=full_search&order=date"
