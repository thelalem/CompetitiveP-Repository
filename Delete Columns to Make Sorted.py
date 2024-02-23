class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0
        for i in range(len(strs[0])):
            letter = []
            for j in range(len(strs)):
                letter.append(strs[j][i])
            if letter != sorted(letter):
                deleted += 1
        return deleted
            
