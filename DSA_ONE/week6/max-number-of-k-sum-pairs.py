class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums) - 1
        count =0
        while l<r:
            sumed = nums[l] + nums[r]
            if sumed < k:
                l+=1

            elif sumed > k:
                r-=1
            else:
                count+=1
                l+=1
                r-=1
        return count
