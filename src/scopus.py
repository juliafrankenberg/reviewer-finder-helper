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
    For names with 3+ parts, return two Scopus search links:
    - Option 1: first word = first name, rest = surname(s)
    - Option 2: first two words = first name(s), rest = surname(s)
    """
    parts = full_name.strip().split()

    if len(parts) < 3:
        raise ValueError("Name must have at least three words for this function.")

    # Option 1: first word = first name
    firstname1 = parts[0]
    surname1 = " ".join(parts[1:])

     # Option 2: first two words = first names
    firstname2 = " ".join(parts[:2])
    surname2 = " ".join(parts[2:])


    return {
        "One First Name": build_scopus_link(surname1, firstname1),
        "Two First Names": build_scopus_link(surname2, firstname2),
    }


# helper function used by both
def build_scopus_link(surname: str, firstname: str) -> str:
    surname = surname.replace(" ", "+")
    firstname = firstname.replace(" ", "+")
    return (
        f"https://www.scopus.com/results/authorNamesList.uri?"
        f"name=name&st1={surname}&st2={firstname}&origin=searchauthorlookup"
    )
