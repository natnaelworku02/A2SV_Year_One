class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()

        ans = 0

        for i,num in enumerate(nums):

            _max = upper - num

            l = 0

            r = len(nums) -1

            while l <= r:
                mid = (l + r)//2

                if nums[mid] > _max:
                    r = mid - 1
                else:
                    l = mid + 1
            

            _min = lower - num

            l2 = 0
            r2 = len(nums) - 1

            while  l2 <= r2:
                mid = (l2 + r2 )//2

                if nums[mid] < _min:
                    l2 = mid + 1
                else:
                    r2 = mid - 1
            # print(l2,i,"____",r,num)
            left = max(l2,i)
            right = r
            if right >= left:
                ans += right - left + 1
                if left == i:
                    ans -= 1
        
        return ans