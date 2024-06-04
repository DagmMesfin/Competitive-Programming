class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = -1
        right = n*m

        while left+1 < right:
            mid = (left+right)//2
            current = matrix[mid//m][mid%m]
            if current > target:
                right = mid
            elif current < target:
                left = mid
            else:
                return True

        return False
        