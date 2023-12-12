class Solution:
    def isHappy(self, n: int) -> bool:
        check_val=n
        used=[]
        while check_val>0:
            ans=0

            while check_val !=0:
                modulo=check_val%10
                modulo **= 2
                ans+=modulo
                check_val//=10
            if ans  in used :
                return False
            else:
                used.append(ans)
            check_val=ans
            if ans ==1:
                return True
        return False
