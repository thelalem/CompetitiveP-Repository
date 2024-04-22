# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                element = stack.pop() if stack else '$'
                if mapping[char] != element:
                    return False
            else:
                stack.append(char)

        return not stack