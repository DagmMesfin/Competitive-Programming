class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) 
        left,right =  0,n-1

        if nums[left] <= nums[right]:
            return nums[left]
        
        while left+1<right:
            mid = (left+right)//2

            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
            
        return min(nums[left],nums[right])

