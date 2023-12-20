class RandomizedSet:

    def __init__(self):
        self.randset={}
        self.data=[]
        self.index=0

    def insert(self, val: int) -> bool:
        if val in self.randset:
            return False
        else:
            self.data.append(val)
            self.randset[val]=self.index
            self.index+=1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.randset:
            x = self.data[self.index-1]

            self.data[self.randset[val]]  , self.data[self.index-1]=self.data[self.index-1],self.data[self.randset[val]] 
            self.randset[x]=self.randset[val]
            del self.randset[val]
            self.data.pop()
            self.index-=1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        random_number = random.randint(0,self.index-1)
        return self.data[random_number]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()