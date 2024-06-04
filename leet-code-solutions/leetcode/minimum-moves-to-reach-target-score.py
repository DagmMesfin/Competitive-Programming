class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cost = 0
        while target != 1:
            if target%2 == 0 and maxDoubles != 0:
                target//=2
                maxDoubles-=1
            elif maxDoubles:
                target-=1
            else:
                cost+=target-1
                break
            cost+=1
        return cost