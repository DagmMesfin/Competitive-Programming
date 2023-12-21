class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checks if there is a repeated value for a given row
        def row_traversal(row, matrix):
            seto = set()
            for i in range(len(matrix[row])):
                if (matrix[row][i]).isnumeric():
                    if matrix[row][i] in seto:
                        return False
                    else:
                        seto.add(matrix[row][i])
            return True
        
        #checks if there is a repeated value for a given column
        def col_traversal(col, matrix):
            seto = set()
            for i in range(len(matrix)):
                if (matrix[i][col]).isnumeric():
                    if matrix[i][col] in seto:
                        return False
                    else:
                        seto.add(matrix[i][col])
            return True
        
        #checks if there is a repeated value for a given 3x3 matrix
        def three_by_three_traversal(st_i, st_j, matrix):
            seto = set()
            for i in range(st_i, st_i+3):
                for j in range(st_j, st_j+3):
                    if (matrix[i][j]).isnumeric():
                        if matrix[i][j] in seto:
                            return False
                        else:
                            seto.add(matrix[i][j])
            return True
        
        #implements the functions to check for validity of the sudoku
        for row in range(len(board)):
            if not row_traversal(row, board):
                return False

        for col in range(len(board[0])):
            if not col_traversal(col, board):
                return False
        
        for i in range(0,7,3):
            for j in range(0,7,3):
                if not three_by_three_traversal(i, j, board):
                    return False
        return True




        