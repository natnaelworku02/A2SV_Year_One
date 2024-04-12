# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjlist = defaultdict(list)
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                adjlist[node].append(node.left)
                adjlist[node.left].append(node)
                stack.append(node.left)
            if node.right:
                adjlist[node].append(node.right)
                adjlist[node.right].append(node)
                stack.append(node.right)   

        # print(adjlist)
        # return None  
        queue = deque()
        visited = set()
        queue.append(target)
        visited.add(target)
        count = 0
        # print(queue,"hi")
        while queue:  
            if count == k:
                break
            for i in range(len(queue)):
                node = queue.popleft()
                
                for ind in adjlist[node]:
                    if ind not in visited:
                        queue.append(ind)
                        visited.add(ind)
            count += 1
            # print(queue,count)
        for i in range (len(queue)):
            queue[i] = queue[i].val
            # node = node.val
        # print(queue)
        return list(queue)


