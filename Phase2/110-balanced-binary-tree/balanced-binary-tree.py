# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        di = defaultdict(int)
        ans = True
        def helper(node):
            nonlocal ans
            if node:
                if not node.left and not node.right:
                    return [1,1]
                left = [0,0]

                if node.left:
                    left = helper(node.left)
                
                right = [0,0]

                if node.right :
                    right = helper(node.right)
                # print(node.val,left,right)
                if abs(left[0] - right[1]) > 1 or abs(right[0] - left [1] > 1):
                    # print("hi",node.val)
                    ans = False
                
                temp = [max(right[0],left[0]) + 1, max(right[1],left[1]) + 1]
                return temp
        
        helper(root)
        # print(ans)
        return ans
                
