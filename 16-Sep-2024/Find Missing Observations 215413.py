# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        s = mean * (m + n)
        curr_sum = sum(rolls)
        req_sum = s - curr_sum
        
        if req_sum < n or req_sum > 6 * n:
            return []

        rem = req_sum % n
        q = req_sum // n
        ans = [q] * n

        for i in range(rem):
            ans[i] += 1

        return ans
        