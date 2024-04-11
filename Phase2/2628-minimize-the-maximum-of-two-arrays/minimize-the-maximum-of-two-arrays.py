class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        
        right = 10**10
        left = 1
        ans = pow(10,10)
        
        while left <= right:
            mid = (left + right)//2
            div1 = mid - mid // divisor1
            div2 = mid - mid // divisor2
            both =mid - mid //lcm(divisor1,divisor2)
            if div1 >=uniqueCnt1 and div2 >= uniqueCnt2 and both >= uniqueCnt1 + uniqueCnt2 :
                
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
