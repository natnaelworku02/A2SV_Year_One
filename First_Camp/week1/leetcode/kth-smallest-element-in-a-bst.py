# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root:
                ans = []
                ans.extend(inorder(root.left))
                ans.append(root.val)
                ans.extend(inorder(root.right))
                return ans
            return []
        array = inorder(root)
        count = 1
        for i in range(len(array)):
            if count == k:
                return array[i]
            count +=1
        return 