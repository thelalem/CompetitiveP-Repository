class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        n = 0
        merged = ""
        if (len(word1) > len(word2)):
            n = len(word2)
        else:
            n = len(word1)
        while i < n:
            merged += word1[i] + word2[j]
            j += 1
            i += 1
        merged += word1[i:]
        merged += word2[j:]
        return merged
        
