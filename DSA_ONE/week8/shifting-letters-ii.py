class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * (len(s)+1)
        for shift in shifts:
            l,r,c = shift
            if c ==0:
                pre[l] -=1
                pre[r+1] += 1
            else:
                pre[l] += 1
                pre[r+1] -= 1
        ans = []
        sumed = 0
        for i in range(len(s)):
            sumed += pre[i]
            char = ord(s[i]) + sumed %26
            
            if char < 97:
                char =96 - char
                char = 122 - char
                ans.append(chr(char))
            elif char > 122:
                char -= 123
                char += 97
                ans.append(chr(char))
            else:
                ans.append(chr(char))
        return ''.join(ans)




        