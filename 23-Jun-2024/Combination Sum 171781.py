# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, current_combination, start):
            if remain == 0:
                result.append(list(current_combination))
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(remain - candidates[i], current_combination, i)
                current_combination.pop()
        
        result = []
        candidates.sort()
        backtrack(target, [], 0)
        return result