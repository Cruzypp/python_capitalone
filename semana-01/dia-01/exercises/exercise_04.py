"""Exercise: Summarize card swipes."""


def summarize_card_swipes(merchant_codes: list[str]) -> str:
    """
    Group consecutive equal merchant codes and return a compact summary string like `A:2|B:1`.

    Args:
    merchant_codes: Merchant category codes observed in order.

    Returns:
        Pipe-separated summary of consecutive runs.

    Examples:
        Review the test file for representative cases.

    Restrictions:
        Prefer clean interview-ready Python 3.12.

    Edge cases:
        Empty inputs, one-element inputs, duplicates, and basic large cases.

    Target complexity:
        Time O(n), space O(n) for the output.

    Interviewer questions:
        What assumptions are you making about the input?
        Can you describe a brute-force alternative first?
    """

    # counter = dict();
    # summary = []

    # for code in merchant_codes:
    #     if code in counter:
    #         counter[code] += 1
    #     else:
    #         counter[code] = 1

    # for key in counter.keys():
    #     summary.append(f"{key}:{counter[key]}")

    # return '|'.join(summary)

    if not merchant_codes:
        return ""

    summary: list[str] = []
    current_code = merchant_codes[0]
    count = 1

    for code in merchant_codes[1:]:
        if code == current_code:
            count += 1
        else:
            summary.append(f"{current_code}:{count}")
            current_code = code
            count = 1

    summary.append(f"{current_code}:{count}")

    return "|".join(summary)

    # TODO: Implement the solution.
    raise NotImplementedError
