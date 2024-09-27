# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def check(m):
            res = -inf

            for s in start:
                res+=m
                if res>s+d:
                    return False
                res = max(res,s)

            return True

        l,h = 0,start[-1]+d
        ans = h
        
        while l<=h:
            m = (l+h)//2
            if check(m):
                ans = m
                l = m+1
            else:
                h = m-1

        return ans