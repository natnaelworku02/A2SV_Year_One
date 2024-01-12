class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=len(cardPoints)-k
        r=len(cardPoints) -1
        length = len(cardPoints)
        # print(cardPoints[l],cardPoints[r])
        ans = 0
        for i in range(l,length):
            ans+= cardPoints[i]
        # print(ans)
        prev = ans
        
        while r != k-1:
            
            r=(r+1) % length
            temp = prev - cardPoints[l] +cardPoints[r]
            ans = max(ans,temp)
            # print(ans)

            l= (l+1) % length
            # print(cardPoints[l],cardPoints[r])
            prev = temp
        return ans

