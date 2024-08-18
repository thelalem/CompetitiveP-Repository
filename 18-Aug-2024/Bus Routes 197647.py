# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        route_map = defaultdict(set)
        for i, r in enumerate(routes):
            for s in r:
                route_map[s].add(i)

        queue = deque([source])
        result = 1
        buses = set()
        visited = set()
        while queue:
            sz = len(queue)
            for _ in range(sz):
                curr = queue.popleft()
                for i in route_map[curr]:
                    if i in buses:
                        continue
                    buses.add(i)

                    for s in routes[i]:
                        if s in visited:
                            continue

                        if s == target:
                            return result
                        
                        visited.add(s)
                        queue.append(s)

            result += 1

        return -1