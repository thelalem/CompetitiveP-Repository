class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lists = []
        for num in nums:
            if num < pivot:
                lists.append(num)
        for num in nums:
            if num == pivot:
                lists.append(num)
        for num in nums:
            if num > pivot:
                lists.append(num)
        return lists
