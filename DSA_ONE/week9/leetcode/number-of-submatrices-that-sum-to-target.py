class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r= len(matrix)
        c = len(matrix[0])
        subsum = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                top = subsum [i-1][j] if i>0 else 0 
                left = subsum [i][j-1] if j >0 else 0
                top_left = subsum [i-1][j-1] if min(i,j) >0 else 0
                subsum[i][j] = matrix [i][j] + top + left - top_left
        ans = 0
        for i in range(r):
            for j in range(i,r):
                di = defaultdict(int)
                di[0] = 1
                for k in range(c):
                    top = subsum[i-1][k] if i>0 else 0
                    cur_sum = subsum [j][k] - top
                    
                    ans += di[cur_sum - target]
                    di[cur_sum] +=1
        return ans
        