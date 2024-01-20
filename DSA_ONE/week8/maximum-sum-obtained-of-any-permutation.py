class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0]*n
        for req in requests:
            l,r = req
            count[l] += 1
            if r+1 < n:
                count[r+1] -= 1
        sumed = 0
        for i in range(n):
            sumed += count[i]
            count[i] = sumed
        count.sort()
        nums.sort()
        ans = 0
        for i in range(n):
            ans+= (nums[i] * count[i])
        return ans%(10**9+7)


        