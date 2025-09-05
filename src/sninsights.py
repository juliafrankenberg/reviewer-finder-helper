import urllib.parse

def get_sn_insights_link(query: str) -> str:
    """
    Return an SN Insights search URL for either an author name or email.
    - If input contains '@' → search by email
    - Else → search by researcher name
    """
    encoded_query = urllib.parse.quote(query.strip())

    base_url = "https://sn-insights.dimensions.ai/analytics/publication/author/aggregated?search_mode=content&order=date"

    if "@" in query:
        # Email search
        return f"{base_url}&search_text={encoded_query}&search_type=kws&search_field=full_search"
    else:
        # Name search
        return f"{base_url}&search_text=researcher_name%3A({encoded_query})&search_type=kws&search_field=full_search"
