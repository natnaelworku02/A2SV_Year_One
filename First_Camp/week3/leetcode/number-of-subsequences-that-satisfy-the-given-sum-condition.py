class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = (10**9) + 7
        ans = 0
        for i in range(len(nums)):
            _min = i
            _max = len(nums) - 1
            count = _min
            while _min <= _max:
                mid = (_min + _max)//2
                # print(mid)
                if nums[mid]+ nums[i] <= target:
                    # print("hi",mid,i)
                    count = mid 
                    _min = mid + 1
                else:
                    _max = mid -1
            # print(count, i)
            count =count - i 
            if count != 0:
                ans += 2** count
            elif count ==0 and nums[i] *2 <= target:
                ans += 1
            

            # ans += 2**count if count != 0  or if  else 0
        # print(ans)
        return ans % mod

            
            