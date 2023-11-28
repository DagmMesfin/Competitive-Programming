class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CrSt = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in CrSt:
                CrSt.remove(s[left])
                left += 1
                
            CrSt.add(s[right])
            res = max(res, right - left + 1)
        return res