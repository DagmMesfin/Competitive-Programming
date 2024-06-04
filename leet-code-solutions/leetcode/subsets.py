class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subsets=[]
        def sub(i):
            if i>=len(nums):
                res.append(subsets.copy())
                return res
            subsets.append(nums[i])
            sub(i+1)
            subsets.pop()
            sub(i+1)
        sub(0)
        return res