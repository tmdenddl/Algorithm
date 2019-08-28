def max_profit_memo(price_list, count, cache):
    # Base Case
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # if max profit already in the cache
    if count in cache:
        return cache[count]

    # profit = max profit
    # if price for selling count number of items is already in the list
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # compare all the combinations of the profits
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache)
                 + max_profit_memo(price_list, count - i, cache))

    # save the profit in the cache
    cache[count] = profit

    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# Test
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))