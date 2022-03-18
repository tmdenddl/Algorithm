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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # slowPointer and fastPointer both start at the head
        slowPointer = head
        fastPointer = head

        # Loop until slowPointer, fasterPointer, or the node after fastPointer becomes null
        # We include fastPointer.next in this check because we'll need to move the pointer by 2 within the loop
        # fastPointer.next.next must be valid, otherwise point shifting will fail
        while slowPointer and fastPointer and fastPointer.next:
            # Move the fastPointer by 2 nodes, while moving the slowPointer by 1
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            # Eventually, if slowPointer and fastPointer meets, we've found the loop
            if (slowPointer == fastPointer):
                return True

        return False

"""
Time Complexity : O(n)
Space Complexity: O(1)
"""

s = Solution()

list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)
list11 = ListNode(11)
list6 = ListNode(6)
list8 = ListNode(8)
list9 = ListNode(9)
list7 = ListNode(7)

list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list11
list11.next = list6
list6.next = list8
list8.next = list9
list9.next = list7
list7.next = list3

answer = s.hasCycle(list1)
print(answer)