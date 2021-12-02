def interssection(l1: list[str], l2: list[str]) -> list[str]:
    return list(set(l1) & set(l2))


def union(l1, l2):
    return list(set(l1) | set(l2))


def support(first_itemset: list[str], second_itemset: list[str], transactions: list[list[str]]) -> float:
    """
    Returns the support of an itemset in a list of transactions.
    """

    itemset = set(union(first_itemset, second_itemset))
    return round(__count_frequence(transactions, itemset) / len(transactions), 2)


def confidence(first_itemset: list[str], second_itemset: list[str], transactions: list[list[str]]) -> float:
    """
    Returns the confidence of an itemset in a list of transactions.
    """

    itemset = set(union(first_itemset, second_itemset))
    first_itemset_frequence = __count_frequence(transactions, set(first_itemset))
    return round(__count_frequence(transactions, itemset) / first_itemset_frequence, 2)


def __count_frequence(transactions: list[list[str]], itemset: set[str]):
    count = 0

    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1

    return count
