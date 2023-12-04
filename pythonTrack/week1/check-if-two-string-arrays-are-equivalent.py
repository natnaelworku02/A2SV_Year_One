class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for n in word1:
            w1+=n
        for n in word2:
            w2+=n
        return w1==w2
    
        