class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex,x) for x in range(0,rowIndex+1)]
        