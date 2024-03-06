# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
            def helper(l,r):
                if l >= r:
                    return 
                print(nums[l:r])
                val = max(nums[l:r])
                ind = nums.index(val)

                left_t = helper(l,ind)
                right_t = helper(ind + 1, r)

                return TreeNode(nums[ind],left_t,right_t)

            return helper(0,len(nums))
