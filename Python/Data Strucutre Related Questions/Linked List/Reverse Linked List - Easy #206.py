"""
Reverse Linked List - Easy #206

Simply reverse the singly linked list, so head becomes the tail and tail becomes the head

Example:

Input: 
list: 1 -> 2 -> 3 -> 4 -> 5

Output:
1 <- 2 <- 3 <- 4 <- 5

which is same as...

5 -> 4 -> 3 -> 2 -> 1
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Basically we need two pointers: previous and next of the current nodes
        # These pointers will help when reversing the pointers between the nodes
        node = None # previous pointer
        
        # head indicates the current node,
        # if it's None, we've reached the end of the list
        while (head is not None):
            next = head.next # next pointer
            head.next = node
            node = head
            head = next

        # Example after the first iteration
        """
        node  head, next
           |  ||
        <- 1   3 -> 5 -> 2 -> 4
        """
        # Now the head pointer is at the end of the original list which is the new head
        return node



        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""

s = Solution()

list_1 = ListNode(1)
list_2 = ListNode(2)
list_3 = ListNode(3)
list_4 = ListNode(4)
list_5 = ListNode(5)

list_1.next = list_2
list_2.next = list_3
list_3.next = list_4
list_4.next = list_5

answer = s.reverseList(list_1)

# print(answer.val)

while (answer!= None):
    print(answer.val)
    answer = answer.next