# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = head

        while current:
            nextnode = current.next

            sorted_prev = dummy
            sorted_current = dummy.next

            while sorted_current and sorted_current.val < current.val:
                sorted_prev = sorted_current
                sorted_current =  sorted_current.next

            sorted_prev.next = current
            current.next = sorted_current

            current = nextnode

        return dummy.next