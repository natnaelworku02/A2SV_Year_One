class Solution:
    def minimumSteps(self, s: str) -> int:
        s= list(s)
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += count

            else:
                count +=1

        return ans
         
        