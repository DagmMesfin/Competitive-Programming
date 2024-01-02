class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted = (''.join(filter(str.isalnum, s))).lower()
        revextr = extracted[::-1]
        if(extracted == revextr):
            return True
        else:
            return False
        