class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numa = set(nums)
        nums = list(numa)
        nums.sort()
        L = 0
        R = 0
        maxLength = 0
        if len(nums) == 1:
            return 1
        while R < len(nums):
            if R == len(nums) - 1:
                break
            if nums[R+1] == nums[R] + 1:
                R += 1
            else:
                R+=1
                L = R
            maxLength = max(maxLength, R-L+1)
        return maxLength



            
