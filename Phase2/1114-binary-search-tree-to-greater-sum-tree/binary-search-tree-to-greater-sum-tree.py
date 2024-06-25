# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumed = [0]
        def helper(node):
            if  not node:
                return 
            
            helper(node.right)

            sumed[0] += node.val

            node.val = sumed[0]
            helper(node.left)
            
        

            # return node.val

        helper(root)
        return root