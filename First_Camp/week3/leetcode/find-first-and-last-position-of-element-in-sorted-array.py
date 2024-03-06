class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        def helper(left,right,bool):
            
            # ans = [-1,- 1]
            mid = (left + right //2)
            while left <= right  :
                mid = (left+right)//2
                if nums[mid] == target:
                    if bool:
                        print("hi",bool,mid)
                        ans[0] = mid
                        right = mid -1
                    else:
                        ans[1] = mid
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid +1
        helper(0,len(nums) - 1,True)
        print(ans)
        helper(0,len(nums) - 1,False)

            
        return ans