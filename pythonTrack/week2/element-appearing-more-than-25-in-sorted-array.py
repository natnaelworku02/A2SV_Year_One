class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=0
        check_val=-1
        for num in arr:
            if num != check_val:
                check_val=num
                count=1
            else:
                count+=1
            if count/len(arr)>0.25:
                return num
        # return arr[0]
            

        