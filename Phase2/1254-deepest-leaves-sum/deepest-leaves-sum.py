# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)

        def traverse(node,level):
            if node:
                di[level].append(node.val)
                if node.left:
                    traverse(node.left,level + 1)
                if node.right:
                    traverse(node.right,level + 1)
        
        traverse(root,0)
        keys = sorted(di.keys())
        
        return sum(di[keys[-1]])