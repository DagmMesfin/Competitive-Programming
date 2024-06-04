class Solution(object):
    def maxSum(self, grid):
        #a helper function that calulates the hour sum for a given starting indices
        def hour_sum(i,j,matrix):
            return sum(matrix[i][j:j+3]) + matrix[i+1][j+1] + sum(matrix[i+2][j:j+3])
        
        row = len(grid)
        col = len(grid[0])
        sum_max = 0
        
        #finding the maximum hourglass sum
        for i in range(row-2):
            for j in range(col-2):
                sum_max = max(sum_max, hour_sum(i,j,grid))
        
        return sum_max
        