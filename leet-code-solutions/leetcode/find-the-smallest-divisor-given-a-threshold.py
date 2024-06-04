class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def checker(divisor):
            sumo = 0
            for i in range(len(nums)):
                sumo += ceil(nums[i]/divisor)
            return sumo <= threshold
        
        left = 1
        right = max(nums)+1
        
        while left+1<right:
            mid = (left+right)//2
            if checker(mid):
                right = mid
            else:
                left = mid
        
        return left if checker(left) else right