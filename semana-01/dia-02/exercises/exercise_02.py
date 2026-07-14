"""Exercise: Build reward frequency."""


def build_reward_frequency(labels: list[str]) -> dict[str, int]:
    """
    Count how many times each reward label appears.

    Args:
    labels: Reward labels assigned to transactions.

    Returns:
        Dictionary from label to frequency.

    Examples:
        Review the test file for representative cases.

    Restrictions:
        Prefer clean interview-ready Python 3.12.

    Edge cases:
        Empty inputs, one-element inputs, duplicates, and basic large cases.

    Target complexity:
        Time O(n), space O(k).

    Interviewer questions:
        What assumptions are you making about the input?
        Can you describe a brute-force alternative first?
    """

    labelsDic = dict()
    for label in labels:
        if label in labelsDic.keys():
            labelsDic[label] += 1
        else:
            labelsDic[label] = 1

    return labelsDic

    # TODO: Implement the solution.
    raise NotImplementedError
