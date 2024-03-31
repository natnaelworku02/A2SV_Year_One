class Solution:
    def smallestValue(self, n: int) -> int:
        def isprime(val):
            i = 2

            while i * i <= val:
                if val % i == 0:
                    return False
                i +=1
            
            return True
        
        def prod(val):

            ans = 0

            i = 2
            while i <=val:
                while val % i == 0:
                    ans += i
                    val //= i
                i +=1
            
            return ans

        num = n
        while  not isprime(num):
            temp = prod(num)
            if num == temp:
                return temp
            num = temp 
        
        return num