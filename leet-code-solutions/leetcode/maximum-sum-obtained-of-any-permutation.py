class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        preorder = [0]*n
        sumo=0
        q = len(requests)
        
        for i in range(q):
            l,r = requests[i][0],requests[i][1]
            
            if r < n-1:
                preorder[r+1] -= 1
            preorder[l]+=1
        
        for i in range(n):
            if i>0:
                preorder[i] += preorder[i-1]
        
        preorder.sort(reverse=True)
        nums.sort(reverse=True)
        
        
        for i in range(n):
            sumo+=preorder[i]*nums[i]
            sumo%=(1000000000+7)
        
        return sumo
        