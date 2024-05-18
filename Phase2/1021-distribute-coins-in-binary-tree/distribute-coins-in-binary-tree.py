# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans =0
        def helper(node):
            nonlocal ans
            if not node:return 0
            
            left = helper(node.left)
            right = helper(node.right)
            print(left,right,ans,node)
            ans += abs(left) + abs(right)
            val = node.val - 1
            val += left + right
            return val
        
        helper(root)

        return ans
