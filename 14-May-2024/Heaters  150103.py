# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def dist_closest(heaters,house):
            left,right = 0,len(heaters) - 1
            min_dist = float('inf')
            while left <= right:
                mid = (left+right)//2
                min_dist = min(min_dist, abs(heaters[mid]- house))
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            return min_dist
        heaters.sort()
        radius = 0
        for house in houses:
            radius = max(radius, dist_closest(heaters,house))
        return radius