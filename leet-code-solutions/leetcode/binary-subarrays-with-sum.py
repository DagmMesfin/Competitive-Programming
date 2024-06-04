class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        dicto = defaultdict(int)
        ans=0
        sumo=0
        dicto[0] = 1
        for i in nums:
            sumo+=i
            ans+=dicto[sumo-goal]
            dicto[sumo]+=1
        return ans