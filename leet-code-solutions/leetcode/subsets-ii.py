class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subsets=[]
        nums.sort()
        def sub(i):
            if i>=len(nums):
                res.append(subsets.copy())
                return res
            subsets.append(nums[i])
            sub(i+1)
            subsets.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            sub(i+1)
        
        sub(0)

        return res