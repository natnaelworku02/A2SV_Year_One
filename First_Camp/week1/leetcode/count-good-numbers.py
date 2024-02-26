class Solution:
   
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) +  7
        def myPow( x: float, n: int) -> float:
            if n ==  1:
                return x
            if n == 0:
                return 1
            if n == -1:
                return 1/x
            y = myPow(x,(n//2)) 
            return (y * y) % mod if n%2==0 else (y * y *x ) % mod
        
        ans = 1
        if n == 1:
            return 5
        ans = myPow(4,n//2)
        if (n - 1) % 2 == 0:
            if n != 1:
                return (ans * myPow(5,ceil(n/2))) % (10**9+7)
        else :
            return (ans * myPow(5,n//2)) % (10**9+7)
        return ans