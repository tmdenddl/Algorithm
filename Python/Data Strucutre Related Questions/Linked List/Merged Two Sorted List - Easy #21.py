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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

s = Solution()

list1_1 = ListNode(1)
list1_2 = ListNode(2)
list1_4 = ListNode(4)
list1_1.next = list1_2
list1_2.next = list1_4

list2_1 = ListNode(1)
list2_3 = ListNode(3)
list2_4 = ListNode(4)
list2_1.next = list2_3
list2_3.next = list2_4

answer = s.mergeTwoLists(list1_1, list2_1)
print(answer) # This just prints the object

while (answer!= None):
    print(answer.val)
    answer = answer.next