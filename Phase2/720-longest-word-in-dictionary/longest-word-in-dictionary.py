class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
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
        
        cur.is_end = True
    
    def maxLengWord(self):

        cur = self.root
        # ans = 0
        word = ''
        stack =[]

        for i,child in enumerate(cur.children):
            if child:
                stack.append([child,[chr(i + 97)]])
        # print(stack)
        while stack:
            node,val = stack.pop()
            # print(val)
            if node.is_end and len(val) > len(word):
                word = ''.join(val)
            elif node.is_end and len(val) == len(word) and ''.join(val) < word:
                word = ''.join(val)
            # print(word)
            if node.is_end:
                for i,child in enumerate(node.children):
                    # print(child)
                    if child:
                        val.append(chr(i+97))
                        # print(val)
                        stack.append([child,val.copy()])
                        val.pop()
        
        return word

    
    def longestWord(self, words: List[str]) -> str:

        for word in words:
            self.insert(word)
        # print(chr(14+97))
        return self.maxLengWord()
        



        