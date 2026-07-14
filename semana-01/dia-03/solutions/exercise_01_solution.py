"""Solution: Pair with target spend."""


def pair_with_target_spend_bruteforce(prices: list[int], target: int) -> bool:
    """
    Educational brute-force version.
    """
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == target:
                return True
    return False


def pair_with_target_spend(prices: list[int], target: int) -> bool:
    """
    Return True when two sorted prices sum to the target amount.

    Complexity:
        Time O(n), space O(1).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    left = 0
    right = len(prices) - 1
    while left < right:
        current = prices[left] + prices[right]
        if current == target:
            return True
        if current < target:
            left += 1
        else:
            right -= 1
    return False
