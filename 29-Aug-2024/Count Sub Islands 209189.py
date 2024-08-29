# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid1[0]))] for j in range(len(grid1))]

        def inbound(row, col):
            return (0 <= row < len(grid1) and 0 <= col < len(grid1[0]))

        def dfs(visited, row, col):
            score = 1
            if grid1[row][col] != 0 and grid2[row][col] != 0:
                visited[row][col] = True
            if grid2[row][col] == 0:
                return 1
            if grid1[row][col] == 0 and grid2[row][col] != 0:
                return 0
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and int(grid2[new_row][new_col]) and not visited[new_row][new_col]:
                    score*=dfs(visited, new_row, new_col)
            return score
            
        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and not visited[i][j] and grid1[i][j] == 1:
                    count += dfs(visited,i,j)
        
        return count
        
        

                