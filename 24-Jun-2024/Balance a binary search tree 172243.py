# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def build_balanced_bst(sorted_vals):
            if not sorted_vals:
                return None
            mid = len(sorted_vals) // 2
            root = TreeNode(sorted_vals[mid])
            root.left = build_balanced_bst(sorted_vals[:mid])
            root.right = build_balanced_bst(sorted_vals[mid+1:])
            return root
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
    
        sorted_vals = inorder(root)
        
        return build_balanced_bst(sorted_vals)