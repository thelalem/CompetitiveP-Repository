# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                x2, x1 = stack.pop(),stack.pop()
                stack.append(int(x1/x2))
            elif c == '-':
                x2, x1 = stack.pop(),stack.pop()
                stack.append(x1-x2)
            else:
                stack.append(int(c))

        return stack[-1]