"""
Add Binary - Easy #067

Given 2 binary strings, return their sum
"""

class Solution:
    def addBinary(self, a: str, b: str):
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        # 010101 => a
        # 111111 => b
        
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
                total += int(a[j])
                j -= 1

            # Add each i || j th sum to the result array
            result.append(str(total%2))
            carry = total // 2

        # We have started from the highest digit of a, b so reverse the result
        return ''.join(reversed(result))
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""