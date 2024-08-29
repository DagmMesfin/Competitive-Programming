# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arr: List[List[int]]) -> int:
        curmin, curmax, res = arr[0][0], arr[0][-1], 0
        for i in range(1, len(arr)): 
            if curmax - arr[i][0] > res or arr[i][-1] - curmin >  res: 
                res = max(curmax - arr[i][0], arr[i][-1] - curmin)
            if arr[i][0] < curmin: 
                curmin = arr[i][0]  
            if arr[i][-1] > curmax: 
                curmax = arr[i][-1]
        return res