class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefsum = [0]*n
        sumo = 0
        for i in range(n):
            sumo+=nums[i]
            prefsum[i] = sumo
        maxo = 0
        for i in range(n):
            maxo = max(int(ceil(prefsum[i]/(i+1))), maxo)

        return maxo