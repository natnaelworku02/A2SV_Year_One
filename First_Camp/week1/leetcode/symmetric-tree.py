# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym (left,right):
            if not left and right or not right and left:
                return False
            if left and right and left.val != right.val:
                return False
            if left and right and not sym(left.left,right.right):
                return False
            if left and right and  not sym(left.right,right.left):
                return False
            return True
        ans = sym(root,root)
        return ans