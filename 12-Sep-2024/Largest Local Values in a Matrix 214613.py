# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxmat = []

        for i in range(n-2):
            maxlist = []
            for j in range(n-2):
                maxnum = 0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        maxnum = max(maxnum,grid[k][l])
                maxlist.append(maxnum)
            maxmat.append(maxlist)
        
        return maxmat
            