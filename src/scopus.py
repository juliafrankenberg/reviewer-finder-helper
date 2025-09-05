import urllib.parse

def build_scopus_link(surname: str, firstname: str) -> str:
    """Helper for name-based Scopus search."""
    surname = surname.replace(" ", "+")
    firstname = firstname.replace(" ", "+")
    return (
        f"https://www.scopus.com/results/authorNamesList.uri?"
        f"name=name&st1={surname}&st2={firstname}&origin=searchauthorlookup"
    )


def build_scopus_email_link(email: str) -> str:
    """Helper for email-based Scopus search."""
    encoded_email = urllib.parse.quote(email)
    return (
        "https://www.scopus.com/results/results.uri?"
        f"st1={encoded_email}&st2=&s=ALL%28{encoded_email}%29"
        "&limit=10&origin=searchbasic&sort=plf-f&src=s&sot=b&sdt=b"
    )


def get_scopus_links(query: str):
    """
    Get Scopus search links for either:
    - Email → list with 1 link
    - Two-word name → list with 1 link
    - Multi-part name → dict with 2 labeled links
    """
    query = query.strip()

    if "@" in query:  # Email search
        return [build_scopus_email_link(query)]

    parts = query.split()

    if len(parts) == 2:  # Two-part name
        first, last = parts
        return [build_scopus_link(last, first)]

    elif len(parts) >= 3:  # Multi-part name
        firstname1 = parts[0]
        surname1 = " ".join(parts[1:])
        firstname2 = " ".join(parts[:2])
        surname2 = " ".join(parts[2:])
        return {
            "One First Name": build_scopus_link(surname1, firstname1),
            "Two First Names": build_scopus_link(surname2, firstname2),
        }

    else:
        raise ValueError("Input must be an email or at least two words for a name.")
