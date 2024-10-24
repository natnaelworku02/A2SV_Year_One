class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        val  = 0
        comp = 0
        alpha = 26
        leng = len(needle) - 1

        for i in range(leng , -1 ,- 1):
            # print(haystack[i])
            val += alpha**(leng-i) * (ord(haystack[i])  - 96)
            comp += alpha**(leng-i) * (ord(needle[i] ) - 96)
        # print(val,comp)
        if val == comp:
            return 0
        
        for i in range(leng + 1, len(haystack)):
            # print(i - (leng + 1),i)
            val -= (ord(haystack[i - (leng + 1)]) - 96 ) * alpha**(leng)

            val *= alpha

            val +=  (ord(haystack[i]) - 96 )


            if val == comp:
                return i - leng
        
        return -1