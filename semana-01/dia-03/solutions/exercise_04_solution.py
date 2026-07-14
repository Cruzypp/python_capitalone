"""Solution: Count close transfers."""


def count_close_transfers_bruteforce(amounts: list[int], threshold: int) -> int:
    """
    Educational brute-force version.
    """
    count = 0
    for i in range(len(amounts)):
        for j in range(i + 1, len(amounts)):
            if amounts[j] - amounts[i] <= threshold:
                count += 1
    return count


def count_close_transfers(amounts: list[int], threshold: int) -> int:
    """
    Count how many pairs of sorted transfer amounts differ by at most threshold.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    count = 0
    left = 0
    for right in range(len(amounts)):
        while amounts[right] - amounts[left] > threshold:
            left += 1
        count += right - left
    return count
