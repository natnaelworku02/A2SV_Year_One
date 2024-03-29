class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        mx = max(nums)
        di = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            if nums[r] == mx:
                di[mx] +=1
            
            while di[mx] >= k:
                if nums[l] == mx:
                    di[mx] -=1
                l += 1
            
            if di[mx] == k - 1:
                ans += l 
            
        return ans
