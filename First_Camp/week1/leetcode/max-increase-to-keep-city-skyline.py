class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = []
        col = []
        for i in range(len(grid)):
            row_max = 0
            col_max = 0
            for j in range(len(grid[0])):
                row_max = max(grid[i][j],row_max)
                col_max = max (grid[j][i],col_max)
            row.append(row_max)
            col.append(col_max)
        ans = 0
        for i in range(len(row)):
            for j in range(len(row)):
                ans += min(row[i],col[j]) - grid[i][j]
        return ans

        