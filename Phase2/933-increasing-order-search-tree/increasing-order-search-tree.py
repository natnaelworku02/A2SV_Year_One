# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder (root):
            if root:
                ans = []
                ans.extend(inorder(root.left))
                ans.append(root.val)
                ans.extend(inorder(root.right))
                return ans
            return []
        nums = inorder(root)

        ans = TreeNode()
        temp = ans

        for i in range(len(nums)):
            temp.val = nums[i]

            if i < len(nums) - 1:
                temp.right = TreeNode()
                temp = temp.right
        # print(ans)
        return ans



