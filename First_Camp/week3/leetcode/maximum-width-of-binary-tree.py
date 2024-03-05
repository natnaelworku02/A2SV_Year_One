# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        di = defaultdict(list)

        def helper(root,lvl,lvlcount):
            if root:
                di[lvl].append(lvlcount)
                helper(root.left,lvl + 1,(2 * lvlcount) + 1)
                helper(root.right,lvl + 1,(2 * lvlcount) + 2)
            return 
        helper(root,0,0)
        for val in di.values():
            ans = max(ans,(val[-1] - val[0] + 1))
        return ans
