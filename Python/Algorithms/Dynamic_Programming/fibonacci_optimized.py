def fib_optimized(n):
    previous = 0
    current = 1

    # update the variables on each round
    for i in range(1, n):
        # temp = current
        # current += previous
        # previous = temp
        current, previous = current + previous, current

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
