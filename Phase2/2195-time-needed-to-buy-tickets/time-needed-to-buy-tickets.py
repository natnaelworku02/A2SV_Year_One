class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        ind = k 
        qu = deque (tickets)
        while qu:
            if  ind ==0 and qu[ind] == 1:
                return count +1
            val = qu.popleft()
            val -=1
            count +=1
            if val != 0:
                qu.append(val)
            ind -=1
            if ind == -1:
                ind = len(qu) -1
        return count
        