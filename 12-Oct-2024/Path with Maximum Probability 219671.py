# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        pq = [(-1.0, start_node)]
        while pq:
            prob, node = heappop(pq)
            prob = -prob
            if prob < max_prob[node]:
                continue
            for nei, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[nei]:
                    max_prob[nei] = new_prob
                    heappush(pq, (-new_prob, nei))
        return max_prob[end_node]