class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n== 2:
            return 1
        
        val = self.tribonacci(n- 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return val