class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = {chr(i):chr(i) for i in range(97,124)}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        
        def union(x,y):
            parx = find(x)
            pary = find(y)
            # print(parx,pary)
            if parx != pary:
                if parx < pary:
                    parent[pary] = parx
                else:
                    parent[parx] = pary
                    # print("hi",parx,pary)

            
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        ans = []
        # print(parent['e'])
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        
        return "".join(ans)