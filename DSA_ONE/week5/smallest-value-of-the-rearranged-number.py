class Solution:
    def smallestNumber(self, num: int) -> int:
        arr = []
        zeros = []
        isnegative=False
        if num * -1 >0:
            isnegative = True
            num *= -1
        temp_num=num
        if num == 0:
            arr.append('0')
        while temp_num >0:
            modulo= temp_num %10
            temp_num //=10
            if modulo == 0:
                zeros.append('0')
            else:
                arr.append(str(modulo))
        if isnegative:
            arr.sort(reverse=True)
        else:
            arr.sort()
        # print(arr)
        ans=[]
        zeros = ''.join(zeros)
        if isnegative == True:
            ans = arr
            ans.append(zeros)

            
        else:
            ans.append(arr[0])
            ans.append(zeros)
            ans.extend(arr[1:])

        ans = ''.join(ans)
        ans = int(ans)
        if isnegative ==True:
            ans *= -1


        return ans
        
        