# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stk = []
        

        for i in range(n):
            if not stk or nums[stk[-1]] > nums[i]:
                stk.append(i)
        
        maxo = 0
        
        for j in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] <= nums[j]:
                maxo = max(maxo, j - stk.pop())
        
        return maxo