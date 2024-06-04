class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transposed_matrix = []
        
        for i in range(len(matrix[0])):
            added_matrix = []
            for j in range(len(matrix)):
                added_matrix.append(matrix[j][i])
            transposed_matrix.append(added_matrix)
        return transposed_matrix
        