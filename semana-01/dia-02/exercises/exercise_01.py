"""Exercise: First repeated customer."""


def first_repeated_customer(customer_ids: list[str]) -> str | None:
    """
    Return the first customer ID that appears twice while scanning left to right, or None when every ID is unique.

    Args:
    customer_ids: Ordered customer identifiers.

    Returns:
        Repeated customer ID or None.

    Examples:
        Review the test file for representative cases.

    Restrictions:
        Prefer clean interview-ready Python 3.12.

    Edge cases:
        Empty inputs, one-element inputs, duplicates, and basic large cases.

    Target complexity:
        Time O(n), space O(n).

    Interviewer questions:
        What assumptions are you making about the input?
        Can you describe a brute-force alternative first?
    """

    ids = set()
    repeatedID = None
    for id in customer_ids:
        if id in ids:
            repeatedID = id
        else:
            ids.add(id)

    return repeatedID

    # TODO: Implement the solution.
    raise NotImplementedError
