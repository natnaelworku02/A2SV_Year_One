class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l=0
        r=0
        ans=[]
        while l<len(word1) and r<len(word2):
            ans.append(word1[l]+word2[r])
            l+=1
            r+=1
        while l <len(word1):
           ans.append(word1[l])
           l+=1
        
        while r < len(word2):
            ans.append(word2[r])
            r+=1
        return "".join(map(str,ans))


        