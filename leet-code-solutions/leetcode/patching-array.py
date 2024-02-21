class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
        sumo = 0
        cost = 0
        for i in range(len(nums)):
            if nums[i] > n: break

            while sumo < nums[i]-1:
                sumo+=1+sumo
                cost+=1
            
            sumo+=nums[i]

        while n > sumo:
            sumo+=1+sumo
            cost+=1

        return cost


        