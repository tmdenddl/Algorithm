"""
Merged Two Sorted List - Easy #021

Given 2 separated sorted Linked Lists, merge them otgether and retain the sorting

Example:

Input: 
A: 1 -> 2 -> 4
B: 1 -> 3 -> 4

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        ans = cur

        while (l1 and l2):
            if (l1.val > l2.val):
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next

            cur = cur.next

        while (l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while (l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        
        return ans.next

        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""