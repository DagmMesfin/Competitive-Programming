# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = {i:i for i in range(0,n)}
        size = {i:1 for i in range(0,n)}
        
        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        
        def union(x, y):
            root1 = find(x)
            root2 = find(y)
            
            if root1 != root2:
                if size[root2] > size[root1]:
                    parents[root1] = root2
                    size[root2]+=size[root1]
                else:
                    parents[root2] = root1
                    size[root1]+=size[root2]
        for x,y in edges:
            union(x,y)
        

        count = 0
        visited = set()

        for child in parents:
            parent = find(child)
            if parent in visited:
                continue
            sizo = size[parent]
            count += sizo*(n-sizo)
            visited.add(parent)

        
        
        return count//2