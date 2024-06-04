class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        lenr = len(grid)
        lenc = len(grid[0])
        maxCol = [0]*lenc
        maxRow = [0]*lenr
        for i in range(lenr):
            for j in range(lenc):
                maxRow[i] = max(maxRow[i],grid[i][j])
                maxCol[j] = max(maxCol[j],grid[i][j])
        sumo = 0
        for i in range(lenr):
            for j in range(lenc):
                sumo+= min(maxCol[j], maxRow[i]) - grid[i][j]

        return sumo
