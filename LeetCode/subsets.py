class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subsets=[]
        def binary(i):
            if i>=len(nums):
                res.append(subsets.copy())
                return res
            subsets.append(nums[i])
            binary(i+1)
            subsets.pop()
            binary(i+1)
        binary(0)
        return res