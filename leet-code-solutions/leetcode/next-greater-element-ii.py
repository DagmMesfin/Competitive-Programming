class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arro = []
        nums.extend(nums)

        for i in range(n):
            nxtelem = -1
            for j in range(i+1,n+i):
                if nums[j] > nums[i]:
                    nxtelem = nums[j]
                    break
            arro.append(nxtelem)
        return arro

                
            



        