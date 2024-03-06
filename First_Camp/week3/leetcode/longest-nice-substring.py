class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)  < 2:
            return ""
        ans = ""
        def helper(left,right):
            nonlocal ans
            di = set(s[left:right])
            ind = 0
            f = False
            for i in range(left, right):
                if s[i].swapcase() not in di:
                    f = True
                    break
                    # return max(left_substr,right_subsrt)
            if f : 
                helper(left , i)
                helper(i+1,right)
            elif not f and right - left > 1:
                if len(ans) < right - left :
                    ans = s[left:right]
        helper(0,len(s))
        return ans
