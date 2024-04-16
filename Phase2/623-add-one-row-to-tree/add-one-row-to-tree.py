# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root,None)
            
        
        depth = depth - 1
        count = 1
        queue = deque()
        queue.append(root)
        flag = False
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if count == depth:
                    # print("hi")

                    
                    temp = TreeNode(val)
                    temp.left = node.left
                    node.left = temp
                
                    temp = TreeNode(val)
                    temp.right = node.right
                    node.right =  temp
                    
                    flag = True
                    # break
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if count == 1:
                    print(queue)
            if flag:
                return root
            count += 1
        
        return root
