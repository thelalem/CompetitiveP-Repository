# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dc = {}

        for num in nums2:
            while stack and stack[-1] < num:
                dc[stack.pop()] = num
            stack.append(num)

        while stack:
            dc[stack.pop()] = -1 

        result = [dc[num] for num in nums1]
    
        return result
