class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        pre = num[:2]
        num = list(map(int,num[2:]))
        for i in range(len(num)):
            num[i] = 1 - num[i]
            num[i] =str(num[i])
        
        pre += ''.join(num)
        return int(pre,2)
        