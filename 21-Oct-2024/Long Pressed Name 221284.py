# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m = 0
        nlen = len(name)
        tlen = len(typed)

        for n in range(tlen):
            if m < nlen and name[m] == typed[n]:
                m+=1
            elif n == 0 or typed[n] != typed[n-1]:
                return False

        return m == nlen

            