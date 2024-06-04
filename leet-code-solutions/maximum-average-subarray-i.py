class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumo = sum(nums[:k])
        maxAvg = sumo/k

        for i in range(1, len(nums)+1-k):
            sumo-=nums[i-1]-nums[i+k-1]
            maxAvg = max(maxAvg, sumo/k)
        
        return maxAvg