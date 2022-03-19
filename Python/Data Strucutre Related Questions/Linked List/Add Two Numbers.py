"""
Add Two Numbers - Medium #002

Given two non-empty linked lists representing two non-negative integers,
digits are stored in reverse order and each of the nodes contain a single digit,
add the two numbers and return it as a new linked list

Example:

Input: 
l1: 2 -> 4 -> 3
l2: 5 -> 6 -> 4

This is same as 342 + 465 = 807 which would be represented as 7 -> 0 -> 8
Note: the digits are stored in the reverse order

Output:
7 -> 0 -> 8
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # This will be the dummy node whose next will be the head of the answer List
        ans = ListNode(0)
        # This pointer will be used to point to the current digit of the answer List
        pointer:ListNode = ans
        # carry will hold the overflow, and the sum will hold the current sum
        # (e.g. 6 + 8 = 14 -> carry = 1 and sum = 4)
        carry = 0
        sum = 0
        # Loop until we have digit left on either of the Lists
        while (l1!=None or l2!=None):
            # Add the previous carry into sum
            sum = carry
            # If we still have digits left on List1, add the value to the sum and move to the next digit(node)
            if (l1 != None):
                sum += l1.val
                l1 = l1.next
            # If we still have digits left on List2, add the value to the sum and move to the next digit(node)
            if (l2 != None):
                sum += l2.val
                l2 = l2.next
            # We only want the first digit of the sum if there's an overflow
            carry = int(sum/10)
            # Next node will have the curnent sum without the overflow
            pointer.next = ListNode(sum%10)
            pointer = pointer.next
        # If we still have a carry, we need to add one more digit to the answer List
        if (carry > 1):
            pointer.next = ListNode(carry)

        return ans.next
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""

s = Solution()

list1_2 = ListNode(2)
list1_4 = ListNode(4)
list1_3 = ListNode(3)

list1_2.next = list1_4
list1_4.next = list1_3

list2_5 = ListNode(5)
list2_6 = ListNode(6)
list2_4 = ListNode(4)

list2_5.next = list2_6
list2_6.next = list2_4

answer = s.addTwoNumbers(list1_2, list2_5)
while (answer!= None):
    print(answer.val)
    answer = answer.next

"""
Input: 
l1: 2 -> 4 -> 3
l2: 5 -> 6 -> 4

2 <- 4 <- 3
5 <- 6 <- 4

Output:
7 -> 0 -> 8
"""