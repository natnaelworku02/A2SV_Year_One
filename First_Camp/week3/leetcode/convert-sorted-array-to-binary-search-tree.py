# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divconc(l,r):
            mid = (r+l)//2
            if l > r:
                return 
            # print(nums[mid])
            
            # left = divconc(l,mid - 1)
            # right = divconc(mid+1,r)
            node = TreeNode(nums[mid])
            node.left = divconc(l,mid - 1)
            node.right = divconc(mid + 1, r)
            return node
        
        head = divconc(0,len(nums)- 1)
        return head
