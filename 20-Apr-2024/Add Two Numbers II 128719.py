# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        res = None

        while stack1 or stack2 or carry:
            if stack1: carry += stack1.pop()
            if stack2: carry += stack2.pop()

            node = ListNode(carry%10)
            carry //= 10
            node.next = res
            res = node

        return res