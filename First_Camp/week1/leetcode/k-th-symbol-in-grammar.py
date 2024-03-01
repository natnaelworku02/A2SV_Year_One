class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if (2**(n - 1))//2 < k :
            val = self.kthGrammar(n-1,   k - 2**(n - 1)//2 )
            return val ^ 1
        else:
            val  = self.kthGrammar(n-1,k)
            return val
        
        