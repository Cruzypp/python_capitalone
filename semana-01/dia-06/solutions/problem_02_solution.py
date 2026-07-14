"""Solution: First index of max."""


def first_index_of_max_bruteforce(values: list[int]) -> int:
    """
    Educational brute-force version.
    """
    if not values:
        return -1
    best_index = 0
    for index in range(1, len(values)):
        if values[index] > values[best_index]:
            best_index = index
    return best_index


def first_index_of_max(values: list[int]) -> int:
    """
    Return the first index of the maximum value, or -1 for an empty list.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    if not values:
        return -1
    max_value = max(values)
    for index, value in enumerate(values):
        if value == max_value:
            return index
    return -1
