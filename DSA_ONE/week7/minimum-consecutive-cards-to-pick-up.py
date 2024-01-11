class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        di = defaultdict (int)
        ans = len(cards)
        temp = -1
        l=0
        for i in range(len(cards)):
            if cards [i] in di:  
                temp = 0
                while l < len(cards) and cards[l] !=cards[i]:
                    di.pop(cards[l])
                    l+=1
                ans = min(i-l+1,ans)  
                di.pop(cards[l])
                l+=1

            di[cards[i]] = 1
            # print(di)
        return ans if temp != -1 else temp
            

        