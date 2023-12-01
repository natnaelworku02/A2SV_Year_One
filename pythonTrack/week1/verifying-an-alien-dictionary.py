class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        di={}
        num=1
        for o in order:
            di[o]=num
            num+=1
        for i in range(len(words)-1):
            temp1= words[i]
            temp2= words[i+1]
            j=0
            while min(len(temp1),len(temp2))>j:
                if temp1[j] == temp2[j]:
                    j+=1
                    continue
                else:
                    if di[temp1[j]]>di[temp2[j]]:
                        return False
                    else:
                        break
            else:
                if len(temp1)>len(temp2):
                    return False

        return True
            

        