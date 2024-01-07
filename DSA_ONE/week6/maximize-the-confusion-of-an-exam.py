class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        r=0
        lent=0
        lenf=0
        ans=0
        while r<len(answerKey):
            if answerKey[r]=='T':
                lent+=1
            else:
                lenf+=1
            while lent>k and lenf>k:
                if answerKey[l]=='T':
                    lent-=1
                else:
                    lenf-=1
                l+=1
            ans=max(ans,lent+lenf)
            r+=1
        return ans

        
            
            
        