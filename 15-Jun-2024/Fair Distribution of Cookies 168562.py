# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(index, distribution):
            nonlocal min_unfairness
            if index == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return min_unfairness  # Return the calculated unfairness

            for i in range(k):
                distribution[i] += cookies[index]
                if max(distribution) < min_unfairness:
                    backtrack(index + 1, distribution)
                distribution[i] -= cookies[index]
                if distribution[i] == 0:
                    break

        min_unfairness = float('inf')
        backtrack(0, [0] * k)
        return min_unfairness
