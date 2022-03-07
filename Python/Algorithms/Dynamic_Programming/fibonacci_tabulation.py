def fib_tab(n):
    # create table
    fib_table = [0, 1, 1]

    # bottom-top approach
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
