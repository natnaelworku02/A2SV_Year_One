class Solution:
    def minimumLength(self, s: str) -> int:
        
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                ind = i
                falg = False
                while i < j and s[i] == s[ind]:
                    i += 1
                    flag = True
                ind = j
                if i == j and flag:
                    return 0 
                while j > i and s[j] == s[ind]:
                    j -= 1
                # print(i,j)
            else:
                return j - i +1
        
        return 1


        