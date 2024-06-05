class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
    
        di= defaultdict(int)
        for ch in words[0]:
            di[ch] += 1
        
        for  i in range(1,len(words)):
            char_count = defaultdict(int)
            for ch in words[i]:
                char_count[ch] += 1
            k = []
            for key , value in char_count.items():
                if key not in di:
                    k.append(key)
                elif value  != di[key]:
                    if value < di[key]:
                        di[key] = value
            for key in k:
                char_count.pop(key)
            k = []
            for key , value in di.items():
                if key not in char_count:
                    k.append(key)
            for key in k:
                di.pop(key)
        
        ans = []
        for key, value in di.items():
            ans.extend([key] * value)
        
        return ans



        
