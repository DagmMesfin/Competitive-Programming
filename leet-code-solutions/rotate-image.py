class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            for j in range(n-1-(2*i)):
                a = matrix[i][j+i]
                b = matrix[i+j][n-1-i]
                c = matrix[n-1-i][n-1-i-j]
                d = matrix[n-1-i-j][i]

                matrix[i][j+i] = d
                matrix[i+j][n-1-i] = a
                matrix[n-1-i][n-1-i-j] = b
                matrix[n-1-i-j][i] = c

        