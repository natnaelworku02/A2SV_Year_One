# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def BST(cur , count):
            if not cur:
                return
            count[cur.val] += 1
            # print("count of :",cur.val, count)
            BST(cur.left,count)
            BST(cur.right,count)
        count = defaultdict(int)
        BST(root, count)

        _max = max(count.values())
        # print(_max)
        ans = []
        for key,value in count.items():
            if value == _max:
                ans.append(key)
        return ans
        