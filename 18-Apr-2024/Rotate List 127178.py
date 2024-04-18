# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1

        k = k% length
        if k == 0:
            return head

        pos = length - k
        tail = head
        for _ in range(pos-1):
            tail = tail.next

        nhead = tail.next
        tail.next = None

        current.next = head
        return nhead
        
