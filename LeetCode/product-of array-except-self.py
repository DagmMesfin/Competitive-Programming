import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodlist = []
        prefixo = []
        postfixo = []
        prefix = 1
        postfix = 1
        prod = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            postfix *= nums[-1-i]
            prefixo.append(prefix)
            postfixo.append(postfix)
        postfixo = postfixo[::-1]
        for j in range(len(nums)):
            if j == 0:
                prod = postfixo[1]
            elif j == len(nums) - 1:
                prod = prefixo[len(nums)-2]
            else:
                prod = prefixo[j-1] * postfixo[j+1]
            prodlist.append(prod)
        return prodlist