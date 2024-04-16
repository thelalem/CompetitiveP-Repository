# Problem: Split Two Strings to Make Palindrome - https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def check_palindrome_from_split(a: str, b: str) -> bool:
            i = 0
            j = len(a) - 1
            
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            
            return is_palindrome(a[i:j + 1]) or is_palindrome(b[i:j + 1])
        
        return check_palindrome_from_split(a, b) or check_palindrome_from_split(b, a)
