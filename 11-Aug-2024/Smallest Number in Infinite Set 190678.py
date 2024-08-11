# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.added_back = []

    def popSmallest(self) -> int:
        if self.added_back:
            return heapq.heappop(self.added_back)

        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back:
            heapq.heappush(self.added_back, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)