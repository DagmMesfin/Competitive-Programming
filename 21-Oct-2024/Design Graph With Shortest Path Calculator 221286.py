# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for i in range(n)]
        self.size = n

        for u,v,w in edges:
            self.graph[u].append((v,w))

    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        self.graph[u].append((v,w))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = {i: float('inf') for i in range(self.size)}
        distances[node1] = 0
        processed = set()

        heap = [(0, node1)]

        while heap:
            _, edge = heappop(heap)
            if edge not in processed:
                processed.add(edge)
                for nodo, w in self.graph[edge]:
                    distances[nodo] = min(distances[nodo], distances[edge]+w)
                    heappush(heap,(distances[nodo],nodo))
        
        return distances[node2] if distances[node2] != inf else -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)