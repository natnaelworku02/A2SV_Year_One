class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        length = len(nums)
        ans = [-1]* length
        st = []
        for i in range(length):
            index = i % length
            while st and nums[st[-1]] < nums[index]:

                ind = st.pop()
                # print(nums[ind],ind)
                ans [ind] = nums[index]
            st.append(index)
            # print(st)
        
        max_ind  = st[0]
        print(st)
        st.clear()
        for i in range(length):
            i = (1 + i + max_ind) % length
            # print(nums[i],i,st)
            while len(st) != 0 and st[-1][1] < nums[i]:
                ind,val = st.pop()
                ans [ind] = nums[i]
            # print(st,"________")
            st.append([i,nums[i]])
            
        # print(st)
        return ans

        