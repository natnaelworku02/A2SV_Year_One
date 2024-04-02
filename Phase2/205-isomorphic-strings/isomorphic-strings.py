class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        di = defaultdict(str)
        dict = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in di and t[i] not in dict:
                di[s[i]] = t[i]
                dict[t[i]] = s[i]
            elif di[s[i]] == t[i] and dict[t[i]] == s[i]:
                continue
            else:
                return False

        return True 