# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        vote_count = defaultdict(int)
        leader = None
        for i in range(len(persons)):
            person = persons[i]
            vote_count[person] += 1
            if leader is None or vote_count[person] >= vote_count[leader]:
                leader = person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == t:
                return self.leaders[mid]
            elif self.times[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        return self.leaders[right] 
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)