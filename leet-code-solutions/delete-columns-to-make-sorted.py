class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        row_len = len(strs)
        col_len = len(strs[0])

        counter = 0  #counts how much columns needed to be deleted

        #full traversal through each column to check if they are sorted (using their ascii values)
        for j in range(col_len):
            prev = 0
            for i in range(row_len):
                if i == 0:
                    prev = ord(strs[i][j])
                else:
                    if prev > ord(strs[i][j]):
                        counter+=1
                        break
                    prev = ord(strs[i][j])
                    
        return counter




        