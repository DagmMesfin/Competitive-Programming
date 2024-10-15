# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        number = len(s)
        counto = 0
        ans = 0
        for i in range(number-1,-1,-1):
            if s[i] == "0":
                counto+=1
            if s[i] == "1":
                ans+=counto
        return ans