class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        def insert(word):
            cur = self.root
            # print(word)
            for ch in word:
                ind = ord(ch)  -97

                if not cur.children[ind]:
                    cur.children[ind] = TrieNode()
                
                cur = cur.children[ind]
            
            cur.is_end = True
        
        def search(word):
            cur = self.root
            res = []
            for ch in word:
                ind = ord(ch) - 97
                if not cur.children[ind]:
                    # print("hi",ch)
                    return word
                cur = cur.children[ind]
                res.append(ch)
                if cur.is_end:
                    # print(res,word)
                    return ''.join(res)
        
            return word
        

        for word in dictionary:
            insert(word)
        
        # print(self.root.children[ord('c') - 97])
        ans = []
        sentence = sentence.split()

        for word in sentence :
            ans.append(search(word))
            # print("________")
        
        res = [ans[0]+ " "]
        if len(ans) >  1:
            res.extend(" ".join(ans[1:]))
        return ''.join(res)

            