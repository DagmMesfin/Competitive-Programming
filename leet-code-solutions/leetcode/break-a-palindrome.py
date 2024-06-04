class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""

        palindrome = list(palindrome)

        for i,letter in enumerate(palindrome):
            if i == n//2:
                continue
            if letter != "a":
                palindrome[i] = "a"
                return "".join(palindrome)
        
        palindrome[-1] = "b"
        return "".join(palindrome)