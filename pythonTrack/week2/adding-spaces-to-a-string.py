class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sttr=""
        count=0
        for i,char in enumerate(s) :
            if count<len(spaces) and spaces[count]==i :
              sttr+=' '
              count+=1
            sttr+=char
           
        return sttr
        