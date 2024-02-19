class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        seen = set()
        sets = set()
        for f,b in zip(fronts,backs):
            seen.add(f)
            seen.add(b)
            if f == b:
                sets.add(f)
        remain = seen - sets
        return min(remain) if remain else 0

