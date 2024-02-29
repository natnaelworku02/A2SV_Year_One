# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def difference(root):
            nonlocal max_diff

            if root:

                _min = float('inf')
                _max = float('-inf')

                minmax1 = difference(root.left)
                minmax2 = difference(root.right)

                if not minmax1 and not minmax2:
                    return root.val, root.val
                
                n = len(minmax1) if minmax1 else len(minmax2)
                for i in range(n):

                    if minmax1:
                        max_diff = max(abs(root.val - minmax1[i]),max_diff)
                    
                    if minmax2:
                        max_diff = max(abs(root.val - minmax2[i]) ,max_diff)
                
                
                for i in range(n):
                    
                    if minmax1:
                        _min = min(minmax1[i],_min,root.val)
                        _max = max(minmax1[i],_max,root.val)
                    
                    if minmax2:
                        _min = min(minmax2[i],_min,root.val)
                        _max = max(minmax2[i],_max,root.val)
                # print(_min,_max,root.val)
                
                return _min,_max
        difference(root)
        return max_diff

        