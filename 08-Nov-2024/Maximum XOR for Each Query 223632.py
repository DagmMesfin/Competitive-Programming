# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maxo: int) -> List[int]:
        k = 2 ** maxo - 1
        prefixo = [nums[0]]
        n = len(nums)

        for i in range(1, n): 
            prefixo.append(prefixo[i - 1] ^ nums[i])

        res = []
        
        for i in range(n - 1, -1, -1):
            res.append(prefixo[i] ^ k)

        return res