class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        val=0
        l= len(piles)//3
        for i in range(1,len(piles)-l,2):
            val+=piles[i]
            
        return val



        