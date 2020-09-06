"""
Give a number N that represent amount of version and a function that 
accpets a number and returns whether it's a bad version or not.
Find the first bad version of the array

Note: If a version is bad, all versions after it are bad
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype : int
        """

        left = 1
        right = not
        while (left < right):
            mid = (right + left) // 2

            if (not isBadVersion(mid)):
                left = mid + 1
            else:
                right = mid

        return left

    def isBadVersion(n) -> bool:
        """
        This should be a function that returns whether the current version n is a bad version or not
        """
        return True


"""
Time Complexity : O(log(n))
Space Complexity: O(1)
"""