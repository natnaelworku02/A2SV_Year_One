class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        total = [arr[0]]
        for i in range(1,len(arr)):
            total.append( total[-1] ^ arr[i])
        total.insert(0,0)
        # print(total)
        for i in range(len(total)):
            for j in range(i+1 , len(total)):
                

                if total[i] ^ total[j]  == 0:
                    
                    ans += j - i - 1
            


        return ans 
