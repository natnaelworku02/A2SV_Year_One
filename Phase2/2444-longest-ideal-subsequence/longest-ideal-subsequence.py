class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ans = [0]*26

        for c in s:
            ind = ord(c) - 97
            left = ind - k if ind - k >=0 else 0
            right = ind + k+ 1 if ind + k +1 <=26 else 26
            ans[ind] = max(ans[left:right]) + 1

        return max(ans) 