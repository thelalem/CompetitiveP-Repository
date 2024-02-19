class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left_ops = [0] * n
        right_ops = [0] * n
        
        balls, ops = 0, 0
        for i in range(1, n):
            balls += int(boxes[i - 1])
            ops += balls
            left_ops[i] = ops
        print(left_ops)
    
        balls, ops = 0, 0
        for i in range(n - 2, -1, -1):
            balls += int(boxes[i + 1])
            ops += balls
            right_ops[i] = ops
        print(right_ops)
        total_ops = [left_ops[i] + right_ops[i] for i in range(n)]
        
        return total_ops
