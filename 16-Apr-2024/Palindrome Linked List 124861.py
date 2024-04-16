# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True