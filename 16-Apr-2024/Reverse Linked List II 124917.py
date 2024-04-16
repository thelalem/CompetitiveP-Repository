# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        cur = prev.next
        next_node = None
        
        for _ in range(right - left):
            next_node = cur.next
            
            # Move the next node to directly after prev
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
    
        return dummy.next