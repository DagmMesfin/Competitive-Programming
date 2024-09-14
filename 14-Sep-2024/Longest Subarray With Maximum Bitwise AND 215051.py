# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = -1
        maxo = max(nums)
        res = 0

        for i, num in enumerate(nums):
            if num != maxo: 
                k = i
            res = max(res, i - k)
            
        return res