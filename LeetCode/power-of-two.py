class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        istwo = True
        if n>0:
            while n != 1:
                if n%2 != 0:
                    istwo = False
                    break
                n /= 2
        else:
            istwo = False
        return istwo