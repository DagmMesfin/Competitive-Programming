class Solution(object):
    def find132pattern(self, nums):
        stack = []
        curmin = nums[0]

        for i in nums[1:]:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i>stack[-1][1]:
                return True
            stack.append([i, curmin])
            curmin = min(curmin, i)
            
        return False
        