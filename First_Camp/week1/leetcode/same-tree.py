# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or ( not q and p):
            return False
        if p and q and  p.val != q.val:
            return False
        if p and q and not self.isSameTree(p.left,q.left):
            return False
        if p and q and not self.isSameTree(p.right,q.right):
            return False
        return True
