# one last name
def get_scopus_link_two_names(full_name: str) -> str:
    """
    Returns a single Scopus link for a two-word name (First Last)
    """
    parts = full_name.strip().split()
    if len(parts) != 2:
        raise ValueError("Name must have exactly two words for this function.")
    first, last = parts
    return build_scopus_link(last, first)


# multiple last names
def get_scopus_link_multi_names(full_name: str) -> dict:
    """
    Returns two Scopus link options for names with 3+ words
    """
    parts = full_name.strip().split()
    if len(parts) < 3:
        raise ValueError("Name must have at least three words for this function.")

    # Option 1: last word is surname
    surname1 = parts[-1]
    firstname1 = " ".join(parts[:-1])

    # Option 2: last two words are surname
    surname2 = " ".join(parts[-2:])
    firstname2 = " ".join(parts[:-2])

    return {
        "Surname is Last Name only": build_scopus_link(surname1, firstname1),
        "Surname are Multiple Names": build_scopus_link(surname2, firstname2),
    }


# helper function used by both
def build_scopus_link(surname: str, firstname: str) -> str:
    surname = surname.replace(" ", "+")
    firstname = firstname.replace(" ", "+")
    return (
        f"https://www.scopus.com/results/authorNamesList.uri?"
        f"name=name&st1={surname}&st2={firstname}&origin=searchauthorlookup"
    )
