"""Solution: Merchant overlap count."""


def merchant_overlap_count_bruteforce(week_one: list[str], week_two: list[str]) -> int:
    """
    Educational brute-force version.
    """
    count = 0
    seen = []
    for code in week_one:
        if code in seen:
            continue
        seen.append(code)
        if code in week_two:
            count += 1
    return count


def merchant_overlap_count(week_one: list[str], week_two: list[str]) -> int:
    """
    Count how many merchant codes are present in both weekly lists, ignoring duplicates inside the same week.

    Complexity:
        Time O(n + m), space O(n + m).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    return len(set(week_one) & set(week_two))
