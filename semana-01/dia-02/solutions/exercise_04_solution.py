"""Solution: Duplicate transaction IDs."""


def duplicate_transaction_ids_bruteforce(transaction_ids: list[str]) -> list[str]:
    """
    Educational brute-force version.
    """
    result = []
    for index, transaction_id in enumerate(transaction_ids):
        if transaction_id in result:
            continue
        if transaction_ids.count(transaction_id) > 1 and transaction_ids.index(transaction_id) != index:
            result.append(transaction_id)
    return result


def duplicate_transaction_ids(transaction_ids: list[str]) -> list[str]:
    """
    Return the transaction IDs that appear more than once, preserving the order of first duplicate detection.

    Complexity:
        Time O(n), space O(n).

    Comparison:
        The main solution avoids repeated work present in the brute-force version.
    """
    seen: set[str] = set()
    duplicates: set[str] = set()
    ordered: list[str] = []
    for transaction_id in transaction_ids:
        if transaction_id in seen and transaction_id not in duplicates:
            duplicates.add(transaction_id)
            ordered.append(transaction_id)
        else:
            seen.add(transaction_id)
    return ordered
