class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefixo = [0]*n
        suffixo = [0]*n
        answer = [0]*n
        for i in range(n):
            prefixo[i] += prefixo[i-1]+nums[i] if i != 0 else nums[i]
            suffixo[-1-i] += suffixo[-i]+nums[-1-i] if i != 0 else nums[-1-i]


        for i in range(n):
            before = prefixo[i-1] if i!=0 else 0
            after = suffixo[i+1] if i!=n-1 else 0
            answer[i] = nums[i]*(2*i + 1 - n) - before + after

        return answer

            
        