class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        sum = 0
        minlen = float(inf)
        for R in range(len(nums)):
            sum += nums[R]
            while sum >= target:
                minlen = min(minlen, R-L+1)
                sum -= nums[L]
                L+=1
        if minlen == float(inf):
            return 0
        return minlen
                
            

        
        
            

