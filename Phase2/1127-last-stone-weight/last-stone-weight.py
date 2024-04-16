class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        for i in range(len(stones)):
            stones[i] = - stones[i]
            
        heapq.heapify(stones)

        while len(stones) >1:
            
            x=   - heapq.heappop(stones)
            if len(stones) == 0:
                return x
            y = - heapq.heappop(stones)
            # print(x,y)
            if x != y:
                x -= y
                # print(y - x)
                heapq.heappush(stones, - x)
                # print(y)
            
        # print(stones)
        return  - stones[0] if stones else 0