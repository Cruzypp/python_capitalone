"""Exercise: Longest budget stretch."""


def longest_budget_stretch(expenses: list[int], budget: int) -> int:
    """
    Given non-negative expenses, return the longest contiguous stretch with sum at most budget.

    Args:
    expenses: Non-negative daily expenses.
    budget: Maximum allowed sum.

    Returns:
        Maximum window length.

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

    count = 0
    left = 0
    maxWindow = 0

    for right, expense in enumerate(expenses):
        count += expense

        while count > budget and left < right:
            count -= expenses[left]
            left += 1

        currWindow = right - left + 1
        if currWindow > maxWindow:
            maxWindow = currWindow

    
    return maxWindow

        
        



    # TODO: Implement the solution.
    raise NotImplementedError
