class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        countwindow = [0]*26
        countp = [0]*26
        res = []
        lenp = len(p)
        if lenp > len(s):
            return []
        for i in range(lenp):
            index = ord(p[i]) - ord("a")
            countp[index] += 1
        for i in range(lenp):
            index = ord(s[i]) - ord("a")
            countwindow[index] += 1
        if countp == countwindow:
            res.append(0)
        i = 1
        while i+lenp-1 < len(s):
            before = ord(s[i-1]) - ord("a")
            after = ord(s[i+lenp-1]) - ord("a")
            countwindow[before] -= 1
            countwindow[after] += 1

            if countp == countwindow:
                res.append(i)
            i+=1
        return res
        