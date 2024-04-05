# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        level = 0
        count = 1  
        queue = deque()

        if root:
            queue.append(root)
        
        while queue:
            
            node= queue.popleft()
            ans.append([node.val,level])
            count -= 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if not count:
                count = len(queue)
                level += 1
            

        ans.sort(key = lambda x : x[1])

        _max=  ans[-1][1] if ans else -1

        res = [[] for _ in range(_max + 1)]
        
        for val,ind in ans:
            res[ind].append(val)
        
        return res
