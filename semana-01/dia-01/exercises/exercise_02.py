"""Exercise: Longest consistent note."""


def longest_consistent_note(note: str) -> int:
    """
    Return the length of the longest contiguous substring made only of letters or only of digits.

    Args:
    note: String containing letters, digits, and optional separators.

    Returns:
        Length of the longest valid contiguous block.

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

    best = 0
    current = 0
    previous_kind = ''

    for char in note:
        kind = 'letter' if char.isalpha() else 'digit' if char.isdigit() else 'other'

        if kind == 'other':
            current = 0
            previous_kind = ''
            continue

        if kind == previous_kind:
            current += 1
        else:
            current = 1
            previous_kind = kind

        if current > best:
            best = current

    return best
