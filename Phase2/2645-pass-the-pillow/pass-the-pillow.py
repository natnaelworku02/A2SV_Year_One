class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        full = time // (n -1)

        mod = ( time % (n - 1))

        if full % 2:
            return n - ( mod) 
        return 1+ mod 