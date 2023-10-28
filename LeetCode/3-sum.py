class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, target, start, res, temp, num_need):
            if num_need != 2:
                for i in range(start, len(nums) - num_need + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    temp.append(nums[i])
                    helper(nums, target - nums[i], i + 1, res, temp, num_need - 1)
                    temp.pop()
                return
            l, r = start, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    temp.append(nums[l])
                    temp.append(nums[r])
                    res.append(temp[:])
                    temp.pop()
                    temp.pop()
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        nums.sort()
        res = []
        temp = []
        helper(nums, 0, 0, res, temp, 3)
        return res