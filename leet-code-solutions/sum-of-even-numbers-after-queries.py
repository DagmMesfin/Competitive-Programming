class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        presum = 0
        for j in range(len(nums)):
            presum+= nums[j] if nums[j]%2==0 else 0
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                presum -= nums[queries[i][1]]
            nums[queries[i][1]] = nums[queries[i][1]]+queries[i][0]
            if nums[queries[i][1]] % 2 == 0:
                presum += nums[queries[i][1]]
            ans.append(presum)
        return ans