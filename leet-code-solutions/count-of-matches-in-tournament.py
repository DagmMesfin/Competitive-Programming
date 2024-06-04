class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        while n != 1:
            if n%2 == 0:
                matches += n//2
                n = n//2
            else:
                matches += n//2
                n = n//2 + 1
        return matches