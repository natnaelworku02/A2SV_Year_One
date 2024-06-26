# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                val = []
                val.extend(inorder(root.left))
                val.append(root.val)
                val.extend(inorder(root.right))
                return val
            
            return []

        ans = inorder(root)


        def divconc(l,r):
            mid = (r+l)//2

            if l > r:
                return 

            left = divconc(l,mid - 1)
            right = divconc(mid + 1, r)

            return TreeNode(ans[mid],left,right)
        
        return divconc(0,len(ans)- 1)