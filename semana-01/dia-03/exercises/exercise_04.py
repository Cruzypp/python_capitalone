"""Exercise: Count close transfers."""


def count_close_transfers(amounts: list[int], threshold: int) -> int:
    """
    Count how many pairs of sorted transfer amounts differ by at most threshold.

    Args:
    amounts: Sorted transfer amounts.
    threshold: Maximum allowed difference.

    Returns:
        Number of valid pairs.

    Examples:
        Review the test file for representative cases.

    Restrictions:
        Prefer clean interview-ready Python 3.12.

    Edge cases:
        Empty inputs, one-element inputs, duplicates, and basic large cases.

    Target complexity:
        Time O(n), space O(1).

    Interviewer questions:
        What assumptions are you making about the input?
        Can you describe a brute-force alternative first?
    """

    pairsAmount = 0
    i = 0
    left = 0

    for right in range(len(amounts)):
        while amounts[right] - amounts[left] > threshold:
            left += 1

        pairsAmount += right - left

    return pairsAmount




    # TODO: Implement the solution.
    raise NotImplementedError
