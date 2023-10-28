class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        isfour = True
        if n>0:
            while n != 1:
                if n%4 != 0:
                    isfour = False
                    break
                n /= 4
        else:
            isfour = False
        return isfour