class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums  = list(map(int,nums))
        nums = sorted(nums,reverse = True)[:k]
        heapq.heapify(nums)
        return str(nums[0])