"""Solution: Longest budget stretch."""


def longest_budget_stretch_bruteforce(expenses: list[int], budget: int) -> int:
    """
    Educational brute-force version.
    """
    best = 0
    for start in range(len(expenses)):
        total = 0
        for end in range(start, len(expenses)):
            total += expenses[end]
            if total <= budget:
                best = max(best, end - start + 1)
    return best


def longest_budget_stretch(expenses: list[int], budget: int) -> int:
    """
    Given non-negative expenses, return the longest contiguous stretch with sum at most budget.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    left = 0
    current = 0
    best = 0
    for right, value in enumerate(expenses):
        current += value
        while current > budget and left <= right:
            current -= expenses[left]
            left += 1
        best = max(best, right - left + 1)
    return best
