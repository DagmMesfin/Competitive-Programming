class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        s = 1
        square = s*s
        while x>=square:
            s+=1
            square = s*s
        return s-1