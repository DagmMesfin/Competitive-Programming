class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = [nums[0]]
        for i in range(1, len(nums)):
            presum.append(presum[i-1] + nums[i])
        return presum