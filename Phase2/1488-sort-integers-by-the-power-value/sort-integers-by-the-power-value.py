class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def check(val):
            count =  0
            while val > 1:
                if val % 2:
                    val = val * 3 + 1
                else:
                    val = val // 2
                count += 1
            return count
        
        ans = []
        for i in range(lo , hi + 1):
            val = check(i)
            ans.append([val,i])
        
        ans.sort()
        # print(ans)
        return ans[k - 1][1]