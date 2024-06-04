class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        j = float('inf')
        k = float('inf')

        #this checks if we can find the k < j < i sequence
        for i in nums:

            #if i > j, and we know j > k then i>j>k is satisfied as well
            if i > j:
                return True
            
            if i <= k:
                k = i
            else:
                j = i
        
        return False
