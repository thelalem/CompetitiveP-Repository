# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red= defaultdict(list)
        blue = defaultdict(list)

        for src,dst in redEdges:
            red[src].append(dst)
        for src,dst in blueEdges:
            blue[src].append(dst)
        
        answer = [-1 for _ in range(n)]
        q = deque()
        q.append([0,0,None])
        visit=set()
        visit.add((0,None))

        while q:
            node,leng,edge = q.popleft()
            if answer[node] == -1:
                answer[node]= leng
            if edge != "RED":
                for nei in red[node]:
                    if (nei,"RED") not in visit:
                        visit.add((nei,"RED"))
                        q.append([nei,leng+1,"RED"])

            if edge != "BLUE":
                for nei in blue[node]:
                    if (nei,"BLUE") not in visit:
                        visit.add((nei,"BLUE"))
                        q.append([nei,leng+1,"BLUE"])

        return answer