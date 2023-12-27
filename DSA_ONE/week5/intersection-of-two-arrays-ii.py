class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=Counter(nums1)
        ans=[]
        for j,num in enumerate(nums2):
            if s[num]>0:
                ans.append(num)
                s[num]-=1
            
        return ans            
