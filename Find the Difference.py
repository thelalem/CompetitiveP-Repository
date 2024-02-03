class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = list(t)
        for i in s:
            d.remove(i)
        return ''.join(d)