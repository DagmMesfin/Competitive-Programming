class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        decolist = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i+1]
            decolist += [val]*freq
        return decolist
        