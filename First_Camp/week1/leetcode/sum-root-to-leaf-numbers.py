# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def concat(root,num):
            nonlocal ans
            if root:
                num  = ((num * 10) + root.val)  
                if not root.left and not root.right:
                    # num.append(str(root.val))
                    ans += num
                    # print(array)

                
                # num.append
                concat(root.left,num )
                concat(root.right,num )
                # num.pop()

                

        concat(root,0)
        
        
        return ans