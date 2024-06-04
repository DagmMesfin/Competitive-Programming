class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        stro = ''
        for i in range(len(s)):
            if s[i] == "#":
                stro = stro[:-2]
                stro+=chr(int(s[i-2:i]) + ord('a')-1)
            else:
                stro+=chr(int(s[i])+ord('a')-1)
        return stro
        