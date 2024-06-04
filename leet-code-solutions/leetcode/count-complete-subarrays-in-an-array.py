class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distincto = len(set(nums))
        dicto = dict()

        l = 0
        count = 0
        for r in range(len(nums)):
            dicto[nums[r]] = dicto.get(nums[r],0) + 1
            while len(dicto) == distincto:
                dicto[nums[l]] -= 1
                if dicto[nums[l]] == 0:
                    del dicto[nums[l]]
                l+=1
            count+=l
                
                    
        return count
