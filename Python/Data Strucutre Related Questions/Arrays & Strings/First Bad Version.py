"""
First Bad Version - Easy #278

Give a number N that represent amount of version and a function that 
accpets a number and returns whether it's a bad version or not.
Find the first bad version of the array

Note: If a version is bad, all versions after it are bad
"""
class Solution:
    def firstBadVersion(self, n: int):
        """
        :type n: int
        :rtype : int
        """

        left = 1
        right = n

        # Since we know after the first bad version rest of the following versions are also a bad version,
        # we can use a binary search approach
        while (left < right):
            mid = left + (right - left) // 2

            if not Solution.isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return left

    def isBadVersion(n: int) -> bool:
        """
        This should be a function that returns whether the current version n is a bad version or not
        """
        return n >= 3


"""
Time Complexity : O(log(n))
Space Complexity: O(1)
"""

s = Solution()
answer = s.firstBadVersion(10)
print(answer) # 3
