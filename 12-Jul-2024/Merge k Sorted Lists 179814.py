# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i,node in enumerate(lists):
            if lists[i]:
                heappush(heap,(node.val,i))
                lists[i] = lists[i].next
        lst = ListNode()
        cur = lst
        while heap:
            val,i = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heappush(heap,(lists[i].val,i))
                lists[i] = lists[i].next
        return lst.next