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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Dummy node to keep track of the inital head
        ans = ListNode(0)
        ans.next = head

        # Two pointers to travers through the list
        # first will start at n + 1 node and traverse to the end (null)
        # second will start at the head and traverse to the node before nth node
        first = ans
        second = ans
        
        # Initialize the first to point to the n + 1 node
        # This way there will be n nodes between the first and second pointers
        for i in range(1, n + 2):
            first = first.next

        # Move the two pointers at the same time
        # Eventually, first will reach the end and second will point to the node before nth node from the end
        while (first is not None):
            first = first.next
            second = second.next

        # Remove the nth node
        second.next = second.next.next
        
        return ans.next

        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""

s= Solution()

list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)

list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5

answer = s.removeNthFromEnd(list1, 2)
while (answer!= None):
    print(answer.val)
    answer = answer.next