class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        evno = 0
        odno = 0
        for j in range(len(nums)):
            if j%2 == 0:
                res.append(even[evno])
                evno = evno+1
            else:
                res.append(odd[odno])
                odno = odno+1
        return res