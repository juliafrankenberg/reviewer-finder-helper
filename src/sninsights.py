
import urllib.parse

def get_sn_insights_link(author_name: str) -> str:
    query_name = urllib.parse.quote(author_name)
    return (
        f"https://sn-insights.dimensions.ai/analytics/publication/author/aggregated?search_mode=content&search_text=researcher_name%3A({query_name})%0A&search_type=kws&search_field=full_search&order=date"
    )


