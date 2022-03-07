def power(x, y):
    if y == 0:
        return 1

    # store the value so no extra work is needed
    subresult = power(x, y // 2)

    # try to divide the cases: even, odd
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# test
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
