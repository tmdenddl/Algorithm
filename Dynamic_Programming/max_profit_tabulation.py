def max_profit(price_list, count):
    # initialize the profit_table with max profit of 0 item
    profit_table = [0]

    # find max profit for selling i items then store it into the table
    for i in range(1, count + 1):
        # if selling i items as indicated in the price_list
        if i < len(price_list):
            profit = price_list[i]
        # if selling more items than inidicated
        else:
            profit = 0

        # find the max_profit for selling i items
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        # add the profit to the table
        profit_table.append(profit)

    return profit_table[count]


# Test
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))