# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        q = deque([[root,0,0]])
        prevLvl,prevNum = 0,0

        while q:
            node,num,lvl = q.popleft()
            if lvl> prevLvl:
                prevLvl = lvl
                prevNum = num
            
            res = max(res,num-prevNum+1)

            if node.left:
                q.append((node.left,2*num,lvl+1))
            if node.right:
                q.append((node.right,2*num+1,lvl+1))
        return res
            
