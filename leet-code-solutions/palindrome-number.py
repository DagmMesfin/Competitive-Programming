class Solution:
    def isPalindrome(self, x: int) -> bool:
        stro = str(x)
        for i in range(len(stro)):
            if stro[i] != stro[-1-i]:
                return False
        return True