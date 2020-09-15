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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if (len(lists)==0):
            return None

        i = 0
        last = len(lists) - 1
        j = last

        while (last != 0):
            i = 0
            j = last
            while (j > i):
                lists[i] = self.mergeTwoLists(list[i], list[j])
                i += 1
                j -= 1
                last = j
        
        return lists[0]


        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""