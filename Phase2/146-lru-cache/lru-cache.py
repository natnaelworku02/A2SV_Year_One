class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val

        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left , self.right = Node(0,0),Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        
        if key in self.cache:
            # print(self.cache[key].key)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    
    def remove(self,node):
        prev,nxt = node.prev, node.next

        prev.next,nxt.prev = nxt,prev



    
    def insert(self,node):
        prev = self.right.prev

        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev
    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # print(self.cache)
            lru = self.left.next
            self.remove(lru)
            if lru.key in self.cache:
                # print(self.cache[lru])
                del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)