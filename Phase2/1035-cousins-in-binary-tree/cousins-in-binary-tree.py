# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue =deque()
        par = defaultdict(int)
        # visited = set()
        queue.append(root)
        # visited.add(root)

        while queue:
            x_ = False
            y_ = False
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    par[node.left.val] = node.val
                    # if not in visited
                    if node.left.val == x:
                        x_ = True
                    elif node.left.val == y:
                        y_ = True
                    queue.append(node.left)
                
                if node.right:
                    par[node.right.val] = node.val
                    # if not in visited
                    if node.right.val == x:
                        x_ = True
                    elif node.right.val == y:
                        y_ = True
                    queue.append(node.right)
            if x_ and y_:
                if par[x] == par[y]:
                    return False
                return True
            if (x_ and not y_ )or (y_ and not x_):
                return False
        
        return False
            
