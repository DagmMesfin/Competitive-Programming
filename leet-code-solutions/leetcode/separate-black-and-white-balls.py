class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        counter = 0
        ans = 0
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                counter+=1
            if s[i] == "1":
                ans+=counter
        return ans