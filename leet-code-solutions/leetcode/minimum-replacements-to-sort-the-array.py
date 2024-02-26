class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        nums.reverse()
        start = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > start:
                divido = ceil(nums[i]/start)
                res+=divido-1
                start = nums[i]//divido
            else:
                start = nums[i]
        
        return res

        