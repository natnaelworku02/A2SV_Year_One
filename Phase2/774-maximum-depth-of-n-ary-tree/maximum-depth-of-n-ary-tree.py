"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans = 0

        def helper(node):
            if not node.children:
                return 1
            
            val = 0
            for ind in node.children:

                val = max(val,helper(ind) + 1)
            
            return val 
        
        return helper(root)