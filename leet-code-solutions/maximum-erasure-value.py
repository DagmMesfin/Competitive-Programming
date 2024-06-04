class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        unique = set()
        max_score = 0
        current = 0

        for r in range(len(nums)):
            while nums[r] in unique and l!=r:
                unique.remove(nums[l])
                current -= nums[l]
                l+=1
                
            unique.add(nums[r])
            current+=nums[r]
            max_score = max(max_score, current)
            
        return max_score




