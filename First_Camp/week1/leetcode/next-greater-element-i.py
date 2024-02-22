class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextbig = {}
        st = []
        for i in range(len(nums2)):
            while st and st[-1] < nums2[i]:
                nextbig [st[-1]] = nums2[i]
                st.pop()
            st.append(nums2[i])
        ans = [0]*len(nums1)
        for i in range(len(nums1)): 
            ans[i] = nextbig.get(nums1[i],-1)
        return ans
