class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        a = n+0
        b = n+0
        sumo = 0
        costs.sort(key = lambda x:abs(x[0]-x[1]), reverse = True)

        for i in range(2*n):
            if a>0 and b>0:
                if costs[i][0] < costs[i][1]:
                    sumo+=costs[i][0]
                    a-=1
                elif costs[i][1] <= costs[i][0]:
                    sumo+=costs[i][1]
                    b-=1
            else:
                if a>0:
                    sumo+=costs[i][0]
                    a-=1
                elif b>0:
                    sumo+=costs[i][1]
                    b-=1
        
        return sumo
            
        
