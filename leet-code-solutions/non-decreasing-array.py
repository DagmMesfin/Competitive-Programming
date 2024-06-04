class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #checker for whether the value is changed at most once
        ischanged = False

        #traverse through the list to check for non-decreasing array and possible changes
        for i in range(len(nums)-1):
            #checks if its satisfies the non-decreasing pattern and skips
            if nums[i] <= nums[i+1]:
                continue
            #returns false right away if the change is done at most once
            if ischanged:
                return False
            
            #changes the element for the first index to change it
            if i == 0:
                nums[i] = nums[i+1]
            #changes the element if the element below it is less than the element above it
            elif nums[i+1]>=nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            
            ischanged = True
        #returns true otherwise after all iterations
        return True
        