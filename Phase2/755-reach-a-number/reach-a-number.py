class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        # print(target,k,k + 1 + k%2)
        return k if target % 2 == 0 else k + 1 + k%2

                

