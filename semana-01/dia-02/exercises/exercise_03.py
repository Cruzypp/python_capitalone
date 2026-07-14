"""Exercise: Merchant overlap count."""


def merchant_overlap_count(week_one: list[str], week_two: list[str]) -> int:
    """
    Count how many merchant codes are present in both weekly lists, ignoring duplicates inside the same week.

    Args:
    week_one: Merchant codes from week one.
    week_two: Merchant codes from week two.

    Returns:
        Number of distinct merchant codes present in both lists.

    Examples:
        Review the test file for representative cases.

    Restrictions:
        Prefer clean interview-ready Python 3.12.

    Edge cases:
        Empty inputs, one-element inputs, duplicates, and basic large cases.

    Target complexity:
        Time O(n + m), space O(n + m).

    Interviewer questions:
        What assumptions are you making about the input?
        Can you describe a brute-force alternative first?
    """

    codes_1 = set()
    codes_2 = set()

    for code in week_one:
        if code not in codes_1:
            codes_1.add(code)
    
    for code in week_two:
        if code not in codes_2:
            codes_2.add(code)

    return len(codes_1.intersection(codes_2))

    # TODO: Implement the solution.
    raise NotImplementedError
