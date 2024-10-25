# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        

        ans = 0
        def dfs(node):
            nonlocal ans
            if not node.left and not node.right:
                return[1]
            
            left = []

            if node.left:
                left = dfs(node.left)
            
            right = []

            if node.right:
                right = dfs(node.right)
            # print(left)
            # print(right)
            for l in left:
                for r in right:
                    if abs(l + r)  <= distance:
                        # print(l,r,node.val)
                        ans += 1
            
            left.extend(right)
            for i in range(len(left)):
                left[i] += 1
            return left
        
        dfs(root)

        return ans
            
