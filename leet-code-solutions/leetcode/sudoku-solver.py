class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_check = {i : [True] * 10 for i in range(9)}
        cols_check = {j : [True] * 10 for j in range(9)}
        boxes_check = {i: [[True] * 10 for _ in range(3)] for i in range(3)}
        points = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    idx = int(board[i][j])
                    rows_check[i][idx] = False
                    cols_check[j][idx] = False
                    boxes_check[i//3][j//3][idx] = False
                else:
                    points.append([i,j])
        
        def possible_comb(pt):
            if pt == len(points):
                return True
            
            x,y = points[pt]
            for col in range(1,10):
                if rows_check[x][col] and cols_check[y][col] and boxes_check[x//3][y//3][col]:
                    rows_check[x][col] = False
                    cols_check[y][col] = False
                    boxes_check[x//3][y//3][col] = False
                    board[x][y] = str(col)

                    if possible_comb(pt+1):
                        return True

                    rows_check[x][col] = True
                    cols_check[y][col] = True
                    boxes_check[x//3][y//3][col] = True
        
        possible_comb(0)


        





        
