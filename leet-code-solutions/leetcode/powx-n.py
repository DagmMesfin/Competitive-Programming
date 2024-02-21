class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod = 1
        if n<0:
            x = 1/x
            n = abs(n)
        while n:
            if n%2:
                prod*= x
            x*=x
            n//=2
        return prod