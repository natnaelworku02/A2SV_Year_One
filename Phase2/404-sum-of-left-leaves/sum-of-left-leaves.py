# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans =  0
        stack = [[root,0]]
        while stack:
            node,ind = stack.pop()
            if not node.left and not node.right and ind:
                ans += node.val
            if node.left:
                # ans += node.left.val

                stack.append([node.left,1])
            if node.right:
                stack.append([node.right,0])
        
        return ans