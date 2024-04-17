# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        queue = deque()
        queue.append([root,[]])

        while queue:
            node,sttr = queue.popleft()
            sttr.append(chr(node.val + 97))
            # print(sttr)
            if not node.left and not node.right:
                ans.append(sttr[::-1])
            if node.left:
                queue.append([node.left,sttr.copy()])
            if node.right:
                queue.append([node.right,sttr.copy()])
        # print(ans)
        return ''.join(min (ans))