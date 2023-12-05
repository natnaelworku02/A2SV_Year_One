class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row=['qwertyuiop','asdfghjkl','zxcvbnm']
        ans=[]
        for w in words:
            di=Counter()
            for i in range(len(w)):
                if w[i].lower() in row[0]:
                    di[0]+=1
                elif w[i].lower() in row[1]:
                    di[1]+=1
                else:
                    di[2]+=1
            if len(di)==1:
                ans.append(w)
        return ans
            
                
        