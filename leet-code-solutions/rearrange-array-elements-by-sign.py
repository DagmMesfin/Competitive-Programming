class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negative = []
        positive = []
        modarray = []
        for number in nums:
            if number > 0:
                positive.append(number)
            elif number < 0:
                negative.append(number)
        for i in range(len(positive)):
            modarray.append(positive[i])
            modarray.append(negative[i])
        return modarray

        