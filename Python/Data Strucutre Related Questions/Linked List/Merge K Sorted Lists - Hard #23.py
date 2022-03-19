"""
Merge K Sorted List - Hard #23

Merge k sorted linked lists and return it as one sorted linked list

Example:

Input: 
1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
"""

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Merge the two given Lists
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

    # We will be iterating through the Lists and merging two Lists at a time until every ListNodes have been merged
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # If there's no ListNode in the List, return None
        if (len(lists)==0):
            return None

        # Initializing 3 pointers
        # i will be at the beginning of the array
        # j and last will be at the end of the array
        i = 0
        last = len(lists) - 1
        j = last

        # Do a loop as long as last is not 0
        while (last != 0):
            # Reset i to 0 and j to last in the loop
            i = 0
            j = last
            # Do a loop as long as j is bigger than i
            while (j > i):
                # Merge the lists at i and j
                lists[i] = self.mergeTwoLists(list[i], list[j])
                # Increment i and decrement j, and set last to point to the last List
                i += 1
                j -= 1
                last = j
        
        # Since every ListNodes have been merged, there'll only be one ListNode in the List
        return lists[0]
        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""

s = Solution()

list1_1 = ListNode(1)
list1_4 = ListNode(4)
list1_5 = ListNode(5)
list1_1.next = list1_4
list1_4.next = list1_5

list2_1 = ListNode(1)
list2_3 = ListNode(3)
list2_4 = ListNode(4)
list2_1.next = list2_3
list2_3.next = list2_4

list3_2 = ListNode(2)
list3_6 = ListNode(6)
list3_2.next = list3_6

answer = s.mergeKLists([list1_1, list2_1, list3_2])
while (answer!= None):
    print(answer.val)
    answer = answer.next