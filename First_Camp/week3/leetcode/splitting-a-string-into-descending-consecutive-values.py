class Solution:
    def splitString(self, s: str) -> bool:
        
        def helper(initial):
            if initial == len(s):
                return len(arr) >=2

            for i in range(initial,len(s)):
                m = s[initial:i+1]
                if arr and int(arr[-1]) - int(m) != 1:
                    continue
                arr.append(m)
                if helper(i + 1):
                    return True  
                arr.pop()
            
            return False
        
        arr = []
        ans = helper(0)

        return ans

