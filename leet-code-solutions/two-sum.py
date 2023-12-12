class Solution:
    def twoSum(self, nums, target):
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res=[i,j]
        return res
                