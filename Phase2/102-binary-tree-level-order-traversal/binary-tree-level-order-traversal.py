# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        

        queue = deque()
        res = []

        if root:
            queue.append(root)
        
        while queue:

            ans = []

            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # print(ans)

            res.append(ans)

            

        

        
        
        
        return res
