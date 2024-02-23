class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        rb = float("-inf")
        st = []
        for i in range(len(nums) -1,-1 ,-1):
            if nums[i] < rb:
                print(rb,nums[i])
                return True
            # print(st)
            while st and st[-1] < nums[i]:
                rb = max(st.pop(),rb)
            st.append(nums[i])
         
        return False
                

        