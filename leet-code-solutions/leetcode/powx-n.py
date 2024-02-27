class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod = 1
        if n<0:
            x = 1/x
            n = abs(n)
        def subPwr(n,x,prod):
            if n == 0:
                return prod
            if n%2:
                prod*= x
            x**=2
            n//=2
            return subPwr(n,x,prod)

        prod = subPwr(n,x,prod)

        return prod