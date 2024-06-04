class Solution:
    def productExceptSelf(self, nums):
        prodlist = []
        left = [0]*len(nums)
        right = [0]*len(nums)
        prefix = postfix = 1
        prod = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            postfix *= nums[-i-1]
            left[i] = prefix
            right[-1-i] = postfix
        for j in range(len(nums)):
            if j == 0:
                prod = right[1]
            elif j == len(nums)-1:
                prod = left[len(nums)-2]
            else:
                prod = left[j-1] * right[j+1]
            prodlist.append(prod)
        return prodlist