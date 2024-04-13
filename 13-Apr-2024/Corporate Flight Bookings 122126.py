# Problem: Corporate Flight Bookings - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+1)
        for i,j,seats in bookings:
            diff[i-1] += seats
            if j < n:
                diff[j] -= seats
        print(diff)
        ans = [0] *n
        ans[0] = diff[0]
        for i in range(1,n):
            ans[i] = ans[i-1] + diff[i]         
        return ans