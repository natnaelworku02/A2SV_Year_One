class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ans = []
        for i in range(len(dungeon[0]) - 1, - 1,- 1):
            if len(dungeon[0]) - 1 == i:
                if dungeon[-1][i] >0:
                    ans.append(0)
                else:
                    ans.append(dungeon[-1][i])
                continue
            # print(i)
            val = ans[-1] + dungeon[-1][i]
            if val >0:
                ans.append(0)
            else:
                ans.append(val)
        
        ans = ans[::-1]


        for i in range(len(dungeon) - 2, -1 ,- 1):
            cur =  [0] * len(dungeon[0])
            for  j in range(len(dungeon[0]) -1 , - 1 , -1):
                val = ans[j] + dungeon[i][j]
                val = 0 if val >0 else val
                if j < len(dungeon[0]) - 1:
                    val = max(val,cur[j +  1] + dungeon[i][j])
                    val = 0 if val > 0 else val

                cur[j] = val

            ans = cur

        
        
        
        return abs(ans[0]) + 1
