class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        l = 0 
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            row_mid = mid // n
            col_mid = mid % n
            if target > matrix[row_mid][col_mid]:
                l = mid + 1
            elif target < matrix[row_mid][col_mid]:
                r = mid - 1
            elif target == matrix[row_mid][col_mid]:
                return True
        
        return False
        