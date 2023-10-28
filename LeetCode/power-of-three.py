import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        isthree = True
        if n>0:
            while n != 1:
                if n%3 != 0:
                    isthree = False
                    break
                n /= 3
        else:
            isthree = False
        return isthree