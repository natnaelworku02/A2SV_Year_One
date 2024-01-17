class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.pre = [0]*len(nums)
        sumed= 0
        for i in range(len(nums)):
            sumed += self.nums[i]
            self.pre[i] = sumed
        



        

    def sumRange(self, left: int, right: int) -> int:
        
        
        return self.pre[right] - self.pre[left-1 ] if left>0 else self.pre[right]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)