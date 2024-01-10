class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l=0
        r=0
        if len(name) > len(typed):
            return False
        while l <len(name) and r < len(typed):
            if name[l] != typed[r]:
                return False
            r+=1
            if l+1 < len(name) and r < len(typed) and  name[l+1] == typed[r]:
                l+=1
                continue
            while r< len(typed) and typed[r] == name [l]:
                r+=1
            l+=1
        if l < len(name):
            return False
        if l >= len(name) and r< len(typed):
            return False
        return True 