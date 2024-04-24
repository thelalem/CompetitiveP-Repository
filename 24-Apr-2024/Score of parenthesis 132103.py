# Problem: Score of parenthesis - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for c in s:
            if c == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score, 1)
        return score