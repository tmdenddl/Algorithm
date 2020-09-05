"""
Given an array of intergers of size N,
find the maximum sum of K consecutive elements
"""

def maxSum(arr, k):
    arraySize = len(arr)

    # If the window size k is bigger than the array size,
    # the operation is invalid
    if (arraySize <= k):
        print("Invalid Operation")
        return -1

    # Initialize the window_sum to be sum of first k consecutive elements
    # Initalize the max_sum to be window_sum
    window_sum = sum(arr[i] for i in range(k))
    max_sum = window_sum

    # Until reaching the end of the array,
    # remove the first element in the window,
    # add the following element after the window
    for i in range(arraySize - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

    

arr = [80, -50, 90, 100]
k = 2

answer = maxSum(arr, k) # answer should be 190
print(answer)
