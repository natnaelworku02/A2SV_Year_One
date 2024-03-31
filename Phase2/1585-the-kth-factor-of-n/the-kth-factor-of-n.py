class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        val = set()
        val.add(1)
        val.add(n)
        i = 2
        while i < n:
            if n % i == 0:
                val.add(i)
            i +=1
        
        val = list(val)

        val.sort()
        print(val)
        return val[k-1] if k - 1 < len(val) else -1