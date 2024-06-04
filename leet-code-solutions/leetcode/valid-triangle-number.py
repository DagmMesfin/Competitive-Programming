class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        n = len(nums)
        
        for l in range(n-2):
            i = l+1
            for r in range(l+2, n):
                while i<r and nums[l]+nums[i] <= nums[r]:
                    i+=1
                count+=r-i

        return count