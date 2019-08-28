def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    # case 1: n in cache
    if n in cache:
        return cache[n]
    # case 2: n not in cache
    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        return cache[n]


def fib(n):
    # dictionary to store fib(n)
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

# USING LIST

# def fib_memo(n, cache):
#     # 코드를 작성하세요.
#     if n < 3:
#         return 1
#     elif cache[n] == -1:
#         cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
#     return cache[n]
# 
# 
# def fib(n):
#     # n번째 피보나치 수를 담는 리스트
#     fib_cache = [-1]*(n+1)
# 
#     return fib_memo(n, fib_cache)
# 
# 
# # 테스트
# print(fib(10))
# print(fib(50))
# print(fib(100))
