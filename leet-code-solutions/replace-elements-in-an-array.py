class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        mappo = {nums[i]:i  for i in range(len(nums))}
        for i in operations:
            nums[mappo[i[0]]] = i[1]
            temp = mappo.pop(i[0])
            mappo[i[1]] = temp
        return nums
        
        