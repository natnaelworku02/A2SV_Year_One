class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s)
        print(s)
        odd = 0
        char = ""
        ans = 0
        for key , value in s.items():
            if value %2 == 1  and value > odd:
                odd = value
                char = key
            if value %2 ==0:
                ans += value
        ans += odd
        for key, value in s.items():
            if key != char and value %2 == 1:
                ans += value -1
        return ans


        