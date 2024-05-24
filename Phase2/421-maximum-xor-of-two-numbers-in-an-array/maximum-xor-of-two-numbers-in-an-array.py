class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        # self.is_end = False
    
    
class Solution:
    
    def __init__(self):
        self.root = TrieNode()

    def findMaximumXOR(self, nums: List[int]) -> int:

        def insert(bits):
            cur = self.root
            for bit in bits:
                ind = int(bit)
                if not cur.children[ind]:
                    cur.children[ind] = TrieNode()
                
                cur = cur.children[ind]
            
            # cur.is_end = True
        
        arr = []
        
        for num in nums:
            val = list(bin(num)[2:]) [::-1]
            # print(val)
            if len(val) < 32:
                val.extend(['0'] * (32 - len(val)))
            # print(val)
            
            val = val [::-1]
            arr.append(val)
        
        # print(arr)

        for num in arr:
            insert(num)
        
        ans = 0
        for num in arr:
            res = []
            cur = self.root

            for bit in num:
                ind = int(bit)
                if ind == 0:
                    if cur.children[1]:
                        res.append("1")
                        cur = cur.children[1]
                    else:
                        res.append("0")
                        cur = cur.children[0]
                else:
                    if cur.children[0]:
                        res.append("1")
                        cur = cur.children[0]
                    else:
                        res.append("0")
                        cur = cur.children[1]
            
            res = ''.join(res)
            res = int(res,2)
            ans = max(ans,res)
        
        return ans



        return 0

               