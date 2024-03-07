class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1
        row = 0
        while left <= right:
            mid = (left + right)//2

            if matrix[mid][0] > target:
                 right = mid - 1
            elif matrix[mid][0] <= target:
                row = mid
                left = mid + 1
        
        left  = 0
        right = len(matrix[0]) - 1
        col = 0
        
        while left <= right:
            mid = (left + right)//2

            if matrix[row][mid] > target:
                 right = mid - 1
            elif matrix[row][mid] <= target:
                col = mid
                left = mid + 1
        # print(row,col)
        return matrix[row][col] == target
        
