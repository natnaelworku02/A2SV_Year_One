class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=len(nums) - 1
        count = nums.count(val)
        while r > -1 and nums[r] == val :
            # count +=1
            r-=1
        l=0
        
        while l <= r:

            if nums[l] == val:
                nums[l] , nums[r] = nums [r], nums[l]
                # print(nums)
                l+=1
                r-=1
                while r > -1 and nums[r] == val :
                    r-=1

            else:
                l+=1
        # print(nums,count)
        return len(nums) - count

        