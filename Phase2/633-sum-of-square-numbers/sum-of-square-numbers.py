class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l = 0
        r = int(sqrt(c))

        while l <=r:
            val = pow(l,2) + pow(r,2)

            if val >  c:
                r -= 1
            elif val < c:
                l += 1
            else:
                return True
        
        return False
         


