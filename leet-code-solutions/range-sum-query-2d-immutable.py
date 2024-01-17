class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixo = []
        for i in range(len(matrix)):
            listo = []
            sumo = 0
            for j in range(len(matrix[0])):
                sumo+=matrix[i][j]
                if i == 0:
                    listo.append(sumo)
                else:
                    listo.append(sumo+self.prefixo[i-1][j])
                
            self.prefixo.append(listo)
        print(self.prefixo)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumo = self.prefixo[row2][col2]
        if row1 != 0:
            sumo-=self.prefixo[row1-1][col2]


        if col1 != 0:
            sumo-=self.prefixo[row2][col1-1]
        
        if row1 != 0 and col1 != 0:
            sumo+=self.prefixo[row1-1][col1-1]

        return sumo



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)