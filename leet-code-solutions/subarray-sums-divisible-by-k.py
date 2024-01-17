class Solution(object):
    def subarraysDivByK(self, nums, k):
        ans , prefsum, d = 0,  0, {0:1}
        for num in nums:
            prefsum += num
            if  prefsum%k  in  d:
                ans = ans + d[prefsum%k]
            d[prefsum%k] = d.get(prefsum%k, 0) + 1
        return ans
        