class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda l : l[0]**2 + l[1]**2)
        return points[:k]