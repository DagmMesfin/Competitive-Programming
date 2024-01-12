class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        i = 0
        while i<len(nums):
            fast = i
            slow = i

            for l in range(len(nums)):

                fast = (fast + nums[fast]) % len(nums)
                if nums[fast] * nums[i] < 0:
                    break
                fast = (fast + nums[fast]) % len(nums)
                if nums[fast] * nums[i] < 0:
                    break
                
                slow = (slow + nums[slow]) % len(nums)
                next_slow = (slow + nums[slow])%len(nums)

                if slow == fast and slow != next_slow:
                    return True
            i+=1
        
        return False