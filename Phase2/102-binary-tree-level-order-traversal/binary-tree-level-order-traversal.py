# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)

        queue = deque()
        if root:
            queue.append([root,0])
        while queue:
            node,level = queue.popleft()
            ans[level].append(node.val)

            if node.left:
                queue.append([node.left,level + 1 ])
            if node.right:
                queue.append([node.right, level + 1])
            # print(queue)
            # print("________")

        _max =  max(ans.keys()) if ans else -1
        # print(_max)
        res = []
        for i in range(_max + 1):
            res.append(ans[i])
        
        return res
