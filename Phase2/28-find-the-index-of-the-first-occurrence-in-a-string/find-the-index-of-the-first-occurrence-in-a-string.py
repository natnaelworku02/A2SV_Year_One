class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            l = i
            r = 0
            count = 0
            while r < len(needle) and l < len(haystack) and haystack[l] == needle[r]:
                l += 1
                r += 1
                count += 1
            
            if count == len(needle):
                return i
        
        return -1