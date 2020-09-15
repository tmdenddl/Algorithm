"""
Add Two Numbers - Medium #002

Given two non-empty linked lists representing two non-negative integers,
digits are stored in reverse order and each of the nodes contain a single digit,
add the two numbers and return it as a new linked list

Example:

Input: 
l1: 2 -> 4 -> 3
l2: 5 -> 6 -> 4

Output:
7 -> 0 -> 8
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        pointer:ListNode = ans
        carry = 0
        sum = 0
        while (l1!=None and l2!=None):
            sum = carry
            if (l1 != None):
                sum += l1.val
                l1 = l1.next
            if (l2 != None):
                sum += l2.val
                l2 = l2.next
            carry = int(sum/10)
            pointer.next = ListNode(sum%10)
            pointer = pointer.next
        if (carry > 1):
            pointer.next = ListNode(carry)

        return ans.next

        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""