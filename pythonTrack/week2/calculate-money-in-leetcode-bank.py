class Solution:
    def totalMoney(self, n: int) -> int:
        amount=0
        day=1
        prev_monday=1
        for i in range(1,n+1):
            if i%7==1 and i!=1:
                prev_monday+=1
                day=prev_monday
                amount+=day
                day+=1
            elif i==1:
                amount+=day
                day+=1
            else:
                amount+=day
                day+=1
        return amount

        