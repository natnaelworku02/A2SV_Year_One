# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        di = defaultdict(list)
        def preorder(root,depth):
            if root:
                # max_depth = max(max_depth,depth)
                
                di[depth].append(root.val)
                val1 = (preorder(root.left,depth + 1))
                val2 = (preorder(root.right, depth + 1))
                return max(val1,val2,depth)
            return 0
            
        max_depth = preorder(root,0)
        ans = []
        print(di,max_depth)
        ind = 0
        right_to_left = True
        while ind <= max_depth:
            if right_to_left:
                if di[ind]:
                    ans.append(di[ind])
            else:
                if di[ind]:
                    ans.append(di[ind][::-1])
            ind += 1
            right_to_left = not right_to_left
        return ans

