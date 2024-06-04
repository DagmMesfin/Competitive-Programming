class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        res = []
        leno = len(digits)
        for i in range(leno):
            num += int(pow(10, leno-i-1)) * digits[i]
        num+=1
        leno = len(str(num))
        for i in range(leno):
            res.append(num // int(pow(10, leno-i-1)))
            num %= int(pow(10, leno-i-1))
        return res
        