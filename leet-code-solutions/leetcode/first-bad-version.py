# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,h = 1,n
        mid = (l+h)//2

        while l+1<h:
            mid = (l+h)//2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid

        return l if isBadVersion(l) else h