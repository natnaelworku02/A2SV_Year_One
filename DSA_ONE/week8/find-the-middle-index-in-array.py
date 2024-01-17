class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        arr = [0]*len(nums)
        pre = 0
        arr[0] = pre
        post = [0]*len(nums)
        post[0]= 0
        suf = 0
        for i in range(1,len(nums)):
            pre += nums[i-1]
            arr[i] = pre
            suf += nums[-i]
            post[-i-1] = suf
            # print(nums[-1-i],nums[i])
        # print(arr,post)
        for i in range(len(nums)):
            if arr[i] == post[i]:
                return i
        return -1


        