class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        result = ""
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                char = chr(ord('a') + num - 1)
                result += char
                i -= 2
            else:
                num = int(s[i])
                char = chr(ord('a') + num - 1)
                result += char
            i -= 1
        return result[::-1]