"""Exercise: Shortest notes window."""


def shortest_notes_window(notes: str, required: str) -> str:
    """
    Find the shortest substring that contains all required characters at least once. Return an empty string if impossible.

    Args:
    notes: Source note string.
    required: Distinct characters that must appear.

    Returns:
        Shortest valid substring.

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

    from collections import Counter

    need = Counter(required)
    missing = len(required)
    left = 0
    start = 0
    min_size = float("inf")

    for right, char in enumerate(notes):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        #Cuando encontramos todos los elementos
        while missing == 0:
            if right - left + 1 < min_size:
                start = left

                #actualizamos la mejor entrada
                min_size = right - left - 1

            #optimizar el tamaño de la ventana
            need[notes[left]] += 1
            #si esta como missing hace la bsuqeda de nuevo
            if need[notes[left]] > 0:
                missing += 1
            left += 1

    if min_size != float('inf'):
        return notes[start: start+1]
    
    else:
        return ''




    # TODO: Implement the solution.
    raise NotImplementedError
