class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lists = list(t)
        for letter in s:
            lists.remove(letter)
        return ''.join(lists)