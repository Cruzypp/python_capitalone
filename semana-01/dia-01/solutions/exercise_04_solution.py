"""Solution: Summarize card swipes."""


def summarize_card_swipes_bruteforce(merchant_codes: list[str]) -> str:
    """
    Educational brute-force version.
    """
    parts = []
    index = 0
    while index < len(merchant_codes):
        end = index
        while end < len(merchant_codes) and merchant_codes[end] == merchant_codes[index]:
            end += 1
        parts.append(f'{merchant_codes[index]}:{end-index}')
        index = end
    return '|'.join(parts)


def summarize_card_swipes(merchant_codes: list[str]) -> str:
    """
    Group consecutive equal merchant codes and return a compact summary string like `A:2|B:1`.

    Complexity:
        Time O(n), space O(n) for the output.

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    if not merchant_codes:
        return ''
    parts: list[str] = []
    current = merchant_codes[0]
    count = 1
    for code in merchant_codes[1:]:
        if code == current:
            count += 1
        else:
            parts.append(f'{current}:{count}')
            current = code
            count = 1
    parts.append(f'{current}:{count}')
    return '|'.join(parts)
