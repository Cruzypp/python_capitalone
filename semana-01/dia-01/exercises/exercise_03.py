"""Exercise: Best support streak."""


def best_support_streak(scores: list[int], window_size: int) -> int:
    """
    Find the maximum sum of any contiguous block of exactly window_size support scores.

    Args:
    scores: Satisfaction score per interaction.
    window_size: Required block size.

    Returns:
        Maximum sum over a valid window.

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

    windowCount = 0
    currCount = 0
    best = 0

    if len(scores) < window_size:
        return 0

    windowCycles = len(scores) - window_size + 1

    for i in range(windowCycles):

        if i == 0:
            windowCount = currCount = sum(scores[0:window_size])
            continue

        currCount = currCount - scores[i-1] + scores[window_size+i-1]

        if currCount > windowCount:
             windowCount = currCount

        
    return windowCount

    raise NotImplementedError
