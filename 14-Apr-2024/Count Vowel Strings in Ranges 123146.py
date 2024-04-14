# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou') 
    
        vowel_word_counts = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        
        prefix_counts = [0] * (len(words) + 1)
        for i in range(1, len(prefix_counts)):
            prefix_counts[i] = prefix_counts[i - 1] + vowel_word_counts[i - 1]
    
        ans = []
        for li, ri in queries:
            count = prefix_counts[ri + 1] - prefix_counts[li]
            ans.append(count)
        
        return ans
        