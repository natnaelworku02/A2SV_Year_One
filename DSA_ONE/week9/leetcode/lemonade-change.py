class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        di = {5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                di[5] +=1
            elif bills[i] == 10 and di[5] == 0:
                print(i)
                return False
            elif bills[i] == 10 and di[5] >0:
                di[5] -=1
                di[10] +=1
            elif bills[i] == 20 and (di[5] == 0 or di[10] == 0):
                if di[5] >=3 and di[10] ==0:
                    di[5] -=3
                    di[20] +=1
                else:

                    # print(i)
                    return False
            else:
                di[20] +=1
                di[10] -=1
                di[5] -=1
        return True
        