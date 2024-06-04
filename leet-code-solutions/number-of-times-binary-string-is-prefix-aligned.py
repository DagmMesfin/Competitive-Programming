class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        sum = 0
        max_step = 0
        count_prefix = 0

        for i in range(len(flips)):
            sum+=flips[i]
            max_step = max(max_step,flips[i])
            sum_full = (max_step*(max_step+1)/2)
            if sum == sum_full:
                count_prefix += 1
        
        return count_prefix
        
        