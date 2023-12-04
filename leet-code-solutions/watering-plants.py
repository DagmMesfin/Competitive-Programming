class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        totalstep = 0
        initialcap = capacity-0
        for i in range(len(plants)):
            if capacity < plants[i]:
                totalstep += (2*i)+1
                capacity = initialcap
                capacity-=plants[i]
            else:
                capacity-=plants[i]
                totalstep += 1
            
        return totalstep