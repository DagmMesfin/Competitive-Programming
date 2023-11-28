class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s0 = ""
        for i in range(len(s)-1, -1, -1):
            if not s[i].isalpha():
                continue
            s0 += s[i]
        j = 0
        ans = ""
        for i in range(len(s)):
            print(s[i].isalpha())
            if not s[i].isalpha():
                ans += s[i]
                j+=1
            else:
                ans += s0[i-j]
        return ans
            
