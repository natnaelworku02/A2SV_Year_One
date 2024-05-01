class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # print(~4)
        val = [abs(num) for num in nums]
        
        leng = max(val)
        # print(bin(leng))
        for i in range(len(bin(leng)[2:])):
            count= 0
            for num in val:
                if num & 1<<i:
                    # print("hi",i)
                    count +=1
            # print(i,count)
            # print(i)
            if count % 3:
                ans += 1 << i
        count = 0
        # print(ans)
        for num in nums:
            if num <0:
                count +=1
        if count % 3:
            ans *= -1
        
        return ans