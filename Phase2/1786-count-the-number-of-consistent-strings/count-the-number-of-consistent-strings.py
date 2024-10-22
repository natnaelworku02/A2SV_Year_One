class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        di = set()
        ans = 0
        for s in allowed:
            di.add(s)
        
        for word in words:
            for ch in word:
                if ch not in di:
                    ans += 1
                    break
        
        return len(words) - ans
