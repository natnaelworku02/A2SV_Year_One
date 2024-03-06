class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(l,r):
            mid = (r+l)//2
            if l > r or mid >= len(nums) :
                return -1

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                val = binary(l,mid - 1)
                return val
            else:
                val = binary(mid + 1, r)
                return val
        return binary(0,len(nums))