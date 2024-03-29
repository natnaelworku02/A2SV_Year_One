class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        nums: list[bool] = [True for _ in range(n + 1)]

        nums[0] = nums[1] = False

        i = 2
        while i <= n:
            if nums[i]:
                j = 2 * i
                while j <= n:
                    nums[j] = False
                    j += i
            i += 1
        
        # print(nums)

        ans = []
        for i in range(2,ceil(len(nums)/2)):
            
            if  nums[i] and nums[n- i] :
                # print(i , n - i)
                val = [i,n - i]
                # val.sort()
                ans.append(val)
        
        # ans = list(ans)
        # print(ans)
        ans.sort()
        return ans


