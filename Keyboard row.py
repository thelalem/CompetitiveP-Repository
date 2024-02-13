class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        lists = []
        for word in words:
            set1 = set(word.lower())
            if set1.issubset(second_row) or set1.issubset(first_row) or set1.issubset(third_row):
                lists.append(word)
        return lists
        