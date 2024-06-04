class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dicto = {i:0 for i in range(3)}
        for i in range(len(nums)):
            dicto[nums[i]]+=1
        i = 0
        for j,k in dicto.items():
            for l in range(k):
                nums[i] = j
                i+=1
            
        