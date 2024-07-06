# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
    
        def build_graph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                if node.left:
                    build_graph(node.left, node)
                if node.right:
                    build_graph(node.right, node)
        
        build_graph(root, None)
        queue = deque([(target.val, 0)])
        visited = set()
        visited.add(target.val)
        
        while queue:
            if queue[0][1] == k:
                return [node for node, dist in queue]
            
            node, dist = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return []