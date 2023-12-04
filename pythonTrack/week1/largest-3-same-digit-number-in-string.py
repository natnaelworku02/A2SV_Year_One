class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sttr=""

        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+2]==num[i]:
                if sttr <= num[i:i+3]:
                    sttr=str(num[i:i+3])
                
        return sttr
        