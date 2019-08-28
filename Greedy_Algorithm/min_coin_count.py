def min_coin_count(value, coin_list):
    # Initialize variable for counting coins
    count = 0

    # give out bigger coins first and count how many are given out
    for coin in sorted(coin_list, reverse=True):
        # how many coins can be given out with the current coin
        count += (value // coin)

        # remaining value to be given out afterwards
        value %= coin

    return count


# Test
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
