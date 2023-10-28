class Solution:
    def isPalindrome(self, x: int) -> bool:
        xo = str(x)
        xoi = xo[::-1]
        if xo != xoi:
            return False
        return True