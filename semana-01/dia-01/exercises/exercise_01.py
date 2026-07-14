"""Exercise: Count balance changes."""


def count_balance_changes(deltas: list[int]) -> int:
    """
    Count how many times the sign of the running balance changes while processing daily deltas.

    Args:
    deltas: Daily balance changes, positive or negative.

    Returns:
        Number of sign changes between non-zero running balances.

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

    counter = 0
    balance = 0
    previous_sign = 0

    for delta in deltas:
        balance += delta
        current_sign = 1 if balance > 0 else -1 if balance < 0 else 0

        if current_sign != 0 and previous_sign != 0 and current_sign != previous_sign:
            counter += 1

        if current_sign != 0:
            previous_sign = current_sign

    return counter
