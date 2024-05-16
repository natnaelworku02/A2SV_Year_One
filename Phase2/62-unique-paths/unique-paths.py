class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [1  for _ in range(n)]
        # print(memo)
        for i in range(1,m):
            cur =  [0  for _ in range(n)]
            for j in  range(n):
                cur[j] += memo[j]
                # print(cur[j],memo[j])
                if j - 1 > -1:
                    cur[j] += cur[j-1]
            
            # print(cur)
            
            memo = cur
                

        
        return memo[-1]