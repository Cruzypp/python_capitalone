"""Solution: Longest consistent note."""


def longest_consistent_note_bruteforce(note: str) -> int:
    """
    Educational brute-force version.
    """
    best = 0
    for start in range(len(note)):
        for end in range(start, len(note)):
            chunk = note[start:end + 1]
            if all(c.isalpha() for c in chunk) or all(c.isdigit() for c in chunk):
                best = max(best, len(chunk))
    return best


def longest_consistent_note(note: str) -> int:
    """
    Return the length of the longest contiguous substring made only of letters or only of digits.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
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
        best = max(best, current)
    return best
