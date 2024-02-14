class Solution:
    def reverseWords(self, s: str) -> str:
        lists = list(map(str, s.strip().split()))
        lists = lists[::-1]
        return " ".join(lists)