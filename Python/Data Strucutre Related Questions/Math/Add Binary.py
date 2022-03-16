"""
Add Binary - Easy #067

Given 2 binary strings, return their sum
"""

class Solution:
    def addBinary(self, a: str, b: str):
        result = []
        carry = 0

        # We want to traverse the 2 strings from right to left
        i = len(a) - 1
        j = len(b) - 1
        
        # Until we have iterated over a or b or carry is 1
        while i >= 0 or j >= 0 or carry:
            total = carry

            # If we have not yet finished iterating over a
            if i >= 0:
                # At ith index, add a[i] and decrement i
                total += int(a[i])
                i -= 1

            # If we have not yet finished iterating over b
            if j >= 0:
                # At jth index, add b[j] and decrement j
                total += int(b[j])
                j -= 1

            # If the total is over 2, we need to separate the carry and the result
            # Example: total 3 would be 2 + 1 and 2 would become a carry and 1 would be the result on i or jth column
            result.append(str(total%2))
            carry = total // 2

        print("result" + str(result))
        # We have started from the highest digit of a, b so reverse the result
        return ''.join(reversed(result))
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""

s = Solution()

# 010101 => a
# 111111 => b
# 1010100
answer = s.addBinary("010101", "111111")
print(answer)

# 011 => a
# 100 => b
# 111
answer1 = s.addBinary("011", "100")
print(answer1)