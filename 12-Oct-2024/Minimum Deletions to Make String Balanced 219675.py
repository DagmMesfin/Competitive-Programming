# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        res =0
        count = 0

        for char in s:
            if char == "b":
                count += 1
            elif count:
                res += 1
                count -= 1
        return res