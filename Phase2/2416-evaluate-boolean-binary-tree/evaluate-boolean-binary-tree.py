# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return
            
            if not node.left and not node.right:
                return node.val
            
            left = helper(node.left)
            right = helper(node.right)

            if node.val ==  2:
                return left | right
            else:
                return left & right
        
        return helper(root)