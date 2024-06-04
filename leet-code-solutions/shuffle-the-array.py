class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arrangedlist = []
        x = nums[:n]
        y = nums[n:]
        for i in range(len(nums)):
            d = i//2
            if i%2 == 0:
                arrangedlist.append(x[d])
            else:
                arrangedlist.append(y[d])
        return arrangedlist

        