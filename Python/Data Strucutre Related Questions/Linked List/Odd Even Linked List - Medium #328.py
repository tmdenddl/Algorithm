"""
Odd Even Linked List - Medium #328

Given a singly linked list, group all odd nodes together followed by the even nodes
Note: We are talking about the node number, not the value of the node

Example:

Input: 
1 -> 2 -> 3 -> 4 -> 5

Output:
1 -> 3 -> 5 -> 2 -> 4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head):
            return head
        
        # head will point to the first node of the oddList
        # Because the first node is odd, odd.next is even
        # evenList will point to the first node of the evenList
        odd = head
        even = odd.next
        evenList = even

        # Traverse till the end as long as even and evenList are valid
        while (even and even.next):
            # odd.next is even, so next odd would be even.next
            # Then move the pointer to the next odd that we just added
            odd.next = even.next
            odd = odd.next

            # even.next is odd, so next even would be odd.next
            # Then move the pointer to the next even that we just added
            even.next = odd.next
            even = even.next
        
        # At this point, we have two node lists, one odd and another even
        # Make the end of the odd's list point to the evenList, so even nodes come after odd nodes
        odd.next = evenList

        # head should point to the first node on the odd list which now includes even list at the end
        return head
        
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

list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5

answer = s.oddEvenList(list1)
while (answer!= None):
    print(answer.val)
    answer = answer.next