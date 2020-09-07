"""
Find First and Last Position of Element in Sorted Array - Medium #034

Given an array of integers 'nums' sorted in ascending order,
find the starting and ending position of a given target value

Example:
0   1   2   3   4   5
10  11  11  11  15  16

target: 11
start : 1
end   : 3
"""
class Solution:
    def getLeftPosition(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                if (mid - 1 >= 0 and nums[mid - 1] != target or mid == 0):
                    return mid
                right = mid - 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def getRightPosition(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                if ((mid + 1 < len(nums)) and (nums[mid + 1] != target) or (mid == len(nums) - 1)):
                    return mid
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        return [left, right]

    




"""
Time Complexity : O(log(n))
Space Complexity: O(1)
"""