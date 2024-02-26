class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        collected = 0
        leftmax = [0]*n
        rightmax = [0]*n
        leftmax[0] = height[0]
        rightmax[-1] = height[-1]

        for i in range(1,n):
            leftmax[i] = max(height[i], leftmax[i-1])
            rightmax[-i-1] = max(height[-1-i], rightmax[-i])

        for i in range(n):
            collected+=min(leftmax[i],rightmax[i]) - height[i]
            
        return collected
