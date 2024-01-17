class Solution:
    def balancedString(self, s: str) -> int:
        def dupcheck (duplicate,compare):
            # flag = True
            for key,value in compare.items():
                if value > duplicate[key]:
                    return  False
            return True

        di = Counter(s)
        n = len(s)
        qouta = n//4
        hi = True
        compare = defaultdict(int)
        for key,value in di.items():
            if value > qouta:
                compare[key] = value - qouta
        if  len(compare) == 0:
            return 0

        duplicate =defaultdict(int)
        l=0
        ans = n
        for r in range(len(s)):
            if s[r] in compare :
                duplicate[s[r]] +=1
            
            
            while l <= r and dupcheck(duplicate,compare):
                # print(r,l,r-l+1)
                ans = min(ans,r-l+1)
                if s[l] in duplicate:
                    duplicate[s[l]] -=1
                if duplicate[s[l]] == 0:
                    duplicate.pop(s[l])
                l+=1

        return ans

                


        



        
