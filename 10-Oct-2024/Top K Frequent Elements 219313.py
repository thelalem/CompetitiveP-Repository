# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            arr[freq].append(num)

        result = []
        for i in range(len(arr) - 1, 0, -1):  
            for num in arr[i]:
                result.append(num)
                if len(result) == k:  
                    return result