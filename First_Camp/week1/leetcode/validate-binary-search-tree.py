# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if root:
                ans = []
                ans.extend(inorder(root.left))
                ans.append(root.val)
                ans.extend(inorder(root.right))
                return ans
            return []
        array = inorder(root)
        for i in range(len(array) - 1):
            if array[i] >= array[i+1]:
                return False
        return True