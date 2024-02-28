# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = TreeNode()
        

        def adding(left , right, cur):
            if not left and not right:
                
                return 
            if not left :
                
                return right
            if not right:
                
                return left 
            cur = TreeNode(left.val + right.val)
            cur.left = adding(left.left,right.left,cur.left)
            # cur.left = 
            # print(cur)
            cur.right = adding(left.right,right.right,cur.right)
            # cur.right = 
            return cur
        

        return adding(root1,root2,root)
