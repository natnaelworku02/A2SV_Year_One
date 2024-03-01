# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column = defaultdict(list)
        def vt(root,row,col):
            if root:
                column[col].append((row,root.val))
                vt(root.left,row+1,col - 1)
                vt(root.right,row + 1,col +1)
        vt(root,0,0)
        keys = list(column.keys())
        keys.sort()
        ans = []
        for values in column.values():
            values.sort()
        print(column)
        for i in range(len(keys)):
            ans.append([vals for row,vals in column[keys[i]]])
        return ans