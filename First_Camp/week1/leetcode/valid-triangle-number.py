class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        # print(nums)
        for i in range(len(nums)-1,1,-1):
            r = i-1
            l= 0
            while l< r:
                if nums[i] < nums[l]+nums[r]:
                    ans += r-l
                    r -=1
                else:
                    l+=1
        return ans
