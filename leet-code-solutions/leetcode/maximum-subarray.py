class Solution(object):
    def maxSubArray(self, nums):
        Maxsum = nums[0]
        CurrSum = 0
        for num in nums:
            CurrSum = max(CurrSum, 0)
            CurrSum += num
            Maxsum = max(CurrSum, Maxsum)

        return Maxsum
        