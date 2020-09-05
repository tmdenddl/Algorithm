"""
Given an array of integers, return true if the following conditions are fulfilled:
    - Lenght of the array is bigger than or equal to 3
    - There exist some index i such that:
        a[0] < a[1] < ... < a[i]
        a[i] > a[i+1] > ... > a[a.size-1]

        Example:
                a[2]
            a[1]    a[3]    
        a[0]            a[4]
"""

def validMountainArray(self, A: List[int]) -> bool:
    if (len(A) < 3):
        return False
    
    i = 1
    # While elements are ascending, increment i
    while (i < len(A) and A[i] > A[i-1]):
        i += 1

    # This means there was no ascending or continuous ascending until the end
    if (i == 1 or i == len(A)):
        return False

    # While elements are descending, increment i
    while (i < len(A) and A[i] < A[i-1]):
        i += 1

    return i == len(A)


"""
Time Complexity : O(n)
Space Complexity: O(1)
"""