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

    if window_size <= 0:
        raise ValueError("window_size must be positive")

    if len(scores) < window_size:
        return 0

    max_sum = sum(scores[:window_size])
    curr_sum = max_sum
    window_cycles = len(scores) - window_size + 1

    for i in range(1, window_cycles):
        curr_sum = curr_sum - scores[i - 1] + scores[window_size + i - 1]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum
