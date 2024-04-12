# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque()
        visited = set()
        queue.append(root)
        visited.add(root)
        ans = []
        while queue:
            temp = 0
            leng = len(queue)
            for i in range(leng):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right:
                    queue.append(node.right)
                    visited.add(node.right)
            
            temp /= leng
            ans.append(temp)
        
        return ans
