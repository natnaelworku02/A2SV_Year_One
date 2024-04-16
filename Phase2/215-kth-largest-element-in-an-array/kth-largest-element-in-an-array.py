class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        ans = 0 
        for i in range(k):
            ans = heapq.heappop(nums)
        # print(ans)
        return  - ans