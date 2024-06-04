class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        n = len(mat)

        for i in range(n):
            sum+=(mat[i][i])+(mat[i][n-i-1])
        if n%2 == 1:
            sum-=mat[n//2][n//2]
            
        return sum
        
        