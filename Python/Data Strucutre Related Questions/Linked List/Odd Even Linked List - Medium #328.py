"""
Odd Even Linked List - Medium #328

Given a singly linked list, group all odd nodes together followed by the even nodes
Note: We are talking about the node number, not the value of the node

Example:

Input: 
1 -> 2 -> 3 -> 4 -> 5
2

Output:
1 -> 2 -> 3 -> 5
"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head):
            return head
        
        odd = head
        even = odd.next
        evenList = even

        while (even and even.next):
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = evenList

        return head

        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""