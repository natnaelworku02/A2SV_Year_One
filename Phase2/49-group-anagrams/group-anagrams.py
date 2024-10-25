class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
            di = defaultdict(list)

            for i,s in enumerate(strs):
                s = list(s)
                s.sort()
                s = tuple(s)
                di[s].append(i)
            ans = []
            for value in di.values():
                temp = []
                for val in value:
                    temp.append(strs[val])
                
                ans.append(temp)
            
            return ans