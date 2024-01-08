class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        minlen = float("inf")
        L = 0
        
        for R in range(len(nums)):
            sum += nums[R]
            while sum >= target:
                minlen = min(minlen, R-L+1)
                sum -= nums[L]
                L+=1

        return minlen if minlen != float("inf") else 0
                
            

        
        
            
