class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i:i for i in range(len(s))}
        

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        def union(x,y):
            parx = find(x)
            pary = find(y)

            if parx != pary:
                if s[parx] < s[pary]:
                    parent[pary] = parx
                else:
                    parent[parx] = pary
            
        
        for x,y in pairs:
            union(x,y)
            # print(parent)
        
        di = defaultdict(list)

        for i in range(len(s)):
            heappush(di[find(i)],s[i])
        
        # print(parent)
        # print(di)
        ans = []
        for i in range(len(s)):
            ans.append(heappop(di[find(i)]))
        
        return ''.join(ans)