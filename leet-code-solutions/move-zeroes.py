class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        stacko = []
        for i in nums:
            if i!=0:
                stacko.append(i)
        for j in range(len(nums)-len(stacko)):
            stacko.append(0)
        nums[:] = stacko[::]
        