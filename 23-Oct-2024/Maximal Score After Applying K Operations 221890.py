# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
        heapify(nums)

        ans = 0
        
        while k:
            numo = -heappop(nums)
            ans+=numo
            numo = ceil(numo/3)
            heappush(nums,-numo)
            k-=1

        return ans



        