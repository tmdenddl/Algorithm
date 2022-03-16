"""
Count Primes - Easy #204

Count the number of prime numbers less than a non-negative given number n

What is Prime Number?
    - Greater than 1 
    - Non-divisible by anything except 1 and itself

Algorithm Used: Sieve of Eratostheness
"""

import math

class Solution:
    def countPrimes(self, n):
        # There is no prime number less than 2
        if (n < 2):
            return 0

        # List of booleans indicating whether the index is Prime number or not
        # 0, 1 are not Prime
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        # If we face a number that's greater than the square root of the given number,
        # we know that when the current number is squared, 
        # it would become greater the given nubmer, thus does not need to be considered.
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if (isPrime[i]):
                # Set all multiples of i as False == not Prime
                for multiples_of_i in range(i*i, n, i):
                    isPrime[multiples_of_i] = False
        
        return sum(isPrime)
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""

s = Solution()
answer = s.countPrimes(10) # 2, 3, 5, 7
print(answer)