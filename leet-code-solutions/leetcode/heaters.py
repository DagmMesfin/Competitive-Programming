class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()
        
        for i in range(len(houses)):
            left = heaters[bisect_left(heaters , houses[i])-1] if bisect_left(heaters , houses[i]) > 0 else float('-inf')
            right = heaters[bisect_left(heaters , houses[i])] if bisect_left(heaters , houses[i]) < len(heaters) else float('inf')
            res = max(res,min(houses[i] - left,right - houses[i]))
        
        return res