class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        nums.extend(nums[0:n - k])
        nums[:] = nums[n - k:]