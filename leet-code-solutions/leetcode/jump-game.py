class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        idx_max = 0
        for i in range(n):
            idx_max = max(idx_max, i+nums[i])
            if i == idx_max:
                break
        return idx_max >= n-1