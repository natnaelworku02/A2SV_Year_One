# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCA(root, node):
            if root:
                if node.val  == root.val:
                    return [node.val]
                if node.val < root.val:
                    ans = []
                    ans.append(root.val)
                    ans.extend(LCA(root.left,node))
                    return ans
                else:
                    ans = []
                    ans.append(root.val)
                    ans.extend(LCA(root.right,node))
                    return ans
            return []
        nodep = LCA(root,p)
        nodeq = LCA(root,q)
        i = max(len(nodep) - 1, len(nodeq) - 1)
        # print(nodep)
        # print(nodeq)
        ans = 0
        while i > -1:
            if i < len(nodep) and i < len(nodeq) and  nodep[i] == nodeq[i]:
                ans =  (nodep[i])
                break
            
            i -=1
        def BST(root,val):
            if root:
                if root.val == val:
                    return root
                elif root.val > val:
                    ans = BST(root.left,val)
                    return ans
                else:
                    ans = BST(root.right,val)
                    return ans
            return None
        node = BST(root,ans)
        return node 