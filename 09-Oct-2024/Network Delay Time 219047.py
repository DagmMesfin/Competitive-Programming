# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for a,b,w in times:
            graph[a].append((b,w))

        distances = [float("inf")]*n
        distances[k-1] = 0

        visited = set()

        heap = [(0,k)]

        while heap:
            dist,edge = heappop(heap)

            if edge not in visited:
                visited.add(edge)
                for b,w in graph[edge]:
                    distances[b-1] = min(distances[b-1],distances[edge-1]+w)
                    heappush(heap,(distances[b-1],b))
        
        return max(distances) if float("inf") not in distances else -1