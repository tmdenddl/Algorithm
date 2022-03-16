"""
Single Number - Easy #136

Given a non-empty array of integers, every element appears twice except for one, find it

Example:

Input: [2, 2, 1, 1, 4]
Output: 4

Explanation: 2*(1 + 2 + 4) - (1 + 1 + 2 + 2 + 4) = 4
    - 2 * (a + b + c) - (a + a + b + b + c) = c
    - (a + b + c)         => summation of the unique elements that you have
    - (a + a + b + b + c) => summation of all elements that you have

Algorithm used: 
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """"
        If all the elements appears twice in the List[int],
        sum of the unique numbers in the List[int] would be 2 * sum(set(num)).
        However, because we have an element that only appears once unlike other elements,
        we would need to substract that element from the 2 * sum(set(num)) to count for the single appearance.
        """
        return 2 * sum(set(nums)) - sum(nums)


"""
Time Complexity : O(n)
Space Complexity: O(n)
"""

s = Solution()
answer = s.singleNumber([2, 2, 1, 1, 4])
print(answer)