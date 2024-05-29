class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            ind = ord(letter) - 97
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
            cur.count += 1
        
        # cur.is_end = True
        

    def search(self, word: str) -> bool:
        ans = 0
        cur = self.root
        for letter in word:
            ind = ord(letter)  - 97
            
            cur = cur.children[ind]
            ans += cur.count
        
        # if cur.is_end:
        #     return True
        
        # return False
        return ans
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        for word in words:
            self.insert(word)
        
        arr = []

        for word in words:
            arr.append(self.search(word))
        
        return arr
        