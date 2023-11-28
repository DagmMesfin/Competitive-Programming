class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxiArea = (r-l) * min(height[r], height[l])
        while l != r:
            if min(height[r], height[l]) == height[l]:
                l += 1
            elif min(height[r], height[l]) == height[r]:
                r-=1
            maxiArea = max(maxiArea, (r-l) * min(height[r], height[l]))
        return maxiArea
             

