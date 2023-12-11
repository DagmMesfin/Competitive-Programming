class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        limit = len(arr)/4
        result = []
        uniquenumbers = set(arr)
        for number in uniquenumbers:
            if arr.count(number) > limit:
                result.append(number)
        return result[0]
        