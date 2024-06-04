class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = -1,x+1

        while left+1<right:
            mid = (left+right)//2
            if mid**2 > x:
                right = mid
            elif mid**2 < x:
                left = mid
            else:
                return mid
        return left