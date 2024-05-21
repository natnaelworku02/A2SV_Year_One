class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = []
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1 and i==0 :
                memo.append(1)
                continue
            elif ( obstacleGrid[0][i] != 1) and (memo[-1] != 0):
                memo.append(1)
                continue
            memo.append(0)
        # print(memo)

        # print(memo)
        for i in range(1,len(obstacleGrid)):
            cur =  [0  for _ in range(len(obstacleGrid[0]))]
            for j in  range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                    continue
                cur[j] += memo[j]
                # print(cur[j],memo[j])
                if j - 1 > -1:
                    cur[j] += cur[j-1]
            
            # print(cur)
            
            memo = cur
        
        # print(memo)

        
        return memo[-1]