import requests
import xml.etree.ElementTree as ET

def pubmed_from_citation(citation: str):
    # 1. Search for citation
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "retmode": "json", "term": citation}
    r = requests.get(search_url, params=params)
    r.raise_for_status()
    result = r.json()

    if not result["esearchresult"]["idlist"]:
        return None, None

    pmid = result["esearchresult"]["idlist"][0]

    # 2. Fetch article metadata
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": pmid, "retmode": "xml"}
    r = requests.get(fetch_url, params=params)
    r.raise_for_status()

    root = ET.fromstring(r.text)

    # 3. Extract title
    title = root.findtext(".//ArticleTitle")

    # 4. Extract authors
    authors = []
    for author in root.findall(".//Author"):
        last = author.findtext("LastName")
        first = author.findtext("ForeName")
        if last and first:
            authors.append(f"{first} {last}")

    journal = root.findtext(".//Journal/Title")
    year = root.findtext(".//PubDate/Year")
    volume = root.findtext(".//JournalIssue/Volume")
    issue = root.findtext(".//JournalIssue/Issue")
    pages = root.findtext(".//MedlinePgn")

    # Construct citation string
    citation_string = ""
    if title:
        citation_string += f"{title} "
    if journal:
        citation_string += f"{journal} "
    if year:
        citation_string += f"{year};"
    if volume:
        citation_string += f"{volume}"
        if issue:
            citation_string += f"({issue})"
        citation_string += ":"
    if pages:
        citation_string += f"{pages}."

    # PubMed link
    pubmed_link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

    return title, authors, pubmed_link, citation_string
