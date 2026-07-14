"""Solution: IDs above threshold."""


def ids_above_threshold_bruteforce(records: list[tuple[str, int]], threshold: int) -> list[str]:
    """
    Educational brute-force version.
    """
    result = []
    for record_id, amount in records:
        if amount > threshold:
            result.append(record_id)
    return result


def ids_above_threshold(records: list[tuple[str, int]], threshold: int) -> list[str]:
    """
    Return the IDs whose amounts exceed the threshold.

    Complexity:
        Time O(n), space O(k).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    return [record_id for record_id, amount in records if amount > threshold]
