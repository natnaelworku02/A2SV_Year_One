"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def help (node):
            if not node:
                return []
            arr =[]
            for child in node.children:
                arr.extend(help(child))
            arr.append(node.val)
            return arr
        
        return help(root)

        