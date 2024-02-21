class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda l:l[1])
        costs = 1
        current = 0
        i = 1
        while i < len(points):
            if points[current][1] < points[i][0]:
                current = i
                i += 1
                costs+=1
            else:
                i+=1
        return costs
        


