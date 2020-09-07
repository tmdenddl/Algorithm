"""
4 Sum II - Medium #454

Given four lists A, B, C, D of integer values, 
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is 0

Note: If A[i] + B[j] is equal to x, then C[k] + D[l] should be -x

Example:

Input:
A: [1, 2]
B: [-2, -1]
C: [-1, 2]
D: [0, 2]

Output: 

"""

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = {}
        ans = 0
        sA = len(A)
        sB = len(B)
        sC = len(C)
        sD = len(D)
        
        # For each of A[i] and B[j], calculate their sum and count the occurance of the sum
        for i in range(0, sA):
            x = A[i]
            for j in range(0, sB):
                y = B[j]

                # When it's the first time adding the sum to the map,
                # initialize the count as 0
                if (x + y not in m):
                    m[x + y] = 0

                m[x+y] += 1

        # For each of C[k] and D[l], calculate their sum and count the occurance of the sum
        for k in range(0, sC):
            x = C[k]
            for l in range(0, sD):
                y = D[l]

                # We want to see if the sums of two arrays have the counter sum
                # Note: If A[i] + B[j] is equal to x, then C[k] + D[l] should be -x
                target = -(x + y)

                if (target in m):
                    ans += m[target]

        return ans



        
"""
Time Complexity : O(n^2)
Space Complexity: O(n)
"""