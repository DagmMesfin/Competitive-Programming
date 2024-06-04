class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = sorted(nums)
        ans = []
        for num in nums:
            ans.append(array.index(num))
        return ans
        