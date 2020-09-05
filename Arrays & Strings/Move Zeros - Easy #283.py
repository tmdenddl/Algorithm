"""
Given an array of integers, write a function to move all 0's to the end while maintaining the relative order of the other elements
"""

def moveZeros(arr):
    j = 0
    length = len(arr) - 1

    for num in arr:
        if (num != 0):
            arr[j] = num
            j += 1

    for i in range(j, length):
        arr[i] = 0    

"""
Time Complexity : O(n)
Space Complexity: O(1)
"""