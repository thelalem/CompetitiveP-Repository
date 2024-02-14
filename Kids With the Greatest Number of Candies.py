class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        lists = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                lists.append(True)
            else:
                lists.append(False)
        return lists