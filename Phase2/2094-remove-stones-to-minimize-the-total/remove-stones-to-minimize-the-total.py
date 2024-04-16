class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = - piles[i]
        heapq.heapify(piles)
        # print(piles)
        for i in range(k):
            val = -(heapq.heappop(piles))
            # print(val)
            val = ceil(val/2)
            heapq.heappush(piles,-val)
        return -(sum(piles))