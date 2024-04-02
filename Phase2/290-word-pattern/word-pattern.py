class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=list(s.split())
        di = defaultdict(str)
        dic = defaultdict(str)

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in di and s[i] not in dic:
                di[pattern[i]] = s[i]
                dic[s[i]] = pattern[i]
            elif di[pattern[i]] == s[i] and dic[s[i]] == pattern[i]:
                continue
            else:
                return False
        
        return True
        
            
        