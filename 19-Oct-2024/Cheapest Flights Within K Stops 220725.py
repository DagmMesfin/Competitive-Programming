# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prevo = [inf]*n
        prevo[src] = 0

        for i in range(k+1):
            curr = prevo[:]
            for u,v,w in flights:
                curr[v] = min(curr[v],prevo[u]+w)
            
            prevo = curr[:]
        
        return prevo[dst] if prevo[dst] != inf else -1