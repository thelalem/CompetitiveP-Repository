# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels= []
        def bst(node,lvl,num):
            if not node:
                return
            if len(levels) <= lvl:
                levels.append([num,num])
            else:
                levels[lvl][0] = min(levels[lvl][0],num)
                levels[lvl][1] = max(levels[lvl][1],num)
            right = 2*num
            left= right - 1

            bst(node.left,lvl+1,left)
            bst(node.right,lvl +1,right)

        bst(root,0,1)
        width = 0
        for left,right in levels:
            width = max(width,right-left+1)
        return width