"""Solution: Count unique values."""


def count_unique_values_bruteforce(values: list[int]) -> int:
    """
    Educational brute-force version.
    """
    seen = []
    for value in values:
        if value not in seen:
            seen.append(value)
    return len(seen)


def count_unique_values(values: list[int]) -> int:
    """
    Return the number of distinct values.

    Complexity:
        Time O(n), space O(n).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    return len(set(values))
