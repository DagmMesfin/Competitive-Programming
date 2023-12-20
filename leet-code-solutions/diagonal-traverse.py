class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        len_row = len(mat) - 1
        len_col = len(mat[0]) - 1
        maxsum = len_row + len_col
        arr = []

        #traverses the list according to the common sum of te index they have
        for comsum in range(maxsum+1):
            #forward diagonal traverse for even common sum indices
            if comsum % 2 == 0:
                row = min(len_row,comsum)
                col = 0
                if row == len_row:
                    col += comsum - row
                #prevents overflow
                while(col <= min(len_col,comsum)):
                    arr.append(mat[row][col])
                    row-=1
                    col+=1
            #forward diagonal traverse for odd common sum indices
            else:
                col = min(len_col,comsum)
                row = 0
                if col == len_col:
                    row += comsum - col
                #prevents overflow
                while(row <= min(len_row,comsum)):
                    arr.append(mat[row][col])
                    row+=1
                    col-=1
        
        return arr
                





        