class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre  = [0]*1001
        for trip in trips:
            n,f,t = trip
            pre[f] +=n
            pre[t] += (n*-1)
        sumed = 0
        for i in range(1000):
            sumed += pre[i]
            if sumed > capacity:
                return False
        return True 