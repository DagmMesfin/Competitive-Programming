class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        row = len(matrix) - 1
        column = len(matrix[0]) - 1
        tempi = row-1
        tempj = 0

        while(tempi != -1 or tempj!=0 ):
            i = tempi
            j = tempj
            while(i<row and j<column):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                j+=1
                i+=1
            tempi-=1
        
        tempi = 0
        tempj = 1
        while(tempi != 0 or tempj!=column):
            i = tempi
            j = tempj
            while(i<row and j<column):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                j+=1
                i+=1
            tempi=0
            tempj+=1

        return True

        