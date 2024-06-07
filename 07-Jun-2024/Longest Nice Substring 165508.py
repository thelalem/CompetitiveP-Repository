# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            return all(char.swapcase() in sub for char in sub)
        
        n = len(s)
        longest = ""

        for i in range(n):
            for j in range(i+1,n+1):
                sub = s[i:j]
                if is_nice(sub) and len(sub) > len(longest):
                    longest = sub
        
        return longest