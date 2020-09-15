"""
Linked List Cycle - Easy #141

Given a linked list, return a boolean indicating if there is a cycle

Example:

Input: 
1 -> 2 -> 3 -> 4 -> 5 -> 11 -> 6 -> 8 -> 9 -> 7
          ^                                   |
          |                                   |
          -------------------------------------

Output:
True
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowPointer = head
        fastPointer = head

        while slowPointer and fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if (slowPointer == fastPointer):
                return True

        return False


        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""