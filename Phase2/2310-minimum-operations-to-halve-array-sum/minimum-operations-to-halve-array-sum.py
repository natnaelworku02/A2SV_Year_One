class Solution:
    def halveArray(self, nums: List[int]) -> int:
        comp = sum(nums)
        half = comp/2
        count = 0
        for i in range(len(nums)):
            nums[i] = - nums[i]
        heapq.heapify(nums)
        while comp > half:
            val = - (heapq.heappop(nums))
            val /=2
            comp -= val
            heapq.heappush(nums,-val) 
            count += 1
        return count

