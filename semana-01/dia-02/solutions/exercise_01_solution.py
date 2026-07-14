"""Solution: First repeated customer."""


def first_repeated_customer_bruteforce(customer_ids: list[str]) -> str | None:
    """
    Educational brute-force version.
    """
    for index, customer_id in enumerate(customer_ids):
        if customer_id in customer_ids[:index]:
            return customer_id
    return None


def first_repeated_customer(customer_ids: list[str]) -> str | None:
    """
    Return the first customer ID that appears twice while scanning left to right, or None when every ID is unique.

    Complexity:
        Time O(n), space O(n).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    seen: set[str] = set()
    for customer_id in customer_ids:
        if customer_id in seen:
            return customer_id
        seen.add(customer_id)
    return None
