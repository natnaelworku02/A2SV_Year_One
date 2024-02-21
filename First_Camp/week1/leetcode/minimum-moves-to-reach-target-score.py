class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        ans = 0
        if target %2 == 1:
            ans +=1
            target -= 1
        while maxDoubles !=0:
            if target ==1:
                return ans
            
            ans +=1
            maxDoubles -=1
            target //= 2
            if target %2 == 1 and target != 1:
                ans +=1
                target -= 1
        ans += target -1
        return ans