class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = Counter(nums)

        ans = -1

        for key  ,value in nums.items():
            if -key in nums and abs(key) > ans:
                ans = abs(key)

        return ans 