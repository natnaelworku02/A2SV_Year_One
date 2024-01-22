class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # return -2 %7
        sumed = sum(nums)%p
        if sumed ==0:
            return 0
        if sum(nums) < p:
            return -1
        ans = len(nums)
        pre = 0
        di = {0:-1}
        # flag = False
        for i in range(len(nums)):
            pre += nums[i]
            
            # print(pre - sumed,i,(pre - sumed)%p)
            mod = ((pre%p) - sumed) %p
            if mod in di:
                # print(i,mod)
                ans = min(ans,i-di[mod])
                # flag = True
            
            di[pre % p] = i
        # print(di,flag)

        return ans if ans != len(nums) else -1