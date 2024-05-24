class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class WordDictionary:

    def __init__(self):
        
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            
            ind = ord(letter) - 97
            
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        def helper(ind,cur_node):
            if ind >= len(word):
                # print("90",word[ind - 1])
                return False
            index = ord(word[ind]) - 97 if word[ind] != '.' else -1
            if index != -1 and not cur_node.children[index]:
                # print("02",word[ind])
                return False
            # print(word[ind],index)
            if index != -1 and cur_node.children[index].is_end and ind == len(word) - 1:
                return True
            
            if word[ind] != '.':
                # print(cur_node.children[index].is_end,word[ind])
                if helper(ind+1,cur_node.children[index]):
                    return True
            else:
                val = False

                for node in cur_node.children:
                    # print(node)
                    if node:
                        if node.is_end and ind == len(word) - 1:
                            return True
                        val = helper(ind + 1,node)
                        if val:
                            return True

            return False
        # print(word)
        # print(cur.children[ord(word[0]) - 97].is_end)

        return helper(0,cur) 
             
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)