class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):

                val = inf
                if i - 1 > - 1:
                    val = min(val,matrix[i-1][j])
                if i - 1  > - 1 and j - 1 > - 1:
                    val = min(val,matrix[i-1][j-1])
                if i - 1  >-1  and j + 1 < len(matrix[0]):
                    val = min(val,matrix[i-1][j+1])
                # print(val,i,j)
                matrix[i][j] += val
        
        return min(matrix[-1])

