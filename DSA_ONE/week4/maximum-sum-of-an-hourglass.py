class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum=0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                temp_sum=grid[row][col]+grid[row][col+2]+(grid[row][col+1] + grid[row +1][col+1]+grid[row +2][col+1])+grid[row+2][col]+grid[row+2][col+2]
                if temp_sum > max_sum:
                    max_sum=temp_sum
        return max_sum
        