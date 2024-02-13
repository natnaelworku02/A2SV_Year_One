class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        di = Counter(nums)
        size = len(di)
        # print(size)
        ans = defaultdict(int)
        last_ele = len(nums) - 1
        l = 0
        res = 0
        for r in range(len(nums)):
            ans[nums[r]] +=1
            
            while l <= r and len(ans) == size:
                # print(ans)
                res += last_ele - r +1
                ans[nums[l]] -=1
                if ans[nums[l]] == 0:
                    ans.pop(nums[l])
                l+=1
            
        return res
        