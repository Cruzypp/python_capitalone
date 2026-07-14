"""Solution: Best support streak."""


def best_support_streak_bruteforce(scores: list[int], window_size: int) -> int:
    """
    Educational brute-force version.
    """
    if window_size <= 0 or window_size > len(scores):
        raise ValueError('invalid window size')
    best = None
    for start in range(len(scores) - window_size + 1):
        total = sum(scores[start:start + window_size])
        best = total if best is None or total > best else best
    return best


def best_support_streak(scores: list[int], window_size: int) -> int:
    """
    Find the maximum sum of any contiguous block of exactly window_size support scores.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    if window_size <= 0:
        raise ValueError('window_size must be positive')
    if window_size > len(scores):
        raise ValueError('window_size cannot exceed the number of scores')
    current = sum(scores[:window_size])
    best = current
    for index in range(window_size, len(scores)):
        current += scores[index] - scores[index - window_size]
        best = max(best, current)
    return best
