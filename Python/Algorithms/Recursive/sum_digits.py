# return sum of all the digits of a number n
def sum_digits(n):
    # base case
    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)


# Test
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
