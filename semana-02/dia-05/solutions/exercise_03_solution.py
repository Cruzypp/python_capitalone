"""Solution: Sum values seen once."""


def sum_values_seen_once_bruteforce(values: list[int]) -> int:
    """
    Educational brute-force version.
    """
    result = 0
    for value in values:
        if values.count(value) == 1:
            result += value
    return result


def sum_values_seen_once(values: list[int]) -> int:
    """
    Return the sum of values that appear exactly once.

    Complexity:
        Time O(n), space O(n).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    counts: dict[int, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return sum(value for value, count in counts.items() if count == 1)
