# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def sumofBST(node):
            ans = [True,float('-inf'),float('inf'),node.val]

            if not node.left and not node.right:
                ans[1] = node.val
                ans[2] = node.val
            
            if node.left:
                temp = sumofBST(node.left)
                ans[0] = temp[0] and (node.val > temp[1])
                ans[1] = max(temp[1],node.val)
                ans[2] = min(temp[2],node.val)
                ans[3] += temp[3] 
            
            if node.right:
                temp  = sumofBST(node.right)
                ans[0] = temp[0] and ans[0] and (node.val < temp[2])
                ans[1] = max(ans[1],temp[1],node.val)
                ans[2] = min(ans[2],temp[2],node.val)
                ans[3] += temp[3] 
            
            if ans[0]:
                res.append(ans[3])

            return ans
        
          

        
        
        sumofBST(root)
        print(res)
        
        return max(res)
