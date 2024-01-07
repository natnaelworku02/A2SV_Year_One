class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        count = 0
        zero_count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count +=1
            else:
                count += 1
            while zero_count >1 :
                if nums[l] == 0:
                    zero_count -=1
                    
                else:
                    count -= 1
                l+=1
            if zero_count == 0:
                ans = max(count - 1,ans)
            else:
                ans = max(count,ans)
        return ans

        