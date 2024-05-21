class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        

        adjlist = defaultdict(list)
        num = defaultdict(int)
        for j in range(len(recipes)):
                for ing in ingredients[j]:
                    adjlist[ing].append(recipes[j])
                # print(ingredients[i])
                # num[ingredients[j]]+=1
                num[recipes[j]] += len(ingredients[j])

        
        di = set(recipes)
        # print(adjlist)
        # print(num)
        queue = deque()

        for supply in supplies:
            queue.append(supply)
        # print(queue)
        ans = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # print(node)
                if node in di:
                    ans.append(node)
                    di.remove(node)

                for ind in adjlist[node]:
                    num[ind] -=1
                    if num[ind] == 0:
                        print(ind)
                        queue.append(ind)
        
        return ans
