"""Solution: Shortest notes window."""


def shortest_notes_window_bruteforce(notes: str, required: str) -> str:
    """
    Educational brute-force version.
    """
    best = ''
    for start in range(len(notes)):
        for end in range(start, len(notes)):
            chunk = notes[start:end + 1]
            if all(char in chunk for char in set(required)):
                if not best or len(chunk) < len(best):
                    best = chunk
    return best


def shortest_notes_window(notes: str, required: str) -> str:
    """
    Find the shortest substring that contains all required characters at least once. Return an empty string if impossible.

    Complexity:
        Time O(n), space O(k).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    if not notes or not required:
        return ''
    need = {char: 1 for char in required}
    have: dict[str, int] = {}
    missing = len(need)
    left = 0
    best = (float('inf'), 0, 0)
    for right, char in enumerate(notes):
        if char in need:
            have[char] = have.get(char, 0) + 1
            if have[char] == 1:
                missing -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            left_char = notes[left]
            if left_char in need:
                have[left_char] -= 1
                if have[left_char] == 0:
                    missing += 1
            left += 1
    return '' if best[0] == float('inf') else notes[best[1]:best[2]]
