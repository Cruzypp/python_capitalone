"""Exercise: Pair with target spend."""


def pair_with_target_spend(prices: list[int], target: int) -> bool:
    """
    Return True when two sorted prices sum to the target amount.

    Args:

    prices: Sorted prices.
    target: Desired combined amount.

    Returns:
        Whether a pair exists.

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

    # TODO: Implement the solution.

    seen = set()
    found = False

    for price in prices:
        second = target - price
        if second in seen:
            found = True
        else:
            seen.add(price)

    return found


    raise NotImplementedError
