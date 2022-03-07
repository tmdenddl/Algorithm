"""
Remove Nth Node From End - Medium #019

Given a linked list, remove the n-th node from the end of the list and return its head

Example:

Input: 
1 -> 2 -> 3 -> 4 -> 5
2

Output:
1 -> 2 -> 3 -> 5
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans
        
        for i in range(1, n+2):
            first = first.next

        while (first is not None):
            first = first.next
            second = second.next

        second.next = second.next.next
        
        return ans.next

        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""