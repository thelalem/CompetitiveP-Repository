# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            old[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = old[cur]
            copy.next = old[cur.next]
            copy.random = old[cur.random]
            cur = cur.next
        
        return old[head]