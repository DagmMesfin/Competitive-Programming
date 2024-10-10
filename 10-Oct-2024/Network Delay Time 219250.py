# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for a,b,w in times:
            graph[a].append((b,w))

        timo = [float("inf")]*n
        timo[k-1] = 0

        visited = set()

        heap = [(0,k)]

        while heap:
            dist,edge = heappop(heap)

            if edge not in visited:
                visited.add(edge)
                for b,w in graph[edge]:
                    timo[b-1] = min(timo[b-1],timo[edge-1]+w)
                    heappush(heap,(timo[b-1],b))
        
        return max(timo) if float("inf") not in timo else -1