class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros_count = 0
        ones_count = nums.count(1)

        max_score = -1
        max_indices = []

        for i in range(n + 1):
            score = zeros_count + ones_count
            if score > max_score:
                max_score = score
                max_indices = [i]
            elif score == max_score:
                max_indices.append(i)

            if i < n:
                if nums[i] == 0:
                    zeros_count += 1
                else:
                    ones_count -= 1

        return max_indices
