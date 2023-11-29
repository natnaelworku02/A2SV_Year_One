class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i=0
        ans=[]
        while n>=3:
            if 3**i<n:
                i+=1
                continue
            elif 3**i==n :
                if i in ans:
                    return False
                return True
            else:
                i-=1
                if i in ans:
                    return False
                ans.append(i)
                n-=3**i
                i=0
        if n==2:
            return False
        return True

        