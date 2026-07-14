"""Solution: Build reward frequency."""


def build_reward_frequency_bruteforce(labels: list[str]) -> dict[str, int]:
    """
    Educational brute-force version.
    """
    result = {}
    for label in labels:
        if label not in result:
            result[label] = labels.count(label)
    return result


def build_reward_frequency(labels: list[str]) -> dict[str, int]:
    """
    Count how many times each reward label appears.

    Complexity:
        Time O(n), space O(k).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    counts: dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return counts
