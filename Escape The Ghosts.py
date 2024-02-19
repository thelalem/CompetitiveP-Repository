class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distanceTarget = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghostDistance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if distanceTarget >= ghostDistance:
                return False
        return True