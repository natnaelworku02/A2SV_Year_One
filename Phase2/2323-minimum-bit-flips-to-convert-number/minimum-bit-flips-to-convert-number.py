class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = bin(start ^ goal)

        return ans.count('1')