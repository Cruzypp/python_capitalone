"""Solution: Count balance changes."""


def count_balance_changes_bruteforce(deltas: list[int]) -> int:
    """
    Educational brute-force version.
    """
    changes = 0
    previous_sign = 0
    for end in range(len(deltas)):
        balance = sum(deltas[: end + 1])
        current_sign = 1 if balance > 0 else -1 if balance < 0 else 0
        if current_sign != 0 and previous_sign != 0 and current_sign != previous_sign:
            changes += 1
        if current_sign != 0:
            previous_sign = current_sign
    return changes


def count_balance_changes(deltas: list[int]) -> int:
    """
    Count how many times the sign of the running balance changes while processing daily deltas.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    changes = 0
    balance = 0
    previous_sign = 0
    for delta in deltas:
        balance += delta
        current_sign = 1 if balance > 0 else -1 if balance < 0 else 0
        if current_sign != 0 and previous_sign != 0 and current_sign != previous_sign:
            changes += 1
        if current_sign != 0:
            previous_sign = current_sign
    return changes
