class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sizo = 0
        points.sort(key = lambda l: l[0])

        for i in range(len(points)-1):
            sizo = max(sizo ,points[i+1][0] - points[i][0])
            
        return sizo