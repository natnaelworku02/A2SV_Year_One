class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        ind = -1
        for i in range(len(word)):
            if ch == word[i]:
                ind =  i
                break
        val = []
        if ind != -1:
            word = list(word)
            val = word[:ind +1][::-1]
            word = word[ind+1:]
            val.extend(word)
        # print(word)
            return "".join(val)
        
        return word