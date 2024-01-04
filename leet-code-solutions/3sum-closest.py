class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = float('inf')
        n = len(nums)

        for i in range(n):
            l = i+1
            r = n-1
    
            while l<r:
                tot = nums[i] + nums[l] + nums[r]
                if tot > target:
                    if abs(tot-target) < abs(result):
                        result = tot-target
                    r-=1
                elif tot < target:
                    if abs(tot-target) < abs(result):
                        result = tot-target
                    l+=1
                else:
                    return target
        return target+result
            