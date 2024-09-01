# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        
        def compare(a, b):
            return (1 if a+b > b+a else -1) if a+b != b+a else 0

        nums_str.sort(key=cmp_to_key(compare), reverse=True)
        largest_num = ''.join(nums_str)
        return '0' if largest_num[0] == '0' else largest_num
