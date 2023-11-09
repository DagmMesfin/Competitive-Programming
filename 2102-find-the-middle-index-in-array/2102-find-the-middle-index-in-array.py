class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sumleft = []
        sumright = []
        sumleft.append(nums[0])
        sumright.append(nums[-1])
        for i in range(1, len(nums)):
            sumleft.append(sumleft[i-1] + nums[i])
            sumright.append(sumright[i-1] + nums[-i-1])
        sumright = sumright[::-1]
        for j in range(len(nums)):
            sumol = sumor = 0
            if len(nums) == 1:
                sumol = sumor = 0
            elif j == 0:
                sumor = sumright[1]
            elif j == len(nums)-1:
                sumol = sumleft[-2]
            elif j<len(nums)-1 and j>0:
                sumol = sumleft[j-1]
                sumor = sumright[j+1]
            if sumor == sumol:
                return j
        return -1