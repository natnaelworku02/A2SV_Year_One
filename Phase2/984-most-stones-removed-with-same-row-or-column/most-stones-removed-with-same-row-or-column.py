class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {tuple(coord): tuple(coord) for coord in stones}
        size = {tuple(coord) : 1 for coord in stones}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(x,y):
            parx = find(x)
            pary = find(y)

            if parx != pary:
                if size[parx] > size[pary]:
                    parent[pary] = parx
                    size [parx] += size[pary]
                else:
                    parent[parx] = pary
                    size [pary] += size[parx]
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0] == stones[j][0]:
                    union(tuple(stones[i]),tuple(stones[j]))
                elif stones[i][1] == stones[j][1]:
                    union(tuple(stones[i]),tuple(stones[j]))
        
        count = 0

        for key,val in parent.items():
            if key == val:
                count +=1
            
        return len(stones) - count

