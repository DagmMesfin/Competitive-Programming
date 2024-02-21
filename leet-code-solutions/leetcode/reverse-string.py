class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            numo1 = ord(s[i])
            numo2 = ord(s[-1-i])
            s[i] = chr(numo2)
            s[-1-i] = chr(numo1)
        